import random

top_of_range=input("Type a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Please type a number larger that 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number=random.randint(0,top_of_range)
guess_count=0
while True:
    guess_count+=1
    user_guess=input("Make a guess: ")

    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess==random_number:
        print('You Got it!')
        break
    elif user_guess>random_number:
        print("You guessed little bit higher, think a smaller number :)")
        continue
    else:
        print("You guessed little bit lower, think a higher number :)")
        continue

print("You got in",guess_count,"guesses")
    



