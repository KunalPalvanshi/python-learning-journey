# Ek dictionary banao apni details ke saath:
# python
#    person = {"name": "Kunal", "age": 22, "city": "Meerut"}

# Print karo:

# Poori dictionary
# Sirf "name" ki value (key se access karke)
# Sirf "age" ki value



# person = {"name": "Kunal", "age": 22, "city": "Meerut"}

# print(person["name"])
# print(person["age"])
# print(person)




# Chalo Question 2:

# Q2. Same person dictionary mein:

# .get() method use karke "city" ki value nikalo
# Ek nayi key-value pair add karo: "country": "India"
# "age" ki value ko 23 mein update karo
# Final dictionary print karo


person = {"name": "Kunal", "age": 22, "city": "Meerut"}


print(person.get("city"))
person.update({"country":"India"})
person.update({"age":"23"})
print(person)


# 3. man dictionary se:

# .keys() use karke saari keys print karo
# .values() use karke saari values print karo
# .items() use karke saare key-value pairs print karo



man = {"name": "Kunal", "age": 22, "city": "Meerut"}

print(man.keys())
print(man.values())
print(man.items())




# Q4. Dictionary se ek key delete karo:

# python
# person = {"name": "Kunal", "age": 22, "city": "Meerut"}
# del keyword use karke "city" hatao
# Ya .pop() method use karke "age" hatao
# Final dictionary print karo

nonu = {"name": "Kunal", "age": 22, "city": "Meerut"}

# del nonu["city"]
nonu.pop("age")

print(nonu)




# Badhiya bhai 👍 Chalo Question 5:

# Q5. in keyword use karke check karo ki "name" key dictionary mein hai ya nahi:

# python
# person = {"name": "Kunal", "age": 22}
# Check karo "name" dictionary mein hai (True/False)
# Check karo "salary" dictionary mein hai (True/False)

# Hint: Yaad hai Chapter 3 mein "fun" in sentence try kiya tha? Dictionary mein in keyword keys ko check karta hai by default (values ko nahi).



lolu = {"name": "Kunal", "age": 22}

check_name = "name" in lolu
check_name2 = "salary" in lolu
print(check_name)
print(check_name2)


# Q6. Sets try karo:

# python
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# s1 print karo
# Ek duplicate value add karke dekho (s1.add(2)) — kya hota hai, list se kya farak hai
# Union nikalo (s1 | s2 ya s1.union(s2))
# Intersection nikalo (s1 & s2 ya 


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(2)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1)




# Q7. Ek dictionary banao jisme 3 students ke naam (key) aur unke marks (value) ho:

# python
# marks = {"Rahul": 85, "Avi": 92, "Amit": 78}
# Sabse zyada marks wale student ka naam print karo (hint: max(marks, key=marks.get))
# Average marks calculate karke print karo (hint: sabhi values ka sum le kar total students se divide karo — sum(marks.values()) / len(marks))


marks = {"Rahul": 85, "Avi": 92, "Amit": 78}
print(max(marks, key=marks.get))

average_marks = sum(marks.values()) / len(marks)

print("Average marks of students are: ",average_marks)
