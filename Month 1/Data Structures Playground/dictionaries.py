inventory = {}

print(inventory)

# Add Wood
inventory["Wood"] = inventory.get("Wood", 0) + 1
print(inventory)

inventory["Stone"] = inventory.get("Stone", 0) + 1
print(inventory)

inventory["Stone"] = inventory.get("Stone", 0) + 1
print(inventory)

inventory["Stone"] -= 1
print(inventory)
