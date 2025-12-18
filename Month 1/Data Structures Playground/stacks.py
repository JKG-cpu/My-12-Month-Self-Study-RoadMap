history = []

# User Goes to Home Page
history.append("https://google.com")
print(history)

# User Goes to Github
history.append("https://github.com")
print(history)

# User Goes to My Repo
history.append("https://github.com/JKG-cpu/My-12-Month-Self-Study-RoadMap")
print(history)

# User Goes back
history.pop()
print(history)

# User Goes Back to Home
history.append("https://google.com")
print(history)

# Goes all the way back
history.pop()
history.pop()
history.pop()

print(history)