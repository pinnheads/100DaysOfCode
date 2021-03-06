# Challenge 1
# Heads or Tails
# Instructions

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# e.g.
# 1 means Heads
# 0 means Tails
# Example Output

# Heads

# or

# Tails
import random
random_face = random.randint(0,1)
if random_face == 0: 
    print("Tails")
else: 
    print("Heads")

############################################################################
# Challenge 2
# Who's Paying
# Instructions

# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
# Example Input

# Angela, Ben, Jenny, Michael, Chloe

# Note: notice that there is a space between the comma and the next name.
# Example Output

# Michael is going to buy the meal today!

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# random_choice = random.randint(0, len(names))
# print(f"{names[random_choice]} is going to buy the meal today!")

###########################################################################
# Challenge 3
# Treasure Map

# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list.
# When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.

# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

# https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5

# First your program must take the user input and convert it to a usable format.

# Next, you need to use it to update your nested list with an "x".
# Example Input 1

# column 2, row 3 would be entered as:

# 23

# Example Output 1

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', 'X', '⬜️']

# Example Input 2

# column 3, row 1 would be entered as:

# 31

# Example Output 2

# ['⬜️', '⬜️', 'X']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first=position[0]
second=position[1]

a=int(first)-1
b=int(second)-1
map[a][b]="X"


print(f"{row1}\n{row2}\n{row3}")