#!/usr/bin/env python2.7

from Student import Student


class School(object):
	def __init__(self,name):
		self.name = name
		self.student_list = []
		self.courses = []

	def register_student(self, student):
		self.student_list.append(student)
		print "added " + str(student)
	
	def get_student(self, name, surname):
		return next(student for student in self.student_list if student.name == name and student.surname == surname)

	def print_all_grades(self):
		for student in self.student_list:
			for course in student.courses:
				print "%s's grades in %s: %s; average = %.2f" %(student.name ,course, student.courses[course], student.get_course_average(course))

	def add_course(self,name):
		if name in self.courses:
			print "Such course already exists"
		else:
			self.courses.append(name)

	def add_grade(self, grade, student, course):
		if course not in student.courses:
			self.assign_course(student,course)
		student.courses[course].append(grade)
		print "%.1f added to %s's record in %s" % (grade, student.name, course)

	def assign_course(self,student,course):
		if course in self.courses and course not in student.courses.keys():
			student.courses[course] = []
			print "assigned %s to %s" %(course, student.name)

	def load_from_file(self,filename):
		file = open(filename, 'r')
		name,surname = file.readline().rstrip().split(",")
		try:
			mystudent = next(student for student in self.student_list if student.name == name if student.surname == surname)
		except StopIteration:  #trzeba stworzyc nowego studenta
			mystudent = Student(name, surname)
			self.register_student(mystudent)

		for line in file:
			course, grades = line.split(': ')
			grades = grades.rstrip().split(", ")
			grades = map(float, grades)
			for grade in grades:
				self.add_grade(grade, mystudent, course)



