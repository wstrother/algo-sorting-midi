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
