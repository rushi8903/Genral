#guessing the age
from ast import While

a=0
b=100

for i in range (1,10):
    guess_age = int((b+a)/2)
    print("are you" , guess_age , "years old?")
    ans = input()
    if ans == "correct":
        print("ok great your age is" , guess_age ,"years old.")
        break
    elif ans == "less":
        b=guess_age  
    elif ans =="more":
        a=guess_age
    else:
        print=("error")  


 






