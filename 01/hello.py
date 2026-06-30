print("Hello")
def chai(n):
    print(n)

chai(1)
nums = [10,20,30]
nums.append(40)
nums.insert(1,50)
nums.sort()
a = [1,2]
b = [3,4]

print(a + b)
print(nums)

numbers = []
for i in range(11,15):
    numbers.append(i)

print(numbers)

numbers2 = [i for i in range(5)]
print(numbers2)

squares = [x*x for x in range (1,5)]
print(squares
      )
evens = [x for x in range(13) if x % 2 == 0]
evens2 = evens[::-2]
print(evens)
print(evens2)
Multiple_of_Four = [((4*4)+i) // (i*i) for i in range(1,3)]
print(Multiple_of_Four)

t = (10,20,30,40,50,20,20)
print(t[2])
print(t[2:5:2])
print(len(t))
print(t.count(20))
def icount(x):
    print(t.count(x))

icount(40)
icount(20)

s = {1,2,3,4,5,6,7,8,5,5,4,2,3,2,2,2}
s.remove(1)

s.discard(20)
s.add(9)
print(s)

a = {1,2,4}
b = {4,5,6}
def uni(a,b):
    print(a|b)

uni(a,b)
print(a-b)
print(a^b) #symmetric difference

student = {
    "name": "Nishant",
    "age": 19
}
print(student["name"])

print(student.get("name")
)

def age(age_value):
    print(age_value)

# age(student.get("age"))
student["city"] = "Ajmer"
student["age"]=20
del student["age"]
print(student.keys())
print(student.values())
print(student.items())
print(student)
sq_num = {(x):x*x for x in range(6)}
print(sq_num)
# print(sq_num[30])
print(sq_num.get(3))
print(sq_num.get(30))
for key, values in sq_num.items():
    print(values,"-",key)

students = {
    1:{
        "name":"Nishant",
        "age":19
    },
    2:{
        "name":"An",
        "age":18
    }
}
print(students[2]["name"])