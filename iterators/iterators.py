def generate_input_lines(n):
    for item in range(n):
        yield item/2

import itertools
import sys
import time

prog = itertools.cycle([' -',' \\',' |',' /'])
prog = itertools.cycle([' .',' o',' O'])

for i in range(10000):
    sys.stdout.write(next(prog)+'\b\b\b')
    sys.stdout.flush()
    time.sleep(0.1)



