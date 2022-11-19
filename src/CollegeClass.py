from Course import *


class CollegeClass:
  def __init__(self, code: str, courses: Course):
    self.code = code
    self.courses = courses

  def getCourses(self):
    courses = ''

    for index, course in enumerate(self.courses):
      if index + 1 == len(self.courses):
        courses += course.code + " - " + course.name
      else:
        courses += course.code + " - " + course.name + ", "

    return courses

  def print(self):
    print(
        "Turma: ", self.code +
        "\nDisciplinas: ", self.getCourses(), "\n"
    )
