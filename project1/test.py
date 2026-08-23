from math import *

# * This is a simple program to demonstrate string manipulation and user input in Python.
before = input("enter the word:")
print(f"After:{before.upper()}")  # * تحويل الحروف إلى حروف كبيرة
print(f"After:{before.lower()}")  # * تحويل الحروف إلي حروف صغيرة
print(f"After:{before.capitalize()}")  # * تحويل الحرف الأول إلى حرف كبير
print(f"After:{before.title()}")  # * تحويل الحرف الأول من كل كلمة إلى حرف كبير
print(f"After:{before.split()}")  # * تقسيم النص إلى قائمة من الكلمات
print(f"After:{before.replace("", "")}")  # * استبدال كلمة معينة بكلمة أخرى
print(f"index:{before.index("h")}")  # * العثور على موقع حرف معين في النص
print(f"Line length:{before.__len__()}")  # * حساب طول النص

# ?The program demonstrates the use built-in functions in Python for mathematical operations.
x = 10.4
print("x =", x, ", type =", type(x))  # ? طباعة المتغير ونوعه

print(round(10.4))  # ? تقريب الرقم إلى أقرب عدد صحيح
print(ceil(20.1))  # ? تقريب الرقم إلى الأعلى
print(pow(2, 3))  # ? رفع العدد إلى قوة معينة
print(abs(-5))  # ? (الايجابيه)الحصول على القيمة المطلقة
print(max(9, 5, 3))  # ? الحصول على أكبر قيمة
print(min(3, 5, 7))  # ? الحصول على أصغر قيمة

name = input("what is your name: ")  # ? الحصول على اسم المستخدم من خلال الإدخال
while True:  # ? حلقة لا نهائية حتى يتم إدخال رقم صحيح
  try:
    age = int(input("Enter a number: "))
    break
  except:
    pass
print(name + " " + str(age))  # ?طباعة الاسم والعمر معًا

# ! The program demonstrates list manipulation, and dictionary handling in Python.
lists = ["ahmed", "mohammed", "ali", [1, 2, 3, [4, [7, 8, [9, 10]], 6]]]
print(lists[3][3][1][2][1])  #! الوصول إلى العنصر 10 داخل القائمة المتداخلة
lists.append("sofy")  #!اضافة عنصر في نهاية القائمة
lists.insert(1, "samy")  #! اضافة عنصر في موقع معين
print(lists)

x = [4, 2, 1, 3]
y = [5, 6, 7, 8]
x.sort(reverse=True)  #! ترتيب العناصر من الأكبر إلى الأصغر
x.sort()  #! ترتيب العناصر من الأصغر إلى الأكبر
y.remove(8)  #! حذف عنصر معين
# x.clear()#! حذف كل العناصر
x.extend(y)  #! دمج القائمتين
print(x)

days = (
  "sat",
  "sun",
  "mon",
  "tue",
)  #! tuple لا يمكن تعديلها
print(days[0])

info = {"name": "menna", "age": 24, "city": "cairo"}
print(info)  #! طباعةالقاموس بالكامل
print(info.get("grade"))  #! بدلاً من رفع خطأ None اذا لم يكن المفتاح موجودًا، سترجع

# TODO search for a person's phone number in a dictionary based on user input.
people = {
  "ahmed": "0100000000",
  "omar": "0123456789",
  "rana": "0987654321",
  "amr": "0111111111",
}
name = input("enter the name: ")
if name in people:
    print(f"Name: {name}, Phone: {people[name]}")  
else:
    print("name not found")

# TODO search for a person's information in a list of dictionaries based on user input.
people = [
  {
    "name": "ahmed",
    "age": 21,
    "city": "cairo",
    "phone": "0100000000",
  },
  {"name": "mohammed", "age": 22, "city": "alex", "phone": "0123456789"},
  {"name": "ali", "age": 20, "city": "giza", "phone": "0987654321"},
]
name = input("enter the name: ")
for person in people:  # البحث في القائمة من خلال كل قاموس داخلها
  if person["name"] == name:
    print(
      f"Name: {person['name']}, Age: {person['age']},City: {person['city']}, Phone: {person['phone']}"
    )
    break
else:
    print("name not found")


# * The program demonstrates how to use sets in Python.
mySet = {"ahmed", "mohammed", "hasan"}
mySet.add("ali")  # * اضافة عنصر جديد إلى المجموعة
print(mySet)  # * طباعة المجموعة

