# זה העמוד הראשי שמפעילים בתוכנית
#הוא יקח את המחלקה machine ויפעיל אותה ויצור מכונות על פי קלט מהמשתמש

from machine import create_machine, delete_machine, run_script

def main():
    while True:
        print("\nInfra Simulator")
        print("1. Create machine")
        print("2. Delete machine")
        print("3. Run provisioning script")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_machine()
            

        elif choice == "2":
            delete_machine()
            

        elif choice == "3":
            run_script()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()