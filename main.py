from collections import deque
import os
import sys
working_dir = sys.argv[1]

counts = {'(S': 0, '(VP': 0, '(NP': 0, "dtv": 0, "itv": 0}
for file in os.listdir(working_dir):
    with open(os.path.join(working_dir, file), 'r') as f:
        depth = deque()
        parse = f.read()
        parse = parse.replace(')', ' ) ')
        
        for pos in parse.split():
            if pos in counts: 
                counts[pos] +=1 
            
            if pos[0] == "(": 
                if pos == "(VP": 
                    depth.append([])
                elif pos == "(NP": 
                    if type(depth[-1]) == list: 
                        depth[-1].append(0)
                    depth.append(0)
                else: 
                    depth.append(0)            
            
            if pos == ")": 
                if len(depth) != 0: 
                    np = depth.pop()
                    if type(np) == list: 
                        if len(np) == 0: 
                            counts["itv"] += 1 
                        if len(np) == 2: 
                            counts["dtv"] += 1 

output = "Sentence\t" + str(counts['(S']) + "\n" + "Noun Phrase\t" + str(counts['(NP']) + "\n" + "Verb Phrase\t" + str(counts['(VP']) + "\n" + "Ditransitive Verb Phrase\t" + str(counts['dtv']) + "\n" + "Intransitive Verb Phrase\t" + str(counts["itv"])
print(output)