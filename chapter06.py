# Ek variable age = 20 lo aur if-else use karke check karo — agar age 18 ya usse zyada hai toh "You are an adult" print karo, warna "You are a minor" print karo.

age = int(input("What is your age: "))

if(age>=18):
    print("You are a Adult")
else:
    print("You are a minor")


#     Chalo Question 2:

# Q2. marks = 65 lo aur if-elif-else use karke grade decide karo:

# 90 ya usse zyada → "Grade A"
# 75 se 89 → "Grade B"
# 50 se 74 → "Grade C"
# 50 se kam → "Fail"


marks = 65

if(marks>=90):
    print("Grade A")
elif(marks>=75):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
else:
    print("Fail")



#     Q3. Ek number num = 15 lo aur check karo wo even hai ya odd hai.

# Hint: % (modulus) operator use karo — agar number ko 2 se divide karne pe remainder 0 aaye, toh even hai, warna odd hai.

# python
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


num = 15

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")



# adhiya bhai 👍 Chalo Question 4:

# Q4. Nested if-else try karo — user se ek number lo (input() se) aur check karo:

# Agar number positive hai, toh check karo wo even hai ya odd
# Agar negative hai, toh "Negative number" print karo
# Agar 0 hai, toh "Zero" print karo

# Hint: "Nested" matlab ek if ke andar doosra if likhna:

# python
# num = int(input("Enter a number: "))

# if num > 0:
#     # yahan andar ek aur if-else lagega even/odd check karne ke liye
#     if num % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

# Isi structure ko khud se likh ke try kar 👍



in_num = int(input("Give me a number: "))

if in_num > 0:

    if in_num % 2 == 0:
        print("Even Num")
    else:
        print("Positive Odd Num")

elif in_num <= 0:
    print("Negetive Number")
else:
    print("Zero")



# Q5. and, or, not operators try karo:

# python
# age = 25
# has_id = True
# Check karo (and use karke): agar age 18+ hai aur has_id True hai, toh "Entry allowed" warna "Entry denied"
# not has_id print karke dekho kya output aata hai



age = 17 
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed ")
else:
    print("Denied")
    print(not has_id)


ten_num = -6 

check_num = "Positive" if ten_num > 0 else "Negetive"
print(check_num)






# Q7. User se 3 numbers input lo, aur if-elif-else use karke sabse bada number print karo (bina max() function use kiye, khud logic lagao).

# Hint: Teen numbers ko compare karna hai ek dusre se:

# python
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("a is the largest:", a)
# elif b >= a and b >= c:
#     print("b is the largest:", b)
# else:
#     print("c is the largest:", c)

# Isi logic ko khud se likh ke try kar — teeno numbers ko pairwise compare karna hai 👍


first = int(input("First Num: "))
second = int(input("Second Num: "))
third = int(input("Third Num: "))

if first >= second >= third:
    print(first)
elif second >= third >= first:
    print(second)
else:
    print(third)


first = int(input("First Num: "))
second = int(input("Second Num: "))
third = int(input("Third Num: "))

if first >= second and first >= third:
    print(first)
elif second >= first and second >= third:
    print(second)
else:
    print(third)