x = {1, 2, 3, 4}
y = {4, 5, 6}
print((x | y))  # * union(y)دمج مجموعتين
print(x.intersection(y))  # * العناصر المشتركة بين المجموعتين
x.remove(4)  # * حذف عنصر معين
y.discard(7)  # * حذف عنصر معين بدون رفع خطأ إذا لم يكن موجودًا
print(x)


# ? The program demonstrates how to define and call functions in Python.
def greet():  # ?user-defined function.
  print("hello world")
greet()


def hello(name):  # ?function with parameter.
  print("hello " + name)
hello(input("what's your name : "))

num1 = float(input("what's your number1: "))
num2 = float(input("what's your number2: "))


def sam(num1, num2):  # ?function with return value.
  return num1 + num2
print(sam(num1, num2))

def calcdays(age):  # ?function with return value.
  return "your age is: " + str(age * 365) + " days"

# print(calcdays(25))
print(calcdays(int(input("what,s your age: "))))

#! The program demonstrates how to use Conditional sentences in Python.
egyption = input("are you egyption?: ").lower()
if egyption in ["yes", "y"]:
  print("i am egyptian")
elif egyption in ["no", "n"]:
  print("i am not egyptian")
else:
  print("inter yes or no")

password = input("inter your pass: ")
if len(password) >= 8:
  print("welcome")
elif len(password) < 8:
  print("week")
else:
  print("inter your pass")

email = input("inter your email: ")
password = int(input("inter your pass: "))
if email == "m@gmail.com" and password == 1234:
  print("welcome")
elif email != "m@gmail.com" and password == 1234:
  print("the email is not correct")
elif email == "m@gmail.com" and password != 1234:
  print("the password is not correct")
else:
  print("the email and password are not correct")


degree = int(input("what's your degree: "))
if degree >= 90:
  print("excellent")
elif degree >= 80:
  print("very good")
elif degree >= 65:
  print("good")
elif degree >= 50:
  print("acceptable")
else:
  print("weak")


x = int(input("what's your x: "))
y = int(input("what's your y: "))
if x > y:
  print("x is greater than y")
elif x < y:
  print("x is less than y")
else:
  print("x is equal to y")


s = input("s: ")
t = input("t: ")
if s == t:
  print("same")
else:
  print("different")

age = int(input("what's your age: "))
height = int(input("what's your height: "))
if age <= 17 and height <= 160:
  print("no")
elif age <= 50 and height <= 250:
  print("yes")
else:
  print("No can't enter")

num1 = float(input("what's your number1: "))
opreator = input()
num2 = float(input("what's your number2: "))
if opreator == "+":
  print(num1 + num2)
elif opreator == "-":
  print(num1 - num2)
elif opreator == "*":
  print(num1 * num2)
elif opreator == "/":
  print(num1 / num2)
else:
  print("Error")


num = float(input("inter your num: "))
if num > 0:
  print("positive")
elif num < 0:
  print("negative")
else:
  print("zero")

# * The program demonstrates how to define and use classes in Python.
class Person:
  def __init__(self, name, age):
    self.name = name      #* صفة اسم الشخص
    self.age = age        #* صفة عمر الشخص

  def greet(self):
    #* طريقة تعرض تحية باسم الشخص وعمره
    print(f"مرحباً! اسمي {self.name} وعمري {self.age} سنة.")

#* إنشاء مثيل (كائن) من الفئة
person1 = Person("عمرو", 25)
person1.greet()  

person2 = Person("سارة", 30)
person2.greet()  

class Point:
  def __init__(self, x, y):
    #* تهيئة إحداثيات النقطة
    self.x = x
    self.y = y

  def display(self):
    print(f"النقطة عند ({self.x}, {self.y})")

p = Point(3, 4)
p.display()#

class Circle:
  pi = 3.14              #* صفة صفية مشتركة (ثابت ثابت لجميع الدوائر)

  def __init__(self, radius):
    self.radius = radius  #* صفة مثيل: نصف قطر كل دائرة

  def area(self):
    #* طريقة تحسب مساحة الدائرة
    return Circle.pi * self.radius ** 2

c = Circle(5)
print(c.area()) # طباعة مساحة الدائرة ذات نصف قطر 5
