#Q5. Count Vowels in a String
#Write a Python program to input a string and count the number of vowels (a, e, i, o, u) in it.

text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)
