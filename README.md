# part-of-speech-counter
```part-of-speech-counter``` counts the number of syntactic constituent types that occur in an annotated corpus. Stacks are employed to keep track of constituents that are defined by a nested structure. For example, ditransitive verb phrases are counted by counting verb phrases followed by two nested noun phrases, whereas intransitive verb phrases are counted by counting verb phrases with no nested children. 

Args:
* ```./input```: directory path to the folder containing WSJ data.

Returns:
* ```output```: formatted table listing count of each constituency type.

To run: 
```
src/run.sh input 
```

PROJECT 1 OF LING473 (08/07/2021)
