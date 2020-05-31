from collections import defaultdict
from sys import stdin

def isWorse(a, b):
    queue = [a]
    visited = set()
    visited.add(a)
    while queue:
        cur = queue.pop()
        for worseCountry in countryList[cur]:
            if worseCountry == b:
                return True
            elif worseCountry not in visited:
                visited.add(worseCountry)
                queue.append(worseCountry)
    return False

n, m = map(int, stdin.readline().split())
countryList = defaultdict(lambda : list())

for i in range(n):
    a, b = stdin.readline().replace("\n", "").split(" are worse than ")
    countryList[a].append(b)

for i in range(m):
    a, b = stdin.readline().replace("\n", "").split(" are worse than ")
    if isWorse(a, b):
        print("Fact")
    elif isWorse(b, a):
        print("Alternative Fact")
    else:
        print("Pants on Fire")