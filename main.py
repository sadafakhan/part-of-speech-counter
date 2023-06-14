
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
import fileinput

# set constituency counters to 0
sentence = 0
np = 0
vp = 0
dtv = 0
itv = 0

# instantiate stacks
npchildren = deque()
parentheses = deque()

working_dir = sys.argv[1]
for file in os.listdir(working_dir):
    with open(os.path.join(working_dir, file), 'r') as f:

        content = f.read()
        content = content.replace(')', ' ) ')

        for elem in content.split():
            if elem == '(S':
                sentence += 1

            elif elem == '(VP':
                vp += 1

                # add values to stacks to indicate we are now inside a VP and haven't encountered direct NP children yet
                npchildren.append(0)
                parentheses.append(0)

            elif elem == '(NP':
                np += 1

                # if we're only one level deep into a VP's children, count the NP as a direct child
                if len(parentheses) == 1:
                    parentheses.append(0)
                    npchildren.append(npchildren.pop() + 1)

                # if we're more than one level deep, keep counting the parentheses but not the NP as a direct child
                else:
                    parentheses.append(0)

            elif elem[0] == '(':
                if len(parentheses) > 0:
                    parentheses.append(0)

            elif elem == ')':
                if len(parentheses) > 0:
                    parentheses.pop()

            # once we've excited a VP phrase and have counted all the direct children, make a judgement of verb type
            if len(parentheses) == 0 & len(npchildren) > 0:
                total = npchildren.pop()
                if total > 1:
                    dtv += 1
                elif total == 0:
                    itv += 1

output = "Sentence\t" + str(sentence) + "\n" + "Noun Phrase\t" + str(np) + "\n" + "Verb Phrase\t" + str(vp) + "\n" + \
         "Ditransitive Verb Phrase\t" + str(dtv) + "\n" + "Intransitive Verb Phrase\t" + str(itv) + "\n"

print(output)