import os
_current_dir = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR: str = os.path.realpath(os.path.join(_current_dir, ".."))
SCRIPT_DIR: str = os.path.join(PROJECT_DIR, "script")
EXPERIMENTS_DIR: str = os.path.join(PROJECT_DIR, "data/experiments")
WORKS: list[str] = [
    "lsgraph", 
    "graphone", 
    "xpgraph", 
    "bubble",
    "bubble_ordered",
]

BATCH_SIZE: list[int] = [2**10, 2**11, 2**12, 2**13, 2**14, 2**15, 
                         2**16, 2**17, 2**18, 2**19, 2**20]