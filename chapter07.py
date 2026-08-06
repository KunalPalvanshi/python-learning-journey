for i in range(0, 10, 3):
    print(i)


# Q2. 1 se 10 tak ke saare even numbers print karo — range() mein sahi start, end, step values daal ke (bina if condition ke, seedha step wala tarika use kar).

# Soch — even numbers hote hain 2, 4, 6, 8, 10 — inka pattern kya hai? Start kahan se, gap kitna?



for i in range(0,11,2):
    print(i)






# Q3. while loop use karke 1 se 5 tak count karo.

# Hint (concept yaad kar jo pehle samjhaya tha):

# Pehle ek variable banao jo counter ka kaam karega, 1 se start karke
# while likho aur condition do — jab tak counter 5 se chota-ya-barabar rahe
# Loop ke andar counter print karo
# Sabse important: counter ko +1 badhao har round mein, warna infinite loop ban jayega

# Khud try kar likhne ka 👍



i = 1
while(i<=5):
    print(i)
    i = i+1


# Badhiya bhai 👍 Chalo Question 4:

# Q4. for loop use karke 1 se 10 tak ke numbers ka sum nikalo.

# Hint (step by step):

# Loop se pehle ek variable banao total = 0 (ye final answer store karega)
# for loop chalao 1 se 10 tak
# Loop ke andar, har number ko total mein add karte jao (total = total + i)
# Loop khatam hone ke baad (bahar), total ko print karo

total = 0

for i in range(1,11):
    total = total + i
    print(total)


# Theek hai, ab se sirf jab poochega tabhi hint dunga 👍 Chalo agla:

# Q5. Ek list fruits = ["apple", "banana", "mango", "grapes"] lo aur for loop se har fruit print karo.


fruits = ["apple", "banana", "mango", "grapes"]

for fruit in fruits:
    print(fruit)




# 1 se 10 tak loop chalao, lekin jaise hi number 5 aaye, loop ruk jaye (break use karke).

# Try kar khud, atke toh bata dena.


# Chalo Question 6 (Part B - continue):

# 1 se 10 tak loop chalao, lekin sirf even numbers print karo — continue use karke odd numbers skip karo (unko print mat karo, seedha agle number pe chale jao).

# Hint: if condition lagao — agar number odd hai (i % 2 != 0), toh continue chala do (print se pehle hi loop agle round mein chala jayega).




for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)





# Perfect bhai! 💯🔥 Bilkul sahi.

# Output:

# 2
4
6
8
10

# Ab logic bilkul clear hai — i % 2 != 0 (matlab remainder 1 hai, odd hai) toh continue chal ke skip ho gaya, aur bache sirf even numbers jo print hue. Concept solid ho gaya!

# Chalo Question 7 — Nested loop:

# Ek chhota multiplication table banao 1 se 3 tak — matlab 1 ka table, 2 ka table, 3 ka table, sab ek saath.

# Structure samajh (ye naya concept hai, dhyan se):

# python
# for i in range(1, 4):        # bahar wala loop - 1, 2, 3 (kaunsa table)
#     for j in range(1, 4):     # andar wala loop - 1, 2, 3 (kis number se multiply)
#         print(i, "x", j, "=", i*j)

# Idea ye hai: Har i (bahar wale loop se) ke liye, poora j wala loop (andar wala) pura chalta hai — matlab i=1 ke liye j=1,2,3 poora chalega, phir i=2 ke liye phir se j=1,2,3 poora chalega, aisa hi.

# Try kar likh ke ye code, run kar, aur output dekh — samjhenge phir step by step kaise chal raha hai andar se.




for i in range(1, 4):        # bahar wala loop - 1, 2, 3 (kaunsa table)
    for j in range(1, 4):     # andar wala loop - 1, 2, 3 (kis number se multiply)
        print(i, "x", j, "=", i*j)



# Chalo last question — Question 8 (Challenge):

# Ek number lo (jaise num = 5), aur uska factorial nikalo for loop use karke — bina math.factorial() use kiye, khud loop se calculate karo.

# Yaad kar: Factorial ka matlab hota hai us number tak ke saare numbers ko multiply karna:

# 5! = 5 × 4 × 3 × 2 × 1 = 120

# Thoda hint (structure ke liye, poora code nahi):

# Ek variable banao jo answer store karega, 1 se start karo (multiplication ke liye 0 se start nahi karna, warna sab kuch 0 ban jayega)
# for loop chalao 1 se num tak (ya num se 1 tak, dono chalega)
# Loop ke andar, us variable ko current number se multiply karte jao

# Try kar khud likhne ka 👍



num = 5
answer = 1

for i in range(1,6):
    answer = answer * i
    print(answer)