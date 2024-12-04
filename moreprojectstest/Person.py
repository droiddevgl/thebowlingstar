class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.title = name

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getStatus(self):
        return f'Name: {self.name}\nAge: {self.age}\nTitle: {self.title}'
