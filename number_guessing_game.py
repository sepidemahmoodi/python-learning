import random


lower_bound = 1
upper_bound = 100
target = random.randint(lower_bound, upper_bound)

print("welcom to my first python game i mean number guessing game!")

print("so you can enter the number between {lower_bound} until {upper_bound}")
attempt = 0
max_attempt = 10

while True :
    user_guess = int(input("Enter your guess : "))
    
    attempt += 1

    if attempt > max_attempt :
        print("Your attempts is more than maximum")
        break
    
    if user_guess < target :
        print("Your guess is lower than target")

    elif user_guess > target :
        print("Your guess is upper than target")
    else :
        print("Congragulation, your geuss is correct !")
        break
