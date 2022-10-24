from simulation_manager import SimulationManager
import datetime
from datetime import timedelta
limit = 5

simulated_days = 1
model_file = ""
sm = SimulationManager(start = datetime.datetime.now(), end = datetime.datetime.now() + timedelta(days=simulated_days))
simulator_file_name = "simulator_output"
sm.simulate(name=simulator_file_name,resource_limit={'support': limit, 'trust': limit})

