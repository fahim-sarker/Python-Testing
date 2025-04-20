# import random

# number = random.randint(1, 1000)
# attempts = 0
# low = 1
# high = 1000
# while True:
#   print("Guess the number (between 1 and 1000): ")
#   input_number = (low + high) // 2 
#   print("My guess is", input_number)
#   attempts += 1
#   if input_number == number:
#     print("Yes, your guess is correct")
#     break
#   if input_number > number:
#     print("Incorrect! Please try to guest a smaller number.")
#     high = input_number - 1
#   else:
#     print("Incorrect! Please try to guess a larger number.")
#     low = input_number + 1
# print("You tried", attempts, "times to find the correct number.")









import random


number = random.randint(1, 1000)
attemps = 0
high = 1000
low = 1

while True :
    print("guess the number (between 1 to 1000) : ")
    input_number = (high + low) // 2
    print("my guess is ", input_number)
    attemps += 1
    if input_number == number:
        print("yes your guess is correct")
        break
    if input_number > number :
        print("please try to get small number")
        high = input_number -1
    else :
        low = input_number + 1
        print("guess a larger number")
        
        print("you tried", attemps, "you guess are correct")
        
    
