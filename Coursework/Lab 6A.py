# Program Name: Lab 6.py
# Course: IT1113/Section W01
# Student Name: Michael Simmons
# Assignment Number: Lab# 6
# Purpose: Write a program that allows the user to enter the total rainfall for each  of 12 months into a list. \
# The program should calculate and display the total rainfall for the year, the average monthly rainfall, and the \
# months with the highest and lowest rainfall amounts.


def rainfallMonths(namedMonths):
    Months_In_Year = 12
    rainfallList = []

    for monthsIndex in range(Months_In_Year):
        monthlyRainfall = float(input("Please enter the rainfall amount for" +"\t"+ namedMonths[monthsIndex]))
        rainfallList.append(monthlyRainfall)
    return rainfallList

def lowestRainfall(namedMonths):
    print('The lowest rainfall month is', min(rainfallMonths(namedMonths)))

def highestRainfall(namedMonths):
    print('The highest rainfall month is', max(rainfallMonths(namedMonths)))

def totalYearlyRainfall(namedMonths):
    print('The total rainfall for the year is', sum(rainfallMonths(namedMonths)))

def averageMonthlyRainfall(namedMonths):
    print('The average monthly rainfall is', float(sum(rainfallMonths(namedMonths))))

def main():
    namedMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    rainfallMonths(namedMonths)
    lowestRainfall(namedMonths)
    highestRainfall(namedMonths)
    totalYearlyRainfall(namedMonths)
    averageMonthlyRainfall(namedMonths)

main()








