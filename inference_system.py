from skfuzzy import control as ctrl
from knowledge_base import ctrl_rules, fabric_type, dirt_level, load_size, wash_time, water_temperature, agitation_intensity

class FuzzyWashSystem:
    def __init__(self):
        self.system = ctrl.ControlSystem(ctrl_rules)
        self.simulation = ctrl.ControlSystemSimulation(self.system)

    def predict(self, fabric_type_value, dirt_level_value, load_size_value):
        self.simulation.input['fabric_type'] = fabric_type_value
        self.simulation.input['dirt_level'] = dirt_level_value
        self.simulation.input['load_size'] = load_size_value
        # Perform the aggregation using the max-min method
        self.simulation.compute()
    
        #Default Defuzzification
        
        return (
            round(self.simulation.output['wash_time'],2),
            round(self.simulation.output['water_temperature'],2),
            round(self.simulation.output['agitation_intensity'],2)
        )
        
    
    def visualize(self):
        fabric_type.view(sim=self.simulation)
        dirt_level.view(sim=self.simulation)
        load_size.view(sim=self.simulation)
        wash_time.view(sim=self.simulation)
        water_temperature.view(sim=self.simulation)
        agitation_intensity.view(sim=self.simulation)
        input("Press Enter to close the plots")
