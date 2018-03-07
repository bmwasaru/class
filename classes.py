class Person:
	"""This is a person class"""

	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def say_hello(self):
		print("Hello there")

	def my_name(self):
		print("My name is ", self.name)


britone = Person("Mwakiacha", 70)
britone.my_name()
