import random

def compareNumber():
  global low, high, number
  input_number = (low + high) // 2 
  print("My guess is", input_number)
  attempts += 1
  if input_number == number:
    print("Yes, your guess is correct")
    return True
  if input_number > number:
    print("Incorrect! Please try to guest a smaller number.")
    high = input_number - 1
  else:
    print("Incorrect! Please try to guess a larger number.")
    low = input_number + 1
  return False

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000
while True:
  print("Guess the number (between 1 and 1000): ")
  if compareNumber():
    break
print("You tried", attempts, "times to find the correct number.")
