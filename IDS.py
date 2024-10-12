import math
from typing import  Optional
from Node import Node



def LDS(goal: int, limit:int,initialState:int = 4) -> Optional[str]:
    if initialState == goal: return f"{initialState}"
    if limit > 0:
        mulChild = LDS(goal, limit - 1, initialState * 2)
        if mulChild: return f"{initialState}=>{mulChild}"
        sqrtChild = LDS(goal, limit - 1, math.sqrt(initialState))
        if sqrtChild: return f"{initialState}=>{sqrtChild}"
        floorChild = LDS(goal, limit - 1, math.floor(initialState))
        if floorChild: return f"{initialState}=>{floorChild}"
    else: return None
        

def IDS(goal:int) -> str:
    if goal % 2 == 0: return f"{IDS(goal / 2)}=>{goal}"

    L = math.ceil(math.log2(goal / 4))

    while True:
        result = LDS(goal, L)
        if result: return result + f"(Steps={result.count("=>")})"
        L += 1

