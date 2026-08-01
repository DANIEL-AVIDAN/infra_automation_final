# python-final-project
#להוסיף הסבר מלא כיצד הפרויקט הולך לרוץ

#להוסיף כאן את הנתיב לקובץ הrequirements ואיזה פקודה להריץ כדי להתקין ממנו
#להוסיף כאן הסבר במילים גם על כל אחד מקבצי הקוד שלי מה הוא עושה
#להכניס כאן גם צעדים איך להרים את האפליקציה
#ולהכניס כאן גם דוגמאות איזה. מכונות הוא צריך ליצור ומה אמור להצליח ומה לא

# Infrastructure Provisioning Simulator

## Overview

Infrastructure Provisioning Simulator is a Python-based CLI application that simulates infrastructure provisioning.

The application allows users to create and manage virtual machine (VM) configurations, validate user input, execute a provisioning Bash script, and log all operations.

This project was developed as part of the **Python module in a DevOps course** and serves as the foundation for future infrastructure automation projects.

---

# Project Structure

```text
infra-automation/
│
├── configs/
│   └── instances.json          # Stores all existing virtual machines
│
├── logs/
│   └── provisioning.log        # Stores application logs
│
├── scripts/
│   └── myscript.sh             # Provisioning Bash script
│
├── src/
│   ├── infra_simulator.py      # Main application (CLI menu)
│   └── machine.py              # Machine logic and helper functions
│
├── requirements.txt
└── README.md
```

---

# Features

The application currently supports:

- Create a new virtual machine
- Delete an existing virtual machine
- Execute a provisioning Bash script
- Store machine configurations in a JSON file
- Validate user input using Pydantic
- Log successful and failed operations
- Prevent duplicate machine names

---

# Machine Validation Rules

Each virtual machine must contain the following information:

| Field | Validation |
|-------|------------|
| Name | Minimum 3 characters |
| Operating System | linux or windows |
| CPU | Integer between 1 and 10 |
| RAM | Integer between 2 and 20 |

If invalid data is entered, the application displays a validation error and the operation is logged.

---

# Logging

All application events are written to:

```text
logs/provisioning.log
```

The log file records:

- Successful machine creation
- Failed machine creation
- Successful machine deletion
- Failed deletion attempts
- Provisioning script execution results

Each log entry contains a timestamp.

---

# Configuration Storage

All virtual machines are stored inside:

```text
configs/instances.json
```

Example:

```json
{
    "web-server": {
        "name": "web-server",
        "os": "linux",
        "cpu": 4,
        "ram": 8
    }
}
```

---

# Technologies Used

- Python 3
- Pydantic
- JSON
- Bash
- subprocess
- pathlib

---

# Installation

## 1. Install the project dependencies

From the project root directory run:

```bash
pip install -r requirements.txt
```

Current dependency:

```text
pydantic>=2,<3
```

---

# Running the Application

From the project root directory run:

```bash
python src/infra_simulator.py
```

After launching the application, the following menu will be displayed:

```text
Infra Simulator

1. Create machine
2. Delete machine
3. Run provisioning script
4. Exit
```

---

# Design Decisions

The project was designed with a modular structure.

- Machine management logic is implemented in `machine.py`.
- The CLI menu is implemented in `infra_simulator.py`.
- Machine configurations are stored in `configs/instances.json`.
- Application logs are written to `logs/provisioning.log`.
- Project paths are resolved using `pathlib.Path`, allowing the application to run correctly regardless of the current working directory.
- User input validation is performed using **Pydantic** before any machine is created.

---

# Future Improvements

This project is intended to evolve throughout the DevOps course.

Future enhancements may include:

- AWS infrastructure provisioning
- Terraform integration
- Additional provisioning scripts
- Support for more operating systems and services

---

# Author

Developed as part of the **Python module in a DevOps course**.