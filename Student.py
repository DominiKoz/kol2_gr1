class Student(object):
	def __init__(self,name,surname):
		self.name = name
		self.surname = surname
		self.id = -1
		self.grades = {}
		self.courses = []


	def print_info(self):
		print "Student %s %s, ID: %d " %(self.name, self.surname, self.id)

	def assigned_courses(self):
		print "%s is assigned to %s" %(self.name, self.courses)

	def print_course_grades(self, course):
		print "%s's grades earned in %s: %s" %(self.name, course,  str(self.grades[course]).strip('[]'))

	def print_average(self,course):
		print "%s's average in %s is: %.1f" %(self.name, course, self.get_average(course))

	def print_grades_info(self):
		for course in self.courses:
			self.print_course_grades(course)
			self.print_average(course)

		print "%s's total average is: %.1f" %(self.name, self.get_overall_average())


	def get_average(self,course):
		sum = 0
		counter = 0
		for grade in self.grades[course]:
			counter += 1
			sum += grade

		return sum/counter

	def get_overall_average(self):
		counter = len(self.courses)
		sum = 0
		for course in self.courses:
			sum += self.get_average(course)

		return sum/counter