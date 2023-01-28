# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuple = ("Html", "CSS", "JS")

mySkills = {
  'Go': "80%",
  'Python': "50%",
  'MySQL': "80%"
}

def show_skills(name, *skills, **skillsWithProgres):

  print(f"Hello {name} \nSkills Without Progress Is: ")

  for skill in skills:

    print(f"- {skill}")

  print("Skills With Progress Is: ")

  for skill_key, skill_value in skillsWithProgres.items():

    print(f"- {skill_key} => {skill_value}")

show_skills("Osama", *myTuple, **mySkills)