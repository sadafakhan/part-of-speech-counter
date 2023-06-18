# part-of-speech-counter
A program that counts the number of syntactic constituent types that occur in an annotated corpus. 
Stacks are employed to keep track of constituents that are defined by a nested structure. For example, ditransitive verb phrases are counted by counting verb phrases followed by two nested noun phrases, whereas intransitive verb phrases are counted by counting verb phrases with no nested children. 

Args:
* dir (str): path to the desired directory.

Returns:
* output (str): formatted table listing count of each constituency type.

To run: 
```
python3 ./main.py data > output
```

PROJECT 1 OF LING473 (08/07/2021)
