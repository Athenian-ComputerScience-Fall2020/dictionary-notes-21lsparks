# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  
student = {'name':'John', 'age':'25', 'courses':{'math', 'compsci'}}


student['phone'] = '555=5555'
student['name'] = 'Jane'
student.update({'name': 'Jane, 'age': 26, 'phone': '555-5555'})
del student['age']
age = student.pop('age')
print(student['courses'])

print(student[1])

print(student.get('name')
print(student.get('phone', 'Not Found'))
print(student)


print(len(student)
print(student.keys())
print(student.values())
print(student.items())
for key,value in student:
    print(key)