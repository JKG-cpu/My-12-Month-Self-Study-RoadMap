from os import system, name

# I'll need these imports for a queue 
# and threading to run that queue in the background (This is overkill... but useful to understand for later things)
# and sleep so I don't have the thread running at 100% (adding sleep(.5) or something)

# This is just to clear the terminal during runtime
# O(1)
def cc():
    system("cls" if name == "nt" else "clear")

# A Class to manage the whole thing
class TaskManager:
    def __init__(self) -> None:
        self.tasks = []  # A List to store all the tasks
        self.task_layout = {   # What a task would look like
            "Name": "",  # Key / Value Pair
            "Importance": ["Low", "Medium", "High"],  # Options for setting importance
            "Details": ""  # Task Details (If want to add, defaults to None)
        }
        self.task_history = [] # Stack of history

    # Helper Methods
    # O(1)
    def add_task(self, name: str, importance: str, details: str | None = None) -> None:
        new_task = self.task_layout.copy()  # Copy a base layout => If we don't we would be changing self.task_layout
        new_task["Name"] = name  # No need for .get() because we know for sure we have a Name key
        new_task["Importance"] = importance
        new_task["Details"] = details if details else "No Details Provided."

        self.tasks.append(new_task)
        index = len(self.tasks) - 1
        self.task_history.append(("add", index))

    # O(n)
    def remove_task(self, number: int) -> None | str:
        try:
            self.task_history.append(("remove", self.tasks.pop(number), number))
            # pop(index) → O(n)
            # append history → O(1)
            # total → O(n)

        except:
            return "Not a valid task number."

    # O(n)
    def view_tasks(self) -> None:
        # View that tasks are being changed
        print("Tasks:\n")

        for task in self.tasks:
            print(f"Task Name: {task["Name"]}") # Access values by KEY
            print(f"Task Importance: {task["Importance"]}")
            print(f"Task Details: {task["Details"]}")
            print()

        input("Press enter to continue. ")

    # O(n)
    def undo(self) -> None:
        if self.task_history:
            command = self.task_history.pop()
            if command[0] == "add":
                self.tasks.pop(command[1])
            
            elif command[0] == "remove":
                self.tasks.insert(command[2], command[1])

    # A Run Method
    def run(self) -> None:
        # Main Loop
        running = True
        while running:
            cc()
            user_input = input("> ").strip().title()

            # Exit
            if user_input.startswith("E"):
                running = False
                continue
        
            # Add Task
            elif user_input.startswith("A"):
                # Get Task Data (VERY BASIC)
                name = input("Task Name > ")
                importance = input("Importance (High, Medium, Low) > ")
                details = input("Details (Press Enter for None) > ")
                self.add_task(name, importance, details if details else None)

            # View Tasks
            elif user_input.startswith("V"):
                self.view_tasks()

            # Remove Task
            elif user_input.startswith("R"):
                number = input("Enter a number > ")
                return_value = self.remove_task(int(number) - 1) # Subtrace 1 due to python's indexing
                if return_value:
                    print(return_value)
                    input("Press enter to continue.")

            # Undo
            elif user_input.startswith("U"):
                self.undo()

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
