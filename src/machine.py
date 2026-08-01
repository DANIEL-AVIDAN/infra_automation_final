from datetime import datetime
from pathlib import Path
from typing import Literal

import json
import subprocess

from pydantic import BaseModel, Field, ValidationError


def get_log_path():
    return Path(__file__).parent.parent / "logs" / "provisioning.log"


def get_instances_path():
    return Path(__file__).parent.parent / "configs" / "instances.json"


def load_instances():
    instances_path = get_instances_path()

    with open(instances_path, "r") as file:
        instances = json.load(file)

    return instances


def save_instances(instances):
    instances_path = get_instances_path()

    with open(instances_path, "w") as file:
        json.dump(instances, file, indent=4)


def write_log(message):
    log_path = get_log_path()

    with open(log_path, "a") as log_file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{current_time}] {message}\n")


class MachineData(BaseModel):
    name: str = Field(min_length=3)
    os: Literal["linux", "windows"]
    cpu: int = Field(ge=1, le=10)
    ram: int = Field(ge=2, le=20)


class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram


    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
            }


def create_machine():
    try:
        name = input("Enter machine name: ").strip()
        os = input("Enter operating system: ").strip().lower()
        cpu = input("Enter CPU count: ").strip()
        ram = input("Enter RAM amount: ").strip()

        machine_data = MachineData(
            name=name,
            os=os,
            cpu=cpu,
            ram=ram
        )

        machine = Machine(
            name=machine_data.name,
            os=machine_data.os,
            cpu=machine_data.cpu,
            ram=machine_data.ram
        )

        instances = load_instances()

        if machine.name in instances:
            print(f"Machine '{machine.name}' already exists.")
            write_log(
                f"FAILED - Machine '{machine.name}' already exists."
            )
            return None

        # instances[machine.name] = {
        #     "name": machine.name,
        #     "os": machine.os,
        #     "cpu": machine.cpu,
        #     "ram": machine.ram
        # }
        instances[machine.name] = machine.to_dict()

        save_instances(instances)

        write_log(
            f"SUCCESS - Machine '{machine.name}' created successfully."
        )

        return machine

    except ValidationError as error:
        for err in error.errors():
            field = err["loc"][0]
            message = err["msg"]

            print(f"Error in '{field}': {message}")

            write_log(
                f"FAILED - Machine '{name}' - {field}: {message}"
            )

        return None


def delete_machine():
    name = input("Enter machine name to delete: ").strip()

    instances = load_instances()

    if name not in instances:
        print(f"Machine '{name}' does not exist.")

        write_log(
            f"FAILED - Machine '{name}' could not be deleted "
            "because it does not exist."
        )

        return False

    del instances[name]

    save_instances(instances)

    write_log(
        f"SUCCESS - Machine '{name}' deleted successfully."
    )

    print(f"Machine '{name}' deleted successfully.")

    return True


def run_script():
    project_root = Path(__file__).parent.parent
    script_path = project_root / "scripts" / "myscript.sh"

    try:
        subprocess.run(
            ["bash", str(script_path)],
            check=True
        )

        print("Script executed successfully.")

        write_log(
            "SUCCESS - myscript.sh executed successfully."
        )

    except subprocess.CalledProcessError as error:
        print("Script execution failed.")

        write_log(
            f"FAILED - myscript.sh exited with code "
            f"{error.returncode}."
        )