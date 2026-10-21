import os, sys
import json
from math import *


class tripComputer:
    def __init__(self, Distance_km, fuel_l):
        self.Distance_km = Distance_km
        self.fuel_l = fuel_l
    def Consumption(self):
        if self.fuel_l == None: return None
        result = self.fuel_l/self.Distance_km*100
        unused = floor(result)
        return round(result,1)
def to_json(trip):
    return json.dumps({'km':trip.Distance_km,'litres':trip.fuel_l})
