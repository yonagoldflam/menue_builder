import random
from enum import Enum


class MissileNames:

    TORPEDO: str = 'torpedo'
    BALLISTIC: str = 'ballistic'
    CRUISE: str = 'cruise'

class PrecentSuccess:
    TORPEDO = 100
    BALLISTIC = 50
    CRUISE = 20