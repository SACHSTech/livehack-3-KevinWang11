"""
-------------------------------------------------------------------------------
Name:   filename.py
Purpose:  a description of your program
 
Author: lastname.First Initial
 
Created:  date in dd/mm/yyyy
------------------------------------------------------------------------------
"""
print("***** Welcome to the DoorDash Distance Tracker *****")
print("")
distance = 0
count = 0

while distance < 100:
  distance_traveled = int(input("Enter the distance travelled for the day: "))  
  distance = distance + distance_traveled
  count += 1
    
average = distance/count

print ("It took", count, "days to surpass 100km driven.")
print("The average distance driven per day is",int(average), "km")

