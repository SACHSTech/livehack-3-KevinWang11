"""
-------------------------------------------------------------------------------
Name:   filename.py
Purpose:  a description of your program
 
Author: lastname.First Initial
 
Created:  date in dd/mm/yyyy
------------------------------------------------------------------------------
"""
print("****** Tournament Tracker ******")
print ("")
win_count = 0 
loss_count = 0

for i in range(6):
  result = input("Enter the wins and losses for your team (W/L): ")
  if result == 'W':
    win_count += 1
  elif result == 'L':
    loss_count += 1

if win_count == 5 or win_count == 6:
  print("You have been placed in group 1.")
elif win_count == 3 or win_count == 4:
  print("You have been placed in group 2.")
elif win_count == 1 or win_count == 2:
  print ("You have been placed in group 3.")
else:
  print ("You have been eliminated from the tournament.")