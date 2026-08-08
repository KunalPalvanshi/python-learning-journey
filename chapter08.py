# Ek simple function banao greet() jo "Hello, welcome to Python!" print kare. Function define karo aur fir usko call karo.


def greet():
    print("Hello, welcome to Python!")

greet()



# Q2. Ek function banao add(a, b) jo do numbers le (parameters) aur unka sum return kare (print nahi, return use karna hai). Fir usko call karke result ek variable mein store karo aur print karo.



# def add(a, b):
#     return a + b

# a = int(input("Enter a Number: "))
# b = int(input("Enter a Number: "))

# result = add(a, b)
# print(result)



def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = 4
result = is_even(n)     # function ko CALL kiya, n pass karke
print(result)   




# Badhiya bhai 👍 Chalo Question 4:

# Q4. Default parameter try karo — ek function banao greet_name(name="Guest") jisme agar naam na diya jaye toh "Guest" use ho, aur agar diya jaye toh wahi use ho.

# Hint:




def greet(name ="guest"):
    print("HELLO",name)
greet()
greet("kunal")



# Q5. Ek function banao calculator jisme teen cheezein pass ho — do numbers aur ek operation (jaise "add", "subtract", "multiply", "divide"). Function if-elif use karke check kare kaunsa operation hai, aur uska result return kare.

# Hint (concept ke liye, poora code nahi):

# def calculator(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         # yahan khud likh
#     # aage khud continue kar sabhi operations ke liye


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "substraction":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
       return  a / b
    
calresult = calculator(2, 4, "multiply")

print(calresult)



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1 )
res_factorial = factorial(5)
print(res_factorial)



# Ek function banao is_prime(num) jo check kare number prime hai ya nahi (True/False return kare).

# Prime number ka matlab: Wo number jo sirf 1 aur khud se hi divide hota hai, kisi aur number se nahi.



def is_prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

chl_rslt = is_prime(6)
print(chl_rslt)