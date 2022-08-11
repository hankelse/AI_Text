import random

no_nos = [".", "?", "!", ",", ":", ";"]

file = open("text.txt")
lines = file.readlines()

word_dict = {}

i = 0
for n in range(len(lines)):
    lines[i] = lines[i].strip()
    if lines[i] == "\n": 
        lines.remove(lines[i])
        i -= 1
        lines[i] = lines[i].strip('\n')
    for no_no in no_nos:
        lines[i] = lines[i].replace(no_no, "")
    
    words = lines[i].split(" ")
    #print(words)
    for x in range(len(words)-1):
        if words[x] in word_dict:
            word_dict[words[x]].append(words[x+1])
        else:
            word_dict[words[x]] = [words[x+1]]

    i += 1



output = ["I"]
starting_word = "I"
word = starting_word
while word in word_dict:
    #print(word_dict[word])
    word = random.choice(word_dict[word])
    output.append(word)

#print(output)
string = ""
for word in output:
    string += word
    string += " "

print(string)


