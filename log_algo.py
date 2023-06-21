from io import StringIO
import sys
import csv


WRITE = "write"
READ = "read"
COMPARE = "compare"


def log_step(step, index=None):
    if index is None:
        index = ''
    
    print(f'{step},{index}')


class LogInt(int):
    def __gt__(self, other: int) -> bool:
        log_step(COMPARE)
        return super().__gt__(other)

class LogList(list):
    def __getitem__(self, i):
        log_step(READ, i)
        return super().__getitem__(i)
    
    def __setitem__(self, i, value):
        log_step(WRITE, i)        
        super().__setitem__(i, value)


def log_array(values):
    return LogList([LogInt(i) for i in values])

def log_algorithm(arr, algorithm):
    arr = log_array(arr)
    
    with StringIO() as step_data:
        _print = sys.stdout
        
        sys.stdout = step_data
        algorithm(arr)
        sys.stdout = _print

        return step_data.getvalue()

def get_step_list(step_data):
    steps = [] 
            
    for row in csv.reader(StringIO(step_data)):
        try:
            value = int(row[1])
        except ValueError:
            value = None
        steps.append((row[0], value))

    return steps
