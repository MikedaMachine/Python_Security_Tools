# Program Name: Lab 5.py
# Course: IT1113/Section W01
# Student Name: Michael Simmons
# Assignment Number: Lab# 5
# Purpose: The Marietta Country Club has asked you to write a program to gather, then display the results of the golf \
# tournament played at the end of March.  The Club president Mr. Martin has asked you to write two programs.
#
# The first program will input each player's first name, last name, handicap and golf score  and then save \
# these records in a file named golf.txt (each record will have a field for the first name, last name, handicap \
# and golf score).


# Defining the input functions
def playerFirstName():
    firstName = input("Please enter the player's first name:")
    return firstName
def playerLastName():
    lastName = input("Please enter the player's last name:")
    return lastName
def playerHandicap():
    handicap = input("Please enter the player's handicap:")
    return handicap
def playerScore():
    score = input("Please enter the player's score:")
    return score

def determine_par(score):
    if score == 80:
        return "Made Par"
    elif score >= 80:
        return "Over Par"
    else:
        return "Under Par"

def results(score):
    print(str(score) + "\t" + determine_par(score))

# Defining the main function of the first program
def main():
    golfFile = open("golf.txt", "w")
# Adding a loop for inputting additional records
    nextFile = "y"
    while nextFile == "y" or nextFile == "yes":
        fileFirstName = playerFirstName()
        fileLastName = playerLastName()
        fileHandicap = playerHandicap()
        fileScore = playerScore()
        golfFile.write(fileFirstName + "\n" + fileLastName + "\n" + fileHandicap + "\n" + fileScore + "\n")
        nextFile = input("Add another player record?")
    golfFile.close()
    print("All records have been added to golf.txt")
# Calling the main function
main()
