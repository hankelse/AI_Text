import random


drac_file = open("AI-Text/dracula.txt", "r")

lines = drac_file.readlines()
print (lines)


def clean_words(file):
    

clean_lines = []
for line in lines:
    if line != "\n" and len(line) > 1: 
        if line[-2:] == "\n": clean_lines.append(line[:-2])
        else: clean_lines.append(line)


print(clean_lines)