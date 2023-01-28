# # ---------------------
# # -- Strings Methods --
# # ---------------------

# # replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# # join(Iterable)

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

