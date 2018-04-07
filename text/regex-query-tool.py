'''
Regex Query Tool
A tool that allows the user to enter a text string and then in a separate control enter a regex pattern.
'''
import re

def regit(text_string):
    regx = input("Regex: ")

    m = re.search(regx, text_string)

    return m.group(0)


text_string = input("Text: ")
print(regit(text_string))
