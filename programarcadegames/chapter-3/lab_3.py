# Variable declaration
score = 0

# Print the quiz message
print("Quiz time!")
print()

# Quiz 1
answer = int(input("How many seasons are there in Mr. Robot? "))
if answer == 4:
    score += 1
    print("Correct!")
else:
    print("No.")
print()

# Quiz 2
answer = int(input("What is 2+2=4-1? "))
if answer == 3:
    score += 1
    print("Correct!")
else:
    print("No.")
print()

# Quiz 3
answer = int(input("What is 1+1? "))
if answer == 2:
    score += 1
    print("Correct!")
else:
    print("No.")
print()

# Quiz 4
print("Which of the following cars uses a rotary engine")
print("1. Toyota Supra")
print("2. Honda NSX")
print("3. Mazda RX-7")
print("4. Nissan Skyline GT-R")
answer = int(input("? "))
if answer == 3:
    score += 1
    print("Correct!")
else:
    print("No.")
print()

# Quiz 5
print("Which band sang Bohemian Rhapsody")
print("1. Queen")
print("2. Bon Jovi")
print("3. Led Zeppelin")
print("4. Metallica")
answer = int(input("? "))
if answer == 1:
    score += 1
    print("Correct!")
else:
    print("No.")
print()
print("Congratulations, you got {} answers right.".format(score))
print("That is a score of {} percent.".format((score*100/5)))
