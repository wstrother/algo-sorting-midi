from midi import NoteGenerator
from log_algo import log_algorithm, get_step_list
from io import StringIO


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
    
    step_data = log_algorithm(
        [randint(0,999) for _ in range(4)],
        bubble_sort
    )
        
    # read the csv and convert to notes
    steps = get_step_list(step_data)
    
    generator = NoteGenerator()
    generator.create_midi(steps, 'output.mid')
    