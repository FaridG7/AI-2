from benchmark import benchmark
from BFS_graph_search import BFSgraphSearch
from BFS_hybrid_search import BFShybridSearch
from BFS_tree_search import BFStreeSearch
from Logger import Logger

logger = Logger()

for i in [5, 56, 34, 33, 367, 123, 346, 333, 777, 125, 999, 997, 43, 245]:
    logger.log(("*"*20)+f"i = {i}")
    # logger.log(f"{benchmark(BFStreeSearch, i)}")
    logger.log(f"{benchmark(BFSgraphSearch, i)}")
    logger.log(f"{benchmark(BFShybridSearch, i)}")