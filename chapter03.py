# Practice Set — Chapter 3: Strings

# Ek string s = "Python Programming" lo aur print karo:
# Uski length (len())
# Pehla character
# Aakhri character

s = "Python Programming"

print(len(s))
print(s[0:1])
print(s[17:18])




# String Indexing: s = "CodeWithHarry" lo aur print karo:
# Index 0 se 3 tak ka part (slicing)
# Sirf last 5 characters (negative indexing use karke)
# Poori string ulti (reverse) — hint: [::-1]



s = "CodeWithHarry"

print(s[0:3])
print(s[-5::])
print(s[::-1])




# Q3. name = "kunal palvanshi" lo aur print karo:

# Poora uppercase mein (.upper())
# Poora lowercase mein (.lower())
# Har word ka pehla letter capital (.title())


name = "kunal palvanshi"
upper_name = name.upper()
lower_name = name.lower()
capital_name = name.title()

print(upper_name)
print(lower_name)
print(capital_name)




# Q4. Ek string mein extra spaces ho:

# python
# text = "   Hello World   "

# Isko dono taraf se (start aur end se) spaces hatakar .strip() use karke print karo.

# Tip: pehle bina strip kiye print karke dekh spaces kaise dikhte hain, fir .strip() lagake compare kar — difference clearly samajh aayega.



text = "   Hello World   "

strip_text = text.strip()

print(strip_text)
print(text)



# Q5. sentence = "I love Python programming" lo:

# .replace() use karke "Python" ko "Java" se replace karo
# .split() use karke sentence ko words ki list mein todo (default space se split hota hai)



sentence =  "I love Python programming"

new_sentence = sentence.replace("Python", "Java")
split_sentence = sentence.split()

print(new_sentence)
print(split_sentence)


# Q6. Do strings a = "Hello" aur b = "World" lo, unko concatenate (jodo) karke "Hello World" print karo (+ operator se, beech mein space daal ke).

# Hint: + se do strings seedhe jud jaate hain, lekin beech mein space nahi aata apne aap — us space ko manually add karna padta hai (" " ek separate string ki tarah).



a = "Hello"
b = "World"
c = " "

print(a + c + b)





# Q7. in keyword use karke check karo ki ek word kisi sentence mein hai ya nahi:

# python
# sentence = "Python is fun"
# # check karo "fun" is sentence mein hai ya nahi (True/False output)

# Hint: in keyword bahut simple hai — "word" in sentence likhoge toh Python khud True ya False bata dega.





sentence = "Python is fun"
check_fun = "fun" in sentence

print(check_fun)



# Q8. User se uska pura naam input lo (input() se), aur:

# Uski length print karo
# Usko uppercase mein print karo
# Check karo (in keyword se) ki uske naam mein "a" letter hai ya nahi

# Sab concepts jo abhi tak seekhe (input, len, upper, in) — sab combine karke likhna hai. Try kar 👍


ask_name = input("What IS Your Name ?")

len_ask_name = len(ask_name)
upper_askname = ask_name.upper()
a_ask_name = "a" in ask_name

print("Your name length is: ",len_ask_name )
print(upper_askname)
print(a_ask_name)