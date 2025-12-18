from time import sleep
from collections import deque

q = deque()

# Add Some Tasks
q.append(("Open Web", 1))
q.append(("Type in Home Address", 2))

while q:
    task, time = q.popleft()
    print(f"Task: {task}")
    sleep(time)
    print(f"Task Complete: {task}")

print(f"Empty Queue: {q}")