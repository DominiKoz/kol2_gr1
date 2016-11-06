#!/usr/bin/env python2.7

from Student import Student


class School(object):
	def __init__(self,name):
		self.name = name
		self.counter = 0 
		self.student_list = []
		self.courses = []

	def register_student(self, student):
		self.counter +=1
		student.id = self.counter
		self.student_list.append(student)
	
	def print_student_list(self):
		for i in self.student_list:
			i.print_info()

	def add_course(self,name):
		if name in self.courses:
			print "Such course already exists"
		else:
			self.courses.append(name)
	
	def  grade_validation(self,grade):
		if grade not in [2.0,3.0,3.5,4.0,4.5,5.0]:
			return False
		else:
			return True


	def add_grade(self, grade, student, course):
		if not self.grade_validation(grade):
			print "grade is invalid! Enter one of: [2.0,3.0,3.5,4.0,4.5,5.0]"
			return
		if not isinstance (student,Student):
			print "Invalid object- not a Student"
			return
		if student not in self.student_list:
			print "No such student registred in school"
			return
		if course not in self.courses:
			print "Invalid course - no such course exists in this school"
			return
		if course not in student.courses:
			print "Invalid course - student isn't assigned to this course"
			return
		student.grades[course].append(grade)
		print "%.1f added to %s's record in %s" % (grade, student.name, course)

	def assign_course(self,student,course):
		if course not in self.courses:
			print "Invalid course - no such course exists in this school"
			return
		if course in student.courses:
			print "This student is already assigned to this course"
			return
		if student not in self.student_list:
			print "No such student registred in school"
			return

		student.courses.append(course)
		student.grades[course] = []
		print "assigned %s to %s" %(course, student.name)


