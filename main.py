'''
Sadaf Khan, Project 1, LING 473, 08/07/2021
This program takes a directory name as input, and returns a table listing the number of given constituents types
within the tree-formatted files contained in the directory.

Args:
    dir (str): path to the desired directory.

Returns:
    output (str): formatted table listing count of each constituency type.
'''

from collections import deque
import os
import sys

working_dir = sys.argv[1]
counts = {'(S': 0, '(VP': 0, '(NP': 0}
structs = []

# extract counts for sentences, verb phrases, and noun phrases 
for file in os.listdir(working_dir):
    with open(os.path.join(working_dir, file), 'r') as f:
        parse = ""
        content = f.read()
        content = content.replace(')', ' ) ')
        for pos in content.split():
            if pos in counts: 
                counts[pos] +=1 
            if pos[0] == "(" or pos == ")": 
                parse += pos + " "
        structs.append(parse)

depth = deque()
vps = [] 

# extract all verb phrases and their nested constituents 
for doc in structs: 
    in_vp = False
    vp = ""
    for pos in doc.split(): 
        if pos == "(VP": 
            depth.append(0)
            in_vp = True

        if in_vp:
            vp += pos + " "
            if pos != "(VP" and pos != ")": 
                depth.append(0)

            if pos == ")": 
                depth.pop()
    
        if len(depth) == 0: 
            in_vp = False 

    vps.append(vp)

dtv = 0 
itv = 0 
for vp in vps: 
    if "(VP (NP ) (NP ) )" in vp: 
        dtv += 1
            
output = "Sentence\t" + str(counts['(S']) + "\n" + "Noun Phrase\t" + str(counts['(NP']) + "\n" + "Verb Phrase\t" + str(counts['(VP']) + "\n" + "Ditransitive Verb Phrase\t" + str(dtv) + "\n" + "Intransitive Verb Phrase\t" + str(itv)
print(output)
# + \ "Ditransitive Verb Phrase\t" + str(counts['dtv']) + "\n" + "Intransitive Verb Phrase\t" + str(counts['itv']) + "\n"
    