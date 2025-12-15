name = input ('What is your name?')
print (f"Hello {name} and welcome to Ct8")
print ("Today we will do a fun little quiz about sports")
basketball_points = 0
soccer_points = 0
baseball_points = 0

answer1 = input ("Do you prefer A long sleeve, B short sleeve, or C tank tops")
if answer1 == "C":
    basketball_points += 1
elif answer1 == "B":
    soccer_points += 1
elif answer1 == "A":
    baseball_points += 1

answer2 = input ("Do you prefer A indivual work , B footwork, or C hand skills")
if answer2 == "C":
    basketball_points += 1
elif answer2 == "B":
    soccer_points += 1
elif answer2 == "A":
    baseball_points += 1

answer3 = input ("Do you prefer A no padding , B shin guards, or C knee pads")
if answer3 == "C":
    basketball_points += 1
elif answer3 == "B":
    soccer_points += 1
elif answer3 == "A":
    baseball_points += 1

answer4 = input ("Do you prefer A to play on dirt , B play on a field, or C play on a court")
if answer4 == "C":
    basketball_points += 1
elif answer4 == "B":
    soccer_points += 1
elif answer4 == "A":
    baseball_points += 1

answer5 = input ("Do you prefer A runs , B goals, or C baskets")
if answer5 == "C" or answer5 == "c":
    basketball_points += 1
elif answer5 == "B" or answer5 == "b":
    soccer_points += 1
elif answer5 == "A" or answer5 == "a":
    baseball_points += 1

if basketball_points >= soccer_points and basketball_points >= baseball_points:
    print(" you should play basketball!!")

if soccer_points >= basketball_points and soccer_points >= baseball_points:
    print(" you should play soccer!!")

if baseball_points >= soccer_points and baseball_points >= basketball_points:
    print(" you should play baseball!!")