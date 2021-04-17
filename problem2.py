"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Write a program that allows Tony to enter the distance driven for each day until the total distance driven surpasses 100km. 
 
Author: Wang.K
 
Created:  date in 03/03/2021
------------------------------------------------------------------------------
"""
#Title page for the code
print("***** Welcome to the DoorDash Distance Tracker *****")
print("")

#Estabishes that distance is currently zero, and number of days is currently 0.
distance = 0
days = 0

#keeps looping until distance is larger than 100
while distance <= 100:
  distance_traveled = int(input("Enter the distance travelled for the day: "))  
  distance = distance + distance_traveled
  days += 1

#Calculates average    
average = distance/days

#Prints the following statements.
print ("It took", days, "days to surpass 100km driven.")
print("The average distance driven per day is",int(average), "km")

