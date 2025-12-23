<div style = "color: white">

# This will just be a Daily Log of what I did
I may have busy days so I will just not write anything for that day...

## Day 12/16/2025

Today I will be working on learning about data structures, 
<br> 
hopefully I can get through a lot because I have used data structures in python (with JSON).

Thought with not the best formats...

---

### 1. Lists
There wasn't really a lot... I already go through this in python coding.

A list in data structures just holds objects or values. These values can be modified, removed, new values can be added, and you can split lists, sort them, and grab the length of it all. Pretty simple stuff

I also learned basic classifications of a list, including key characteristics.

Some key characteristics are listed below

- Ordered: The values or objects in a list keep the order they were made / added in

- Dynamic Size: This just means that the size can be changed during runtime

- Indexed: Objects and values in a list can be accessed by something called an index. <br> Which just means that, starting at zero (in most languages), you count up in a list and grab the object or value at that number.<br> Not all languages have lists that can be indexed! (I don't know if that makes sense for you)

- Mutable: This is just a fancy word for the list can be changed during runtime (not static).

- Flexible Data Types: Some languages (not all) can have flexible data types inside that list! <br>Like in python, it could be a messy list full of strings, ints, floats, anything! But in some langauges like C#, it isn't that flexible because you have to define what is in the list beforehand...

---

### 2. Dictionaries
I decided to tackle dictionaries next because I use them almost as much if not more than lists in my day to day python coding!

Dictionaries just use something called Key-Value pairs.<br> Which means that if you have something like the inventory you need to access in a video game. You would make this...
```python
game_data = {
    "Inventory": ["List", "Of", "Items"]
}
```
For Game data, the key would be "Inventory" and "Inventory"'s data would be ["List", "Of", "Items"].


To access dictionary's values it pretty easy, it's just data[key], though you need to make sure that data has that key your specifying, or it will throw an error.

I like do use data.get(key, None) because it will search that dictionary for that key, and if it is not there, it will just return None

Some Core Concepts for dictionaries...

- Unique Keys: Each key in a dictionary is different from the others

- Flexible Values: Values can be any data type, even more dictionaries for complex structures

- Keys must be immutable: Just means that the key can't be something like a list, where a list can be changed

---

### Difference?

The difference between lists and dictionaries are pretty straightforward.

If you just need an ordered collection of items and care about position, use a list.

If you need an organized way to hold a lot (or a little) amount of data, use dictionaries.

---
### Information on today
Time Spent: ~30-40 minutes<br>
Sources Used: Internet, some docs<br>
Mostly just reviewed some of what I know about Data Structures


## Day 12/17/2025

Today I will continue learning about data structures.

---

### 1. Stacks

Going into this, I have no clue what a stack is...

So a stack is a linear data structure that follows LIFO. LIFO stands for Last In First Out.
<br>
This just means that the last element in the stack is the first on to be removed.
<br>
Think like a stack of rings, you gotta remove them from top to bottom; but you place them bottom to top.

Core Operations in stacks include

- Push: Adds an element to the top of the stack.

- Pop: Removes **and returns** the object at the top

- Peek (or Top): Returns the object at the top **without removing it**

- isEmpty and isFull: Just returns a bool if the stack is empty or full

I looked around for some uses of stacks in programming language and I found the following.

- History: Like the back button on a webpage

- Sorting Algorithms: You can sort lists and arrays by using a stack method.

A way to use this in python is kinda simple if you understand syntax.

```python
# Create a stack (list)
stack = []

# Add Values to the stack
stack.append("a")
stack.append("b")
stack.append("c")

# See values in the stack
print(stack)

# Remove values in a stack and print
# For this .pop() is used
print(stack.pop())
print(stack.pop())
print(stack.pop())

# Display the empty stack
print(stack)
```

Now the output would look like this...

```python
["a", "b", "c"]
"c"
"b"
"a"
[]
```

I read this <a href="https://www.geeksforgeeks.org/python/stack-in-python/">website (click here)</a> to see how stacks are used in Python.

### 2. Queues

I knew less about this than I did about stacks...

I googled what a queue is and found that these are some key concepts.

- Front (Head): The side where objects are removed

- Rear: The side where objects are added

- Enqueue (Push): Adds an object to the rear

- Dequeue (Pop): Removes an object from the front

- Empty / Size: Checks the size of the queue

- Uses FIFO: First in, First out

I found some interesting implementations for this, including 

- Arrays: fixed or dynamic => often with pointers?

- Linked Lists: Allows multiple lists to be used *and* it points to the next list

- Circular Queue: Just imagine a list that repeats itself + can have values *added*

It wasn't as complicated as I thought... it's actually pretty simple to use in python!

Here's an example to use where you make a queue q and add values, then remove them in queue style

```python
q = []

# Add Items from REAR
q.append("a")
q.append("b")
q.append("c")

# Display what is in the current queue
print(f"Current Items in Queue: {q}")

# Remove + Display removed items from queue
print("Elements Dequeued")
print(q.pop(0)) # pop(0) so its from the front (Because of FIFO)
print(q.pop(0))
print(q.pop(0))

# List what the queue is now
print(f"Current Items in Queue: {q}")
```
Here's the output...
```
Current Items in Queue: ["a", "b", "c"]
Elements Dequeued
a
b
c
Current Items in Queue: []
```

I found a really cool example <a href="https://www.geeksforgeeks.org/python/queue-in-python/">***here***</a> where you use collection.deque library

```python
from collections import deque
q = deque()

q.append('a')
q.append('b')
q.append('c')
print(f"Current Items in Queue: {q}")

print("Elements Dequeued")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print(f"Current Items in Queue: {q}")
```

and one using a queue specific library

```python
from queue import Queue
q = Queue(maxsize=3)
print("Initial size:", q.qsize())

q.put('a')
q.put('b')
q.put('c')
print("Is full:", q.full())

print("Elements dequeued from the queue:")
print(q.get())
print(q.get())
print(q.get())
print("Is empty:", q.empty())

q.put(1)
print("Is empty:", q.empty())
print("Is full:", q.full())
```

### Difference?
Stacks and Queues are used for different things and use different *"rules"*.<br>Stacks use LIFO while Queues use FIFO.
<br>

Stacks => undo/redo, parsing, recursion, backtracking

Queues => scheduling, buffering, task processing, pipelines

### Information on Today
Time Spent: ~45 minutes<br>
Sources: Internet and <a href="https://www.geeksforgeeks.org">GeeksForGeeks.org</a><br>
Learned some new stuff I didn't know works that way.

## Day 12/18/2025

I reviewed and made some scripts on what I studied...

I went over stacks and queues, as well as dictionaries and lists.
<br>
Here's some links to the practice files

- [Lists](Data%20Structures%20Playground/lists.py)

- [Dictionaries](Data%20Structures%20Playground/dictionaries.py)

- [Queues](Data%20Structures%20Playground/queues.py)

- [Stacks](Data%20Structures%20Playground/stacks.py)

I also started working on some projects including all of these (or most).<br>Don't worry... I explain the code underneath the project and in the file for you guys.

1. [Task Manager](Code/task%20manager.py)

    - Breaking down the problem.
        - Finding a way to include lists, dictionaries, stacks and queues?
            - Add a undo button
            - Dictionaries for task details + a list of the tasks
            - Queues to run in the background with threading
        - Going to need a way to grab user input from CLI
        - Parse User Input
        - Add, Remove, or View Tasks

    - Creating Different methods.
        - An add task method
        - A remove task method
        - And a view task method

    - Running the program.
        - Use a class and call a run method

### Information on Today

Time Spent: ~1 hr<br>
Sources: Notes from yesterday.<br>
I created a few practice programs to reinforce the data structures I learned. <br>I then got started on creating the task manager. I made methods to add stuff to a queue, continuously process the queue (until program stopped) with threading (PS Threading is overkill for this, but it's just some practice because I have used it before).<br> And made a method to add tasks.

## Day 12/19/25

Today I'm just gonna finish creating the task manager (maybe another project for extra practice???)

I finished the task manager!<br> I made a stack for history (undo changes), made a remove and adding task + made tasks dictionaries<br>and a list holding all the tasks! I also used a queue with threading (THREADING IS OVERKILL FOR THIS)!

I had to do some research on thread locks, but other than that I made this with only the previous notes!<br>
Of course you can make this better, this is a very "rough" task manager... I only made it to practice data structers.<br>
I included comments so you can see what each part of code does!

Here is the code for the (currently) finished task manager:
```python
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
        self.task_history = [] # Stack of history

    # Helper Methods
    def add_task(self, name: str, importance: str, details: str | None = None) -> None:
        new_task = self.task_layout.copy()  # Copy a base layout => If we don't we would be changing self.task_layout
        new_task["Name"] = name  # No need for .get() because we know for sure we have a Name key
        new_task["Importance"] = importance
        new_task["Details"] = details if details else "No Details Provided."

        # Add the task to the list (thread-safe)
        with self.lock:
            self.tasks.append(new_task)
            self.task_history.append(self.tasks.index(new_task))

    def remove_task(self, number: int) -> None | str:
        try:
            self.task_history.append(self.tasks.pop(number))
        
        except:
            return "Not a valid task number."

    def view_tasks(self) -> None:
        # View that tasks are being changed
        print("Tasks:\n")

        for task in self.tasks:
            print(f"Task Name: {task["Name"]}") # Access values by KEY
            print(f"Task Importance: {task["Importance"]}")
            print(f"Task Details: {task["Details"]}")
            print()

        input("Press enter to continue. ")

    def undo(self) -> None:
        if self.task_history:
            command = self.task_history.pop()
            if isinstance(command, int):
                self.tasks.pop(command)
            else:
                self.tasks.append(self.task_history.pop())

    # Queue stuff
    def add_to_queue(self, func, args: tuple[Any, ...] = ()) -> None:
        self.queue.append((func, args))

    # Actual thread
    def _run_queue(self) -> None:
        # This just checks if something is in the queue, but if nothing it just idles
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
        # Safely stop the queue thread by setting the event
        self.kill_thread_event.set()
        if self.queue_thread:
            # Wait for thread to stop
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
                # Get Task Data (VERY BASIC)
                name = input("Task Name > ")
                importance = input("Importance (High, Medium, Low) > ")
                details = input("Details (Press Enter for None) > ")
                self.add_to_queue(self.add_task, (name, importance, details if details else None))

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

        # Stop Thread
        self.stop_queue()

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()

```

### Quick Reflection

I sort of messed up a bit with threading (because I was somewhat "rusty" with locks). I need to keep consistency with my locks (using with self.lock everywhere I modify self.tasks).<br>
Also for my stack design, I shouldn't be using raw data, more like commands. It should be like ("add", task) or ("remove", task, index) (I'll need index because there may be duplicated tasks...).<br>
I won't be updating the code because this was just for practice, but in the future I will be changing code to include these things.

### Information on Today
Time Spent: ~30-45 min<br>
Sources: Notes<br>
I wasn't completely sure on queues and stacks, so I used my notes. I'm quite sure that if you read through my code **[here](Code/task%20manager.py)** while looking at my notes, you would be able to understand it!

## Day 12/20/25

I watched a Video on Big-O Notation *[(Click Here)](https://www.youtube.com/watch?v=XMUe3zFhM5c&t=40s)*

Big-O Notation Notes

- Describes the preformance of an algorithm as data increases

- Ignores small operations like O(n + 1) is just O(n)

- N is the amount of data used

Examples of notation (In Video at 6:06):
- O(1) => constant time: Fastest, doesn't take more time (steps) with larger data sets

- O(n) => linear time: Kinda slow, grows linear depending on data

- O(log n) => logarithimc time: Little bit slower than constant time, but faster than linear. It also doesn't have much of a grow on steps for larger data sets

- O(n^2) => quadratic time: Really slow, takes n^2 steps to complete

- O(n!) => factorial time: Really **REALLY** slow, don't ever use this for everyday things

### Examples
O(1): Constant Time
```python
def addUp(n: int) -> int:
    return n * (n + 1) / 2
```
Now if n is 1000000, then it would take about 3 steps because it does 3 "operations"

O(log n): Logarithmic Time
```python
def log_n_loop(n: int) -> int:
    count = 0
    i = n
    while i > 1:
        # The key is dividing the problem space in half
        i = i // 2
        count += 1
        print(f"Current i: {i}")
    return count

input_size = 16
ops = log_n_loop(input_size)
print(f"Number of operations for n = {input_size}: {ops}")
```

This runs 4 times (8 -> 4 -> 2 -> 1)

O(n): Linear Time
```python
def addUp(n: int) -> int:
    sum = 0

    for _ in range(n):
        sum += 1

    return sum
```

If n is 1000000, then it would take about 1000000 steps.

O(n^2): Quadratic Time
```python
def printPairs(items: list) -> None:
    n = len(items)
    for i in range(n):
        for j in range(n):
            print(f"{items[i]} and {items[j]}")
```

If the input list is 3 items, then the outer loop would run 3 times and for each time the inner loop would run 3 times.

### Information on Today
Time Spent: ~20-30 minutes<br>
Sources: [Bro Code Video](https://www.youtube.com/watch?v=XMUe3zFhM5c&t=40s)<br>
Learned that different notations in Big-O Scale a lot faster than others.

## Day 12/21/25

Started creating a project (for ONLY sundays)

[Project Link](../PDU/README.md)

## Day 12/22/25

Today I am going to be reading through my previous task manager code and labeling functions and loops with Big-O notation...

I doubled checked if my annotations were right and most of them were!<br>Finished code:
```python
import threading
from collections import deque
from time import sleep
from typing import Any
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
        self.queue = deque()  # Init our queue
        self.kill_thread_event = threading.Event()
        self.lock = threading.Lock()  # Protect shared state
        self.queue_thread: threading.Thread | None = None
        self.task_history = [] # Stack of history

    # Helper Methods
    # O(n)
    def add_task(self, name: str, importance: str, details: str | None = None) -> None:
        new_task = self.task_layout.copy()  # Copy a base layout => If we don't we would be changing self.task_layout
        new_task["Name"] = name  # No need for .get() because we know for sure we have a Name key
        new_task["Importance"] = importance
        new_task["Details"] = details if details else "No Details Provided."

        # Add the task to the list (thread-safe)
        with self.lock:
            self.tasks.append(new_task)
            self.task_history.append(self.tasks.index(new_task))

    # O(n)
    def remove_task(self, number: int) -> None | str:
        try:
            self.task_history.append(self.tasks.pop(number))
        
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
            if isinstance(command, int):
                self.tasks.pop(command)
            else:
                self.tasks.append(self.task_history.pop())

    # Queue stuff
    # O(1)
    def add_to_queue(self, func, args: tuple[Any, ...] = ()) -> None:
        self.queue.append((func, args))

    # Actual thread
    # O(1): per iteration
    def _run_queue(self) -> None:
        # This just checks if something is in the queue, but if nothing it just idles
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
    # O(1)
    def run_queue(self) -> None:
        self.queue_thread = threading.Thread(target=self._run_queue)
        self.queue_thread.start()

    # Method for stopping the thread
    def stop_queue(self) -> None:
        # Safely stop the queue thread by setting the event
        self.kill_thread_event.set()
        if self.queue_thread:
            # Wait for thread to stop
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
                # Get Task Data (VERY BASIC)
                name = input("Task Name > ")
                importance = input("Importance (High, Medium, Low) > ")
                details = input("Details (Press Enter for None) > ")
                self.add_to_queue(self.add_task, (name, importance, details if details else None))

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

        # Stop Thread
        self.stop_queue()

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
```

</div>