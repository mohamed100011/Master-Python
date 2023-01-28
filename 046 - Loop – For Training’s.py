# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

myRange = range(1, 101)

for number in myRange:

  print(number)

# Dictionary

mySkills = {
  "Html": "90%",
  "Css": "60%",
  "PHP": "70%",
  "JS": "80%",
  "Python": "90%",
  "MySQL": "60%"
}

print(mySkills['JS'])
print(mySkills.get("Python"))

for skill in mySkills:

  # print(skill)

  print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}")