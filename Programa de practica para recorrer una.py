# Programa de practica para recorrer una estructura
# LIST

nums =[1,3,5,7,9,11,13,15]

#Sentencia LOOP
for item in nums:
    print(item)
    
print(sum(nums))
print(min(nums))
print(max(nums))

courses=['History','Math','Physics','CompSci']
courses_2=['Art','Science']

print(len(courses))
print(courses[0])
print(courses[0:2])
print(courses[:2])
print(courses[2:0])

courses.insert(0,courses_2)
print(courses)
print(courses[0])

courses.extend(courses_2)
print(courses)

courses.append(courses_2)
print(courses)

#Remove method
courses.remove('Math')
print(courses)

courses.pop()
print(courses)

popped = courses.pop
print(courses)

courses.reverse
print(courses)

courses.sort
print(courses)

#sorted_courses = courses.sort
#print(courses.sort)

for item in courses:
    print(item)
      
#
        
for index, item in enumerate (courses):
    print(index, item)
    
for index, item in enumerate (courses,start=1):
    print(index, item)    