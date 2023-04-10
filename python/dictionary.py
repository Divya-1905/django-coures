person={
    "name":"emp1",
    "age":"45"
}
# person['name'] = "emp2"
# print(person['name'])
# person['age'] = [56]
# print(person['age'])
# print(person['name'].capitalize())
# print(person['name'].replace(['value']))
for i in person.values():
    print(i)
# for i in person.values('45'):
#     print('age is: ')
for key,value in person.items():
    print(key,value,'value')    

print(person["name"].upper())
print(person["name"].capitalize())  
print(person["name"].index(1))  