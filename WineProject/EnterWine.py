import csv

'''This program solves a minor problem: My wife and I can never remember the wines we try.
It takes user input and stores it in a CSV. The user has the choice to enter however many wines they want. 
A wine identifier is created for later use as an object name'''
x = int(input("How many wines would you like to enter at this time?"))

y  = -1
#Iterating through file to determine number of wines
with open("wine.csv", "r") as fcount:
    for row in fcount:
        y+= 1


with open('wine.csv', 'a+') as f:#Open file in append plus mode 
    
    w = csv.writer(f, quoting=csv.QUOTE_ALL) 
    for i in range(1, x+1):#Enter the number of wines according to human counting methods
        Name = input("Name: ")
        Country = input("Country ")
        Year = input("Year: ")
        Grape = input("Grape: ")
        Price = input("Price: ")
        Enjoyed = input("Home, Restaurant name, Other: ")
        Number = "wine" + "." + str(y) #Create backend wine identifer number
        w.writerow([Name, Country, Year, Grape, Price, Enjoyed, Number])