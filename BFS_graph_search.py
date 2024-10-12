from collections import deque
import math
from typing import Deque, Set
from Node import Node



def BFSgraphSearch(goal:int) -> str:
    if goal % 2 == 0: return f"{BFSgraphSearch(goal / 2)}=>{goal}"
    frontier:Deque['Node'] = deque([Node(4.0, None)])
    explored:Set[float] = set()
    while len(frontier) > 0:
        L = frontier.popleft()
        explored.add(L.state)
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode == goal:
                return f"{L}=>{expandedNode}"
            if expandedNode not in explored:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"

