import threading
from collections import deque
from time import sleep
from typing import Any
# I'll need these imports for a queue 
# and threading to run that queue in the background
# and sleep so I don't have the thread running at 100% (adding sleep(.5) or something)

# A Class to manage the whole thing
class TaskManager:
    def __init__(self) -> None:
        self.tasks = [] # A List to store all the tasks
        self.task_layout = {   # What a task would look like
            "Name": "", # Key / Value Pair
            "Importance": ["Low", "Medium", "High"], # Options for setting importance
            "Details": "" # Task Details (If want to add, defaults to None)
        }
        self.queue = deque() # Init are queue

    # Helper Methods
    def add_task(self, name: str, importance: str, details: str | None) -> None:
        new_task = self.task_layout.copy() # Copy a base layout => If we don't we would be changing self.task_layout
        new_task["Name"] = name # No need for .get() because we know for sure we have a Name key
        new_task["Importance"] = importance
        new_task["Details"] = details if details else "No Details Provided."

        # Add the task to the list
        self.tasks.append(new_task)

    def remove_task(self) -> None:
        pass

    def view_tasks(self) -> None:
        pass

    # Queue stuff
    def add_to_queue(self, func: function, args: Any = None) -> None:
        self.queue.append((func, args))

    # Actual thread
    def _run_queue(self) -> None:
        while True:
            if self.queue.count != 0:
                # Grab leftmost item
                function, arg = self.queue.popleft()
                if arg:
                    function(*arg)
                else:
                    function()

            else:
                sleep(.5)
    
    # Method for starting the thread
    def run_queue(self) -> None:
        queue_thread = threading.Thread(target = self._run_queue, daemon = True)
        queue_thread.start()

    # A Run Method
    def run(self) -> None:
        pass

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()