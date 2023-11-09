# reverser.py

# this will reverse the text that is
# input and then print it... woohoo!

string = input("\nEnter a single line of text to be reversed: ")
print()
output = string[::-1]
print(f"{string} <-- REVERSED is --> {output}\n")
