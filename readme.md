### Sorting Algo MIDI

Comparing sorting algorithms is a canonical example in studying algorithm performance and efficiency. On Youtube you can even find examples
of visualization algorithms that will incorporate audio output based on array accesses that allow you to experience the "general vibe"
of different algorithms based on their approach to comparing and sorting elements of an array.

With that in mind, I decided to create a python script that generates actual MIDI files based on sorting algorithms that can then
be imported into the DAW and post-processed with MIDI filters and other audio processing plugins (VSTs).

The general idea will be to specify some parameters such as the particular sorting algorithm, the size of the array, and particular
guidelines for how the MIDI will be generated (potential for swing or other rhythmic transformations, as well as note mapping guidelines)
and get a MIDI file as output that can be used as an element in music production.

## Requirements

* Python 3
* MIDIUtil package
```
pip install MIDIUtil
```