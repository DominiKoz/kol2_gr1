class Student(object):
	def __init__(self,name,surname):
		self.name = name
		self.surname = surname
		self.courses = {}

	def __str__(self):
		return self.name + " " + self.surname

	def assigned_courses(self):
		print "%s is assigned to %s" %(self.name, self.courses.keys())

	def get_course_average(self,course):
		total = sum(self.courses[course])
		counter = len(self.courses[course])
		return total/counter


	def save_to_file(self,filename):
		file = open(filename, 'w')
		file.write(str(self) + "\n")
		for course, grades in self.courses.iteritems():
			file.write(course + ": " + str(grades)[1:-1] + "\n")
		file.close()






