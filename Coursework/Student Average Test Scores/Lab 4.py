# Program Name: Lab 4.py
# Course: IT1113/Section W01
# Student Name: Michael Simmons
# Assignment Number: Lab# 4
# Purpose: Write a program that asks the user to enter a student's name and  8 numeric tests scores (out of 100 for \
# each test).  The name will be a local variable.  The program should display a letter grade for each score, and the \
# average test score, along with the student's name.

# Define the main functions
def main():
    student_Name()
    score1, score2, score3, score4, score5, score6, score7, score8 = studentScore()
    results(score1, score2, score3, score4, score5, score6, score7, score8)
    calc_average(score1, score2, score3, score4, score5, score6, score7, score8)
# Enter a student's name
def student_Name():
    name1 = str(input("Please enter the student's name:"))
    return name1
# Enter 8 test scores
def studentScore():
    score1 = int(input("Please enter test score 1:"))
    score2 = int(input("Please enter test score 2:"))
    score3 = int(input("Please enter test score 3:"))
    score4 = int(input("Please enter test score 4:"))
    score5 = int(input("Please enter test score 5:"))
    score6 = int(input("Please enter test score 6:"))
    score7 = int(input("Please enter test score 7:"))
    score8 = int(input("Please enter test score 8:"))
    return score1, score2, score3, score4, score5, score6, score7, score8
# Calculate the average test scores
def calc_average(score1, score2, score3, score4, score5, score6, score7, score8):
    average = (score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8) / 8
    return average
# Determine the letter grade
def determine_grade(testScore):
    if (testScore >= 90):
        return "A"
    elif (testScore >= 80):
        return "B"
    elif (testScore >= 70):
        return "C"
    elif (testScore >= 60):
        return "D"
    else:
        return "F"
# Print the results after input
def results(score1, score2, score3, score4, score5, score6, score7, score8):
    print(sep="\n")
    print("Score\tLetter Grade")
    print(str(score1) + "\t\t" + determine_grade(score1),
          str(score2) + "\t\t" + determine_grade(score2),
          str(score3) + "\t\t" + determine_grade(score3),
          str(score4) + "\t\t" + determine_grade(score4),
          str(score5) + "\t\t" + determine_grade(score5),
          str(score6) + "\t\t" + determine_grade(score6),
          str(score7) + "\t\t" + determine_grade(score7),
          str(score8) + "\t\t" + determine_grade(score8), sep="\n")
    print("The test score average is:", calc_average(score1, score2, score3, score4, score5, score6, score7, score8))
# Call the main function
main()
