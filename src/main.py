from Teacher import *
from CollegeClass import *
from Course import *

if __name__ == '__main__':
  teacher_1 = Teacher(1, 'Evandro Da Silva Dos Santos')
  teacher_2 = Teacher(1, 'Carlos Frederico Charret Brandt')
  teacher_3 = Teacher(1, 'Diego Venancio Thomaz')
  teacher_4 = Teacher(1, 'Evandro Alves Nakajima')
  teacher_5 = Teacher(1, 'Davi Marcondes Rocha')

  teacher_6 = Teacher(2, 'Leiliane Pereira De Rezende')

  course_1_1 = Course("CC21C", "Fundamentos de Programação", 4, [], teacher_1)
  course_1_2 = Course(
      "CC21D", "Introdução a Ciência da Computação", 4, [], teacher_1)
  course_1_3 = Course(
      "FI221E", "Fundamentos de Eletricidade", 4, [], teacher_2)
  course_1_4 = Course(
      "MA221A", "Cálculo Diferencial e Integral 1", 4, [], teacher_3)
  course_1_5 = Course(
      "MA221B", "Geometria Analítica e Álgebra Linear", 4, [], teacher_4)
  course_1_6 = Course("MA221F", "Lógica Matemática", 4, [], teacher_5)

  course_2_1 = Course(
      "CC22C", "Linguagem de Programação Estruturada", 3, [course_1_1], teacher_6)

  class_1 = CollegeClass(
      "CC12", [course_1_1, course_1_2, course_1_3, course_1_4, course_1_5, course_1_6])
  class_2 = CollegeClass("CC21", [course_2_1])

  class_1.print()
  class_2.print()

  course_1_1.print()
  course_2_1.print()
