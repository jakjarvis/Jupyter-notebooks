#!/usr/bin/env python
# coding: utf-8

# # --- Day 2: I Was Told There Would Be No Math ---
# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
# 
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
# 
# For example:
# 
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

 

# Importing the list

import pandas as pd

df = pd.read_csv(r"C:\Users\Jono\Downloads\Input.csv") # my input is saved in a .csv file at this location - you need to save yours as one and change the path to the right location

df.info()

# define empty lists for subsequent code

list2 = []
real_list = []

# Read the rows out of the input dataframe df and into a list (real_list)

for row in df["Presents!"]:
    a, b, c = row.split('x')
    real_list.append([int(a),int(b),int(c)])

# Cycle through the values in real_list and calculate the areas of all the sides (plus the extra), and add them to a new list, list2

for a in real_list:
    x = 2 * a[0] * a[1]
    y = 2 * a[1] * a[2]
    z = 2 * a[2] * a[0]
    b = [x,y,z]
    b.sort()
    xtra = b[:1]

    b.append(xtra[0]/2)
    list2.append(b)

# for each present in the list, sum all the areas of paper in list2 and creat a third and final list, shopping_list, contining the total paper per present
    
shopping_list = []

for present in list2:
    shopping_list.append(sum(present))

print(shopping_list)

# add up all the presents for a total
order = sum(shopping_list)

print(order)


# # Part 2

# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.
# 
# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
# 
# For example:
# 
# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
# A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
# 
# How many total feet of ribbon should they order?

list3 = []

# similar logic to Part 1 but this time instead of using two seperate lists (list2 and shopping_list) I did it all in one step to complete a list of total ribbon per present

for a in real_list:
    a.sort()
    ribbon = 2*a[0]+2*a[1]+(a[0]*a[1]*a[2])
    
    list3.append(ribbon)
print(list3)

Output = sum(list3)
print(Output)

