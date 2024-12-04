def user_info(name, age=40, city="Kfar Saba"):
    '''This is a function to print name, age, city'''

    print(f"{name} is {age} years old, from {city}")


user_info("omri", 47, "rosh haayin")
user_info("jakob", city ="tel aviv")

#*args = can take any number of arguments to be passed into function
#**kwargs = can take any number of keyword be passed into function
# for example,
def application(fname, lname, email, company, *args, **kwargs):
    print(f"{fname} {lname} works at {company}. the email is {email}")

application("Jess", "Ingress", "mail@mail.com", "TeachCode.org", 75000, hire_date = "September 2010")


fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(type(fruits))
print(type(years))
print(fruits, years)
fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)
print("asdaddddddddddddddddddddddd")
print("asdaddddddddddddddddddddddd")
print("asdaddddddddddddddddddddddd")
print("asdaddddddddddddddddddddddd")
print(fruits)
fruits.remove(3)
print(fruits)
print("asdaddddddddddddddddddddddd")
print("asdaddddddddddddddddddddddd")
print("asdaddddddddddddddddddddddd")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

fruits.sort(key=str)
print(fruits)

# dictionaries key value mutable uses curly braces
print("sadsaaaaaaaaaaaaaaa")
print("sadsaaaaaaaaaaaaaaa")
stuff = {"omri":47, "merav":44, "daniel":15, "maayan":12, "guy":8}
print(stuff.get("guy"))
print(stuff.keys())
print(stuff.pop("merav"))
print(stuff.setdefault("merav"))
print(stuff)
print("sadsaaaaaaaaaaaaaaa")
print("sadsaaaaaaaaaaaaaaa")

#print(stuff.items())

#print(stuff.popitem())
#print(stuff)

print(stuff.setdefault("omri"))
print(stuff)

print(stuff.setdefault("daniel"))
print(stuff)

new_stuff = {"fufu":34, "gigi":18}
stuff.update(new_stuff)
print(stuff)























