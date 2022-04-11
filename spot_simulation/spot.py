import time
from board import SCL,SDA

import enum

class SpotBehaviour(enum.Enum):
        REST = 0
        TROT = 1
        CRAWL = 2
        STAND = 3
