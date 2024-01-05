from skfuzzy import control as ctrl
from collections import namedtuple

from membership_function import MF
from input_output_variables import ranges, Variable, LinguisticVariable

from collections import namedtuple

T = namedtuple("Variable", ['name', 'term'])

class Rule:
     def __init__(self, IF, THEN):
        self.IF = IF
        self.THEN = THEN


rules = [
    # fabric_type = delicate
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.VERY_SHORT), T(Variable.WATER_TEMPERATURE, LinguisticVariable.COLD), T(Variable.AGITATION_INTENSITY, LinguisticVariable.GENTLE)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.SHORT), T(Variable.WATER_TEMPERATURE, LinguisticVariable.COLD), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),

    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.COLD), T(Variable.AGITATION_INTENSITY, LinguisticVariable.GENTLE)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.COLD), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.COLD), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.GENTLE)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.DELICATE), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.VERY_LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.GENTLE)]),
    
    # fabric_type = cotton
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.SHORT), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.GENTLE)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),

    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.HOT), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.HOT), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.COTTON), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.VERY_LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.HOT), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    
    # fabric_type = synthetic
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.SHORT), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.GENTLE)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.LOW), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),

    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.MEDIUM), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.NORMAL)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.MEDIUM), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.VERY_LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.WARM), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.SMALL)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.HOT), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.MEDIUM)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.HOT), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)]),
    Rule(IF=[T(Variable.FABRIC_TYPE, LinguisticVariable.SYNTHETIC), T(Variable.DIRT_LEVEL, LinguisticVariable.HIGH), T(Variable.LOAD_SIZE, LinguisticVariable.LARGE)], 
         THEN=[T(Variable.WASH_TIME, LinguisticVariable.VERY_LONG), T(Variable.WATER_TEMPERATURE, LinguisticVariable.HOT), T(Variable.AGITATION_INTENSITY, LinguisticVariable.STRONG)])
]

# Define Antecedents and Consequents
fabric_type = ctrl.Antecedent(ranges["fabric_type"], 'fabric_type')
dirt_level = ctrl.Antecedent(ranges["dirt_level"], 'dirt_level')
load_size = ctrl.Antecedent(ranges["load_size"], 'load_size')
wash_time = ctrl.Consequent(ranges["wash_time"], 'wash_time')
water_temperature = ctrl.Consequent(ranges["water_temperature"], 'water_temperature')
agitation_intensity = ctrl.Consequent(ranges["agitation_intensity"], 'agitation_intensity')

# Add membership functions to Antecedents and Consequents
for var_name, var in zip(["fabric_type", "dirt_level", "load_size", "wash_time", "water_temperature", "agitation_intensity"], 
                         [fabric_type, dirt_level, load_size, wash_time, water_temperature, agitation_intensity]):
     for term in MF[Variable[var_name.upper()]]:
          var[term.name.lower()] = MF[Variable[var_name.upper()]][term]

# Convert Rule objects to ctrl.Rule objects
ctrl_rules = []
for rule in rules:
    antecedent = fabric_type[rule.IF[0].term.name.lower()] & dirt_level[rule.IF[1].term.name.lower()] & load_size[rule.IF[2].term.name.lower()]
    consequent = [wash_time[rule.THEN[0].term.name.lower()], water_temperature[rule.THEN[1].term.name.lower()], agitation_intensity[rule.THEN[2].term.name.lower()]]
    ctrl_rules.append(ctrl.Rule(antecedent, consequent))