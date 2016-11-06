#!/usr/bin/env python2.7

from School import School
from Student import Student

#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#dodac obecnosci, dodatkowa klase do wypisywania info o studentach uczelni


if __name__ == "__main__":
	Jan = Student("Jan", "Kowalski")
	Adam = Student("Adam", "Kowalski")
	Janusz = Student("Janusz", "Kowalski")

	AGH = School("AGH")

	AGH.add_course("Python in the enterprise")
	AGH.add_course("Java")

	print "\nAdding students..."
	AGH.register_student(Jan)
	AGH.register_student(Janusz)
	AGH.print_student_list()

	print "\nAssigning courses..."
	AGH.assign_course(Jan,"Java")
	AGH.assign_course(Jan,"Python in the enterprise")

	AGH.assign_course(Janusz,"Python in the enterprise")
	Janusz.assigned_courses()
	Jan.assigned_courses()

	print "\nAssigning grades..."
	AGH.add_grade(5.0, Jan,"Java")
	AGH.add_grade(4.0, Jan,"Java")
	AGH.add_grade(3.3, Jan,"Java")#nie zadziala
	AGH.add_grade(3.0, Jan,"Python in the enterprise")

	AGH.add_grade(3.5, Janusz,"Python in the enterprise")
	AGH.add_grade(4.5, Janusz,"Python in the enterprise")
	AGH.add_grade(3.5, Janusz,"Java")#nie zadziala



	print "\nPrinting grades..."
	Jan.print_grades_info()
	Janusz.print_grades_info()