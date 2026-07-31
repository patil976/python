#Write a program to input a string and display its length without using the len() function. 
'''string = input("Enter a string: ")
count = 0
for char in string:
    count += 1
print("Length of the string is:", count)'''


#Reverse the given string without using built-in reverse functions. 
'''string= input("Enter a String")
reverse = ""
for ch in string:
    reverse = ch + reverse
print("Reversed string:", reverse)'''


#Count the number of uppercase and lowercase letters in a string
'''string=input("Enter a string")
uppercase = 0
lowercase = 0
for ch in string:
     if ch.isupper():
          uppercase += 1 
     elif ch.islower():
          lowercase += 1     
print("Uppercase letters:", uppercase)
print("Lowewrcase letters:", lowercase)'''

#●	Replace all occurrences of a given character with another character. 

'''string = input("Enter a string ")
old_char = input("Enter the character to replace ")
new_char = input("Enter the new character ")
new_string = string.replace(old_char, new_char)

print("The replaced string is", new_string)'''

#	Remove all spaces from the input string. 

'''string=input("Enter a string")
new_string = string.replace(" ","")
print("string after removing spaces", new_string)'''

#Find the number of times a specified character appears in a string. 

'''string=input("Enter A String")
char = input("Enter the character to count: ")
count = string.count(char)
print("The character appears", count, "times.")'''

#Print the first and last character of a string

'''string = input("Enter a string")
print("First character:", string[0])
print("Last character:", string[-1])'''

#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
'''string = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
for ch in string:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)'''


#Find the longest word in a given sentence. 

'''sentence = input("Enter a sentence: ")
words = sentence.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
print("Length:", len(longest))'''


#Find the shortest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:", shortest)
print("Length:", len(shortest))

