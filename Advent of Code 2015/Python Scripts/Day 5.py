#!/usr/bin/env python
# coding: utf-8

# # --- Day 5: Doesn't He Have Intern-Elves For This? ---
# 
# Santa needs help figuring out which strings in his text file are naughty or nice.
# 
# A nice string is one with all of the following properties:
# 
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
# 
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# 
# How many strings are nice?

# Define test word
word = 'abcdeffghi'

# Read input
import pandas as pd
df = pd.read_csv(r"C:\Users\Jono\Documents\Python Scripts\Day 5 Input.csv")

lst = []

for row in df["Words"]:
    lst.append(row)

# Define a function to count vowels and return if there are >= 3:
def countvowels(word):
    
    vowels = False
    
    a = word.count('a')
    e = word.count('e')
    i = word.count('i')
    o = word.count('o')
    u = word.count('u')

    if (a+e+i+o+u) >=3:
        vowels = True
    else:
        vowels = False
    
    return vowels

# Test function
vowels = countvowels(word)
print(vowels)

# Create a function to parse the string and check each letter against it's next
def countdups(word):

    counter = 0
    dups = False
    a = ''

    for char in word:
        if char == a:
            dups = True
    
        a = char
    
    return dups

# Test function
dups = countdups(word)
print(dups)

# Create a function with if and or's to check for banned pairs
def checksubs(word):
    
    subs = False
    
    if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
        subs = True
        
    return subs

# Test function
subs = checksubs(word)
print(subs)

counter = 0

# Loop through list and apply functions
for entry in lst:
    vowels = countvowels(entry)
    dups = countdups(entry)
    subs = checksubs(entry)
    
    # If all tests are good, increase the counter
    if vowels == True and dups == True and subs == False:
        counter = counter +1

# Answer!
print(counter)


# # Part 2
# 
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
# 
# Now, a nice string is one with all of the following properties:
# 
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:
# 
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# 
# How many strings are nice under these new rules?

# Define a test word
word = 'abugglgsssskbjzjg'

# Create a function for double pairs using string.count(substring) for first 2 values (write first 2 values as a string)
def doublepair(word):

    n = len(word)
    c = len(word)
    dubs = False

    for a in word:
        # Define what each pair looks like
        pair = a + word[(1+n-c)]
        b = word.count(pair)
        # Define what a triple of that letter would look like (to check you don't have aaa looking like 2 pairs)
        trip = a + a + a
        d = word.count(trip)
        # Define what a quadruple would look like, so you don't accidentally rule out a bbbb)
        quad = a + a + a + a
        p = word.count(quad)
        
        # Check if there are 2 more pairs than triples, or there is a quadruple
        if p >= 1 or b - d >=2:
            dubs = True
            break
        
        c = c-1
        
        if c<=1:
            break

    return dubs   

# Test function
dubs = doublepair(word)
print(dubs)

#Define function to check for a bridge letter
def bridge(word):
    
    n = 2
    l = len(word)
    xyx = False
    
    for a in word:
        
        # Check if the letter in the for loop is the same as one 2 ahead
        if a == word[n]:
            xyx = True
            break
        
        n = n+1
        
        if n == l:
            break
    
    return xyx

# Test function
xyx = bridge(word)
print(xyx)


counter = 0

# Run through entries and apply all functions again
for entry in lst:
    dubs = doublepair(entry)
    xyx = bridge(entry)
    
    if dubs == True and xyx == True:
        counter = counter +1
    
print(counter)