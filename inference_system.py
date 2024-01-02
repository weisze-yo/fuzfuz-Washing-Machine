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
        # Defuzzification
        # Defuzzification using centroid method
        # wash_time_centroid = ctrl.centroid(self.simulation.output['wash_time'])
        # water_temp_centroid = ctrl.centroid(self.simulation.output['water_temperature'])
        # agitation_intensity_centroid = ctrl.centroid(self.simulation.output['agitation_intensity'])

        # # Print centroid values
        # print("Wash Time Centroid:", wash_time_centroid)
        # print("Water Temperature Centroid:", water_temp_centroid)
        # print("Agitation Intensity Centroid:", agitation_intensity_centroid)

        # return {
        #     'wash_time_centroid': wash_time_centroid,
        #     'water_temp_centroid': water_temp_centroid,
        #     'agitation_intensity_centroid': agitation_intensity_centroid
        # }

        return (
            self.simulation.output['wash_time'],
            self.simulation.output['water_temperature'],
            self.simulation.output['agitation_intensity']
        )
    
    def defuzz_predict(self, fabric_type_value, dirt_level_value, load_size_value, defuzzification_method):
        self.simulation.input['fabric_type'] = fabric_type_value
        self.simulation.input['dirt_level'] = dirt_level_value
        self.simulation.input['load_size'] = load_size_value
        # Perform the aggregation using the max-min method
        self.simulation.compute()

        # Defuzzification based on the provided method
        if defuzzification_method == 'centroid':
            wash_time_output = ctrl.centroid(self.simulation.output['wash_time'])
        elif defuzzification_method == 'bisector':
            wash_time_output = ctrl.defuzz(self.simulation.output['wash_time'], 'bisector')
        elif defuzzification_method == 'mom':
            wash_time_output = ctrl.defuzz(self.simulation.output['wash_time'], 'mom')
        elif defuzzification_method == 'som':
            wash_time_output = ctrl.defuzz(self.simulation.output['wash_time'], 'som')
        elif defuzzification_method == 'lom':
            wash_time_output = ctrl.defuzz(self.simulation.output['wash_time'], 'lom')
        else:
            raise ValueError("Invalid defuzzification method")

        return wash_time_output

    def visualize(self):
        fabric_type.view(sim=self.simulation)
        dirt_level.view(sim=self.simulation)
        load_size.view(sim=self.simulation)
        wash_time.view(sim=self.simulation)
        water_temperature.view(sim=self.simulation)
        agitation_intensity.view(sim=self.simulation)
        input("Press Enter to close the plots")