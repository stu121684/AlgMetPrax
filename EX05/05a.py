from dataclasses import dataclass
from sys import stdin
from queue import PriorityQueue
import sys

@dataclass(order=True)
class node:
    key : int
    x : int(compare=False)
    y : int(compare=False)
    z : int(compare=False)
    def __init__(self, x, y, z):
        self.key = 300001
        self.x = x
        self.y = y
        self.z = z

testcases = int(stdin.readline())
for i in range(1, testcases+1):
    n = int(stdin.readline())
    nodes = PriorityQueue()
    
    for i in range(n):
        x, y, z = map(int, stdin.readline().split())
        nodes.put(node(x, y, z))
    
    mstSet = set()


    if i < testcases:
        stdin.readline()