#coding: utf-8

import pickle
import os



def initStack():
    Smemory = {'prompt': 0, 'DATE' : 0, 'LOCATION' : None}
    print(os.getcwd())
    f = open("ENTITIES/stack.txt", 'wb')
    pickle.dump(Smemory, f, protocol=0)
    f.close()