# Ek list fruits = ["apple", "banana", "mango", "grapes"] banao aur print karo:
# Poori list
# Pehla element
# Aakhri element (negative indexing se)
# List ki length (len())



fruits = ["apple", "banana", "mango", "grapes"]

print(fruits)
print(fruits[0])
print(fruits[-1])
print(len(fruits))




# Q2. numbers = [10, 20, 30, 40, 50] list lo:

# .append() use karke usme 60 add karo (end mein add hota hai)
# .remove() use karke 20 hatao (value ke basis pe hatata hai)
# .insert() use karke index 1 pe 15 daalo (specific position pe daalta hai)
# Final list print karo

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.remove(20)
numbers.insert(1,15)

print(numbers)



# Q3. List slicing try karo — nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:

# Pehle 3 elements print karo
# Last 3 elements print karo
# Poori list reverse karke print karo ([::-1])



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[0:3])
print(nums[-3::])
nums.reverse()
print(nums)



# Q4. numbers = [5, 3, 8, 1, 9, 2] lo:

# .sort() use karke ascending order mein sort karo
# Fir usi list ko descending order mein sort karo (reverse=True)
# max() aur min() se sabse bada aur chota number nikalo


numbers = [5, 3, 8, 1, 9, 2]
numbers.sort(reverse=True)

print(max(numbers))

print(min(numbers))



# Q5. Ek tuple banao t = (1, 2, 3), fir try karo usme koi value change karne ki (jaise t[0] = 10) aur dekho kya hota hai. Jo error aaye uska message yahan paste karna.


# t = (1, 2, 3)

# t[0] = 10




# Q7. Ek list mixed = [1, "hello", 3.5, True, "world"] banao (dekh — list mein alag-alag datatypes ek saath rakh sakte ho, ye list ki khaasiyat hai). Print karo:





# Poori list



# List ki length



# Check karo "hello" list mein hai ya nahi (in keyword se — yaad hai Chapter 3 mein seekha tha)




mixed = [1, "hello", 3.5, True, "world"]

print(mixed)
print(len(mixed))

print("hello" in mixed)