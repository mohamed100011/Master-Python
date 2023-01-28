# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("D:\Python\Files\mohamed.txt", "a")
myFile.truncate(5)

myFile = open("D:\Python\Files\mohamed.txt", "a")
print(myFile.tell())

myFile = open("D:\Python\Files\mohamed.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("D:\Python\Files\mohamed.txt")