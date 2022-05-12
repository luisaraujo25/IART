from collections import deque

class pot:
    def __init__(self, maxCapacity):
        self.lit = 0
        self.cap = maxCapacity

    def fill(self): 
        self.lit = self.cap
        print(self.lit)       

    def empty(self):
        self.lit = 0
        print(self.lit)

    def pour(self,pourer):
        if pourer.lit + self.lit < self.cap:
            self.lit += pourer.lit
            print(self.lit)
        else:
            print("Not a valid operation")


def breadFirst(w1, w2):

    queue = deque()
    visited = []

    firstPair = (w1.lit, w2.lit)
    print(firstPair)
    queue.append(firstPair)

    while w1.lit != 2 & len(queue) > 0:
        
        pair = queue.popleft()
        first = pair[0]
        second = pair[1]
        
        # check if this pair (or state) was already visited
        # if yes then no need to check again
        if visited.count(pair) == 0:
            visited.append(pair)
        else:
            continue

        if first > 0:

            if second < second.cap:
                
            else:

        elif second > 0:

            if first < first.cap:
            
            else:


        elif first < first.cap:

        elif second < second.cap:



# TESTING CONTENT
w1 = pot(4)
w2 = pot(3)

breadFirst(w1,w2)


