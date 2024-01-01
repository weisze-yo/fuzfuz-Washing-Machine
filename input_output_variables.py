import numpy as np
from enum import Enum

class Variable(Enum):
    FABRIC_TYPE = 1
    DIRT_LEVEL = 2
    LOAD_SIZE = 3
    WASH_TIME = 4
    WATER_TEMPERATURE = 5
    AGITATION_INTENSITY = 6

class LinguisticVariable(Enum):
    DELICATE = 1
    COTTON = 2
    SYNTHETIC = 3
    LOW = 4
    MEDIUM = 5
    HIGH = 6
    SMALL = 7
    LARGE = 8
    COLD = 9
    WARM = 10
    HOT = 11
    VERY_SHORT = 12
    SHORT = 13
    LONG = 14
    VERY_LONG = 15
    GENTLE = 16
    NORMAL = 17
    STRONG = 18

ranges = {
    # Input
    "fabric_type": np.arange(0, 11, 1),
    "dirt_level": np.arange(0, 11, 1),
    "load_size": np.arange(0, 11, 1),
    # Output
    "wash_time": np.arange(0, 61, 1),
    "water_temperature": np.arange(18, 61, 1),
    "agitation_intensity": np.arange(0, 11, 1)
}