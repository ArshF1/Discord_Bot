# import array as arr

import numpy as np


public_cmd=np.array(["Arsh","Mahesh","Bhanu","Charchit"])
admin_cmd=np.array([])

def my_generator():
    for i in public_cmd:
        yield i

gen=my_generator()

print(public_cmd[1])