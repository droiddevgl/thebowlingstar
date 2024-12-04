#class
#inheritance
#multiple inheritance
#polymorphism
import random
from calendar import firstweekday


class Person:
    def __init__(self, fname, lname, health, status):
        """initialize attributes to be ised for all class method in this class
        and for all class objects created by this class """

        self.fname = fname
        self.lname = lname
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves"""
        print(f"Hello my name is {self.fname} {self.lname}")

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print(f"{self.fname} is happy today")
        elif emotion == 2:
            print(f"{self.fname} is sad right now")



    def status_change(self):
        if self.health == 100:
            print(f"{self.fname} is totally healthy")
        elif self.health >= 76:
            print(f"{self.fname} is a little tired today")
        elif self.health >= 51:
            print(f"{self.fname} feels unwell")
        elif self.health >= 40:
            print(f"{self.fname} goes to the doctor")
        else:
            print(f"{self.fname} is unconscious")


Maria = Person("Maria", "Cohen", 95, status=True)
Jakob = Person("Jakob", "barbados", 40, status=False)
Ray = Person("Rey", "findrus", 72, status=True)

print(f"{Maria.fname} {Maria.lname} is my friend ? {Maria.status}")
print(f"{Jakob.fname} {Jakob.lname} is my friend ? {Jakob.status}")
print(f"{Ray.fname} {Ray.lname} is my friend ? {Ray.status}")

Maria.introduce()
Jakob.introduce()
Ray.introduce()

Maria.emote()
Jakob.emote()
Ray.emote()

Maria.status_change()
Jakob.status_change()
Ray.status_change()

class Enemy(Person):
    def __init__(self, weapon, fname, lname, health, status):
        super().__init__(fname, lname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print(f"{other.fname}, you are weak")

    def steal(self, other):
        print(f"ha ha ha, {other.fname} I have your stuff")
        if other.status:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)
Alex.hurt(Maria)
Alex.insult(Jakob)
Alex.insult(Ray)
Alex.insult(Maria)
Alex.steal(Ray)
Alex.steal(Maria)
Alex.steal(Jakob)


Ray.introduce()
Alex.introduce()
