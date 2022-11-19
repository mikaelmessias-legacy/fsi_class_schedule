class Teacher:
  def __init__(self, id: int, name: str):
    self.id = id
    self.name = name

  def print(self):
    print(
        "Teacher: ", self.id, " - ", self.name, "\n"
    )
