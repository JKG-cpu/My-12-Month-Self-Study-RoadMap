import threading
from collections import deque
from time import sleep
from typing import Any
from os import system, name

# I'll need these imports for a queue 
# and threading to run that queue in the background (This is overkill... but useful to understand for later things)
# and sleep so I don't have the thread running at 100% (adding sleep(.5) or something)

# This is just to clear the terminal during runtime
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
        self.queue = deque()  # Init our queue
        self.kill_thread_event = threading.Event()
        self.lock = threading.Lock()  # Protect shared state
        self.queue_thread: threading.Thread | None = None

    # Helper Methods
    def add_task(self, name: str, importance: str, details: str | None = None) -> None:
        new_task = self.task_layout.copy()  # Copy a base layout => If we don't we would be changing self.task_layout
        new_task["Name"] = name  # No need for .get() because we know for sure we have a Name key
        new_task["Importance"] = importance
        new_task["Details"] = details if details else "No Details Provided."

        # Add the task to the list (thread-safe)
        with self.lock:
            self.tasks.append(new_task)

    def remove_task(self) -> None:
        pass

    def view_tasks(self) -> None:
        print(self.tasks)
        input()

    # Queue stuff
    def add_to_queue(self, func, args: tuple[Any, ...] = ()) -> None:
        self.queue.append((func, args))

    # Actual thread
    def _run_queue(self) -> None:
        while not self.kill_thread_event.is_set() or self.queue:
            if self.queue:
                # Grab leftmost item
                function, args = self.queue.popleft()
                try:
                    function(*args)
                except Exception as e:
                    print(f"Thread error: {e}")
            else:
                sleep(.05)

    # Method for starting the thread
    def run_queue(self) -> None:
        self.queue_thread = threading.Thread(target=self._run_queue)
        self.queue_thread.start()

    # Method for stopping the thread
    def stop_queue(self) -> None:
        self.kill_thread_event.set()
        if self.queue_thread:
            self.queue_thread.join()

    # A Run Method
    def run(self) -> None:
        self.run_queue() # Start running the background thread

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
                name = input("Task Name > ")
                importance = input("Importance (High, Medium, Low) > ")
                details = input("Details (Press Enter for None) > ")
                self.add_to_queue(self.add_task, (name, importance, details if details else None))

            # View Tasks
            elif user_input.startswith("V"):
                self.view_tasks()

        # Stop Thread
        self.stop_queue()

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
