"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Write a program to determine which group a player is placed in.

Author: Wang.K
 
Created:  date in 03/03/2021
------------------------------------------------------------------------------
"""
#Title for the code
print("****** Tournament Tracker ******")
print ("")

#Establishes that win count and loss count is currently zero
win_count = 0 
loss_count = 0

#Asks the user to input six different times
for i in range(6):
  result = input("Enter the wins and losses for your team (W/L): ")
  if result == 'W':
    win_count += 1
  elif result == 'L':
    loss_count += 1

#determines what group the user is put in.
if win_count == 5 or win_count == 6:
  print("You have been placed in group 1.")
elif win_count == 3 or win_count == 4:
  print("You have been placed in group 2.")
elif win_count == 1 or win_count == 2:
  print ("You have been placed in group 3.")
else:
  print ("You have been eliminated from the tournament.")