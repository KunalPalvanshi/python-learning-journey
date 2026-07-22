# saving my age height name in float in different variables 
name = "Kunal"
age = 22
height = 5.6

print("my name is:",(name))
print("my age is: ",(age))
print("my height is: ",(height))




# Q2. type() function use karke ye check karo aur print karo:

# Ek integer ka type
# Ek float ka type
# Ek string ka type
# Ek boolean (True/False) ka type

a = 1 
b = 2.2 
c = "name"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))



# Q3. Do numbers a = 10 aur b = 3 le lo, aur inke saath:

# Addition, Subtraction, Multiplication print karo
# Division (/) aur Floor Division (//) dono print karo aur difference dekho
# Modulus (%) print karo

# Hint: / decimal answer deta hai, // sirf poora number (decimal hata ke) deta hai, aur % remainder deta hai.


a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)



# Q4. Ek variable x = 5 (int) lo aur usse str aur float mein convert (typecast) karke print karo. Fir wapas check karo type() se ki conversion ho gaya ya nahi.

# Hint: str(x) se string banega, float(x) se float banega — yahan float() ka sahi use hoga kyunki hum ek existing int ko convert kar rahe hain.


x = 5

print(type(x))
print(type(str(x)))
print(type(float(x)))



# Q5. Do variables a = 5 aur b = 10 lo, aur unko bina teesra variable use kiye swap karo (values aapas mein badlo), phir print karo.

# Hint: Python mein ek trick hoti hai jisse ek line mein hi swap ho jata hai — try kar dhoondhne ki.


a = 5
b = 10 

a, b = b, a

print("a:" ,(a))
print("b:" ,(b))



# Q6. Multiple assignment try karo — ek hi line mein 3 variables ko values do:

# python
# x, y, z = 1, 2, 3


x, y, z, = 1, 2, 3
print(x, y, z)


# Q7. input() function use karke user se uska naam poocho aur "Hello, <naam>!" print karo.


name = input("What is your name: ")

print("Hello!", name)



# Q8. User se do numbers input lo. Yaad rakhna — input() se jo bhi aata hai wo hamesha string hota hai, isliye use int() se convert karna padega tabhi unka sum calculate hoga. Fir dono ka sum print karo.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum of two number is: ",x + y)