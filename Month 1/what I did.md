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
```
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
## Infomation for today
Time Spent: ~30-40 minutes

Sources Used: Internet, some docs

Mostly just reviewed some of what I know about Data Structures

</div>