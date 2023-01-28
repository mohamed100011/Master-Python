# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("D:\Python\Files\mohamed.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Mohamed Ibrahim\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\mohamed.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\mohamed.txt", "a")
myFile.write("Elzero")