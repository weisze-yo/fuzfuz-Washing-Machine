import skfuzzy as fuzz
from input_output_variables import ranges, LinguisticVariable, Variable

# Define membership functions
MF = {
    Variable.FABRIC_TYPE:{
        LinguisticVariable.DELICATE: fuzz.trimf(ranges["fabric_type"], [0, 0, 5]),
        LinguisticVariable.COTTON: fuzz.trimf(ranges["fabric_type"], [0, 5, 10]),
        LinguisticVariable.SYNTHETIC: fuzz.trimf(ranges["fabric_type"], [5, 10, 10])
    },
    Variable.DIRT_LEVEL:{
        LinguisticVariable.LOW: fuzz.trimf(ranges["dirt_level"], [0, 0, 5]),
        LinguisticVariable.MEDIUM: fuzz.trimf(ranges["dirt_level"], [0, 5, 10]),
        LinguisticVariable.HIGH: fuzz.trimf(ranges["dirt_level"], [5, 10, 10])
    },
    Variable.LOAD_SIZE:{
        LinguisticVariable.SMALL: fuzz.trimf(ranges["load_size"], [0, 0, 5]),
        LinguisticVariable.MEDIUM: fuzz.trimf(ranges["load_size"], [0, 5, 10]),
        LinguisticVariable.LARGE: fuzz.trimf(ranges["load_size"], [5, 10, 10])
    },
    Variable.WASH_TIME:{
        LinguisticVariable.VERY_SHORT: fuzz.trimf(ranges["wash_time"], [0, 8, 12]),
        LinguisticVariable.SHORT: fuzz.trimf(ranges["wash_time"], [8, 12, 20]),
        LinguisticVariable.MEDIUM: fuzz.trimf(ranges["wash_time"], [12, 20, 40]),
        LinguisticVariable.LONG: fuzz.trimf(ranges["wash_time"], [20, 40, 60]),
        LinguisticVariable.VERY_LONG: fuzz.trimf(ranges["wash_time"], [40, 60, 60]),
    },
    Variable.WATER_TEMPERATURE:{
        LinguisticVariable.COLD: fuzz.trimf(ranges["water_temperature"], [18, 18, 39]),
        LinguisticVariable.WARM: fuzz.trimf(ranges["water_temperature"], [18, 39, 60]),
        LinguisticVariable.HOT: fuzz.trimf(ranges["water_temperature"], [39, 60, 60])
    },
    Variable.AGITATION_INTENSITY:{
        LinguisticVariable.GENTLE: fuzz.trimf(ranges["agitation_intensity"], [0, 0, 5]),
        LinguisticVariable.NORMAL: fuzz.trimf(ranges["agitation_intensity"], [0, 5, 10]),
        LinguisticVariable.STRONG: fuzz.trimf(ranges["agitation_intensity"], [5, 10, 10])
    }
}