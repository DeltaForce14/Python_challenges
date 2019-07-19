'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year
that they will turn 100 years old.
Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
'''


name = input("What's your name?")
             
age = input("How old are you?")

def hunderd_age():
    return 100 - int(age) 


age_sentence = name +", you will be 100 years old in " + str(hunderd_age()) + " years."
print(age_sentence)
            

def number_check():
    try:
        global user_number
        user_number = int(input("Give me a number from 1 to 10: "))
    except ValueError:
        print("You need to type a whole number. This is not a whole number.")
    else:
        
        if (user_number > 0) and (user_number <=10):
            print("You typed:", user_number)
        else:
            print("This is not a number between 1 and 10. Try it again.")
        
print(number_check())     


for i in range(user_number):
    print(str(age_sentence * i))


