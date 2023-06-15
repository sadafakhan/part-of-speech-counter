                # if con == 'VP': 

            # # encountered pos is not an S, NP, or VP 
            # else: 
            #     if inVP:
            #         inVP.append(0)

            # # # once we've excited a VP phrase and have counted all the direct children, make a judgement of verb type
            # if len(depth) == 0 & npchildren > 0:
            #     if npchildren > 1:
            #         counts['dtv'] += 1
            #     elif npchildren == 0:
            #         counts['itv'] += 1

# output = "Sentence\t" + str(counts['S']) + "\n" + "Noun Phrase\t" + str(counts['NP']) + "\n" + "Verb Phrase\t" + str(counts['VP']) + "\n" + \
#          "Ditransitive Verb Phrase\t" + str(counts['dtv']) + "\n" + "Intransitive Verb Phrase\t" + str(counts['itv']) + "\n"

# print(output)