print("\nhello")
print("welcome to this password guess game")

Name = str(input("please type your name: "))

print("ok "+Name+" Instructions first")
input("press enter\n")
print("INSTRUCTIONS:\n" \
"1. you just have to guess the password using your skills.\n" \
"2. you will get +5 for correct answer.\n" \
"3. no negative marking for worng answer\n" \
"4. there is 10 questions from difficulty level 1-10")
input("press enter to rock 'n roll\n")

score = 0

password1 = "Albert1Einstein"
password2 = "JhonDoe33"
password3 = "6DonBradman7"
password4 = "ThomasA.99Edison"
password5 = "Arnab6Pal4"
password6 = "8Allen5Walker6"
password7 = "Alfred8Wegnar"
password8 = "8Oscar5Wilde4"
password9 = "Mary4Lamb06"
password10 = "87Alfred2Noyes"

print("Q 1. Name = Albert Einstein\n" \
"Favourite number = 1\n")
guess1 = str(input("expected password : "))#q1

if guess1 == password1:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 2. Name = Jhon Doe\n" \
"Favourite number = 33\n")
guess2 = str(input("expected password : "))#q2

if guess2 == password2:
    score = score + 5
    print("Correct password ✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 3. Name = Don Bradman\n" \
"Favourite number = 67\n")
guess3 = str(input("expected password : "))#q3

if guess3 == password3:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 4. Name = Thomas A. Edison\n" \
"Favourite number = 99\n")
guess4 = str(input("expected password : "))#q4

if guess4 == password4:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 5. Name = Arnab Pal\n" \
"Favourite number = 64\n")
guess5 = str(input("expected password : "))#q5

if guess5 == password5:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 6. Name = Allen Walker\n" \
"Favourite number = 856\n")
guess6 = str(input("expected password : "))#q6

if guess6 == password6:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 7. Name = Alfred Wegnar\n" \
"Favourite number = 84\n")
guess7 = str(input("expected password : "))#q7

if guess7 == password7:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 8. Name = Oscar Wilde\n" \
"Favourite number = 854\n")
guess8 = str(input("expected password : "))#q8

if guess8 == password8:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 9. Name = Mary Lamb\n" \
"Favourite number = 406\n")
guess9 = str(input("expected password : "))#q9

if guess9 == password9:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    

print("Q 10. Name = Alfred Noyes\n" \
"Favourite number = 872\n")
guess10 = str(input("expected password : "))#q10

if guess10 == password10:
    score = score + 5
    print("Correct password✅\n")
else:
    print("wrong password❌\n")
input()    
print("questions compleated press enter to get result\n")
input("\n")
print("RESULT:\n" \
"you got " + str(score) + " out of 50")
print("type a to get answers and e to exit")
dec = str(input())
if dec == "a":
    print("Answers are " \
    " 1. "+password1+""
    " 2. "+password2+""
    " 3. "+password3+""
    " 4. "+password4+
    " 5. "+password5+""
    " 6. "+password6+""
    " 7. "+password7+""
    " 8. "+password8+""
    " 9. "+password9+
    " 10. "+password10)
else:
    print("Thanks for using my tool ")
    input()