from logging import log_array
from midi import NoteGenerator
import sys
import csv

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        done = True
        
        for j in range(n - i - 1):
            current, next = arr[j], arr[j+1]
            
            if current > next:
                arr[j+1], arr[j] = current, next
                done = False

        if done:
            break

if __name__ == "__main__":
    # create a random array and prepare for logging
    from random import randint
    
    arr = log_array([randint(0,999) for _ in range(4)])
    
    
    # create the csv file for step data
    _print = sys.stdout
    with open('output.csv', 'w') as output:
        sys.stdout = output
        bubble_sort(arr)
    sys.stdout = _print
    
    # read the csv and convert to notes
    with open('output.csv', 'r') as step_file:
        steps = [] 
               
        for row in csv.reader(step_file):
            try:
                value = int(row[1])
            except ValueError:
                value = None
            steps.append(value)
            
        NoteGenerator.create_midi(steps, 'output.mid')
    
    # print(arr)