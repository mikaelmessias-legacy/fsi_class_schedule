from typing import List
from Teacher import *


class Course:
  def __init__(self, code: str, name: str, durationPerWeek: int, requisites: List['Course'], teacher: Teacher):
    self.code = code
    self.name = name
    self.durationPerWeek = durationPerWeek
    self.requisites = requisites
    self.teacher = teacher

  def getRequisitesList(self):
    requisites = ''

    if len(self.requisites) == 0:
      return 'Nenhum'

    for index, requisite in enumerate(self.requisites):
      if index + 1 == len(self.requisites):
        requisites += requisite.code + " - " + requisite.name
      else:
        requisites += requisite.code + " - " + requisite.name + ", "

    return requisites

  def print(self):
    print(
        "Disciplina: ", self.code + " - ", self.name +
        "\nAulas por semana: ", self.durationPerWeek, "" +
        "\nPré-Requisitos: ", self.getRequisitesList(), "" +
        "\nProfessores: ", self.teacher.name +
        "\n"
    )
