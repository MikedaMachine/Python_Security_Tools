# Program Name: Lab 5.py
# Course: IT1113/Section W01
# Student Name: Michael Simmons
# Assignment Number: Lab# 5
# Purpose: The Marietta Country Club has asked you to write a program to gather, then display the results of the golf \
# tournament played at the end of March.  The Club president Mr. Martin has asked you to write two programs.
# The second program will read the records from the golf.txt file and display them with appropriate headings above the \
# data being displayed.

# Defining the main function of the second program
def main():
    golfFile = open("golf.txt", "r")
    print("First Name" + "\t\t" + "LastName" + "\t\t" + "Handicap" + "\t\t" + "GolfScore")
    playerFirstName = golfFile.readline().rstrip("\n")
# Reading and processing the records
    while playerFirstName != '':
        playerLastName = golfFile.readline().rstrip("\n")
        playerHandicap = golfFile.readline().rstrip("\n")
        playerScore = golfFile.readline().rstrip("\n")
        print(playerFirstName, "\t\t\t" + playerLastName, "\t\t\t" + playerHandicap, "\t\t\t" + playerScore)
        playerFirstName = golfFile.readline().rstrip("\n")
    golfFile.close()
# Determine Par
def determine_par(score):
    if (score == 80):
        return "Made Par"
    elif (score>= 80):
        return "Over Par"
    else:
        return "Under Par"
def results(score):
    print(str(determine_par(score)))
# Calling the main function
main()
