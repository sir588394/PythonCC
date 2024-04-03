"""
File: ClassConcept.py
Name: Sidney Beeler
Date: 2022-02-23

Description: Explains the concept of classes in Python
"""

# Define a classes with default, non-parameterized,
# parameterized and parameterized with default values constructors

# default constructor
class Employee:

    def show(self):
        print("Default Constructor")

# non-parameterized constructor
class Company:

    def __init__(self):
        self.name = "ABC"
        self.address = "XYZ"

    def show(self):
        print("Name:", self.name, "Address:", self.address)

# parameterized constructor
class Person:
    '''Class Person with instance variables name, sex, and profession and methods show and work_as'''
    # instance variables
    # parameterized constructor
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession
    # instance method
    def show(self):
        print("Name:", self.name, "Sex:", self.sex, "Profession:", self.profession)

    def work_as(self):
        print(self.name, "is working as a", self.profession)

# parameterized constructor with default values
class Student:

    def __init__(self, name="John Doe", age=16, classroom=1):
        self.name = name
        self.age = age
        self.classroom = classroom

    def show(self):
        print("Name:", self.name, "Age:", self.age, "Marks:", self.classroom)

# https://pynative.com/python-classes-and-objects/
