def birthday2(name="Raymond", age = 12):
    print("Hello", name, ", I heard you are", age, "years old.")

birthday2()
birthday2("Tom", 15)
birthday2(age=13, name="Peter")

def birthday3(name, age):
    print("Hi", name, ", I heard you are", age, "years old.")
    
birthday3("Raymond", 12)


def square(number):
    number*=number
    return number

number=26
print("The square of", number, "is", square(number))

def rectangle_area(height, length):
    area=height*length
    return area

print("This is the area", rectangle_area(78, 42))

def rectangle_perimeter(height=78, length=42):
    perimeter=height*2+length*2
    return perimeter

print("This is the perimeter", rectangle_perimeter())