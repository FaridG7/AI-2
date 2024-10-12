from benchmark import benchmark
from IDS import IDS
from Logger import Logger

logger = Logger()

for i in [5, 56, 34, 33,77, 123, 125, 367, 123, 346, 333, 777, 125, 999, 997, 43, 245]:
    logger.log(("*"*20)+f"i = {i}")
    logger.log(f"{benchmark(IDS, i)}")