# -*- coding: utf-8 -*-
"""
demo example
"""
import numpy as np
import time

class ourmethod():
    def __init__(self):
        self._3e4Result = np.loadtxt("3e4Result")
        self._2e4Result = np.loadtxt("2e4Result")  
        self.array_average_res = 2.5e4
    def calculate_array_output(self,InputVoltage):
        array_output=np.zeros([1,256])
        response_array = (self._3e4Result+self._2e4Result)/2
        array_output = InputVoltage*response_array
        return array_output


ourmethod = ourmethod()
InputVoltage=np.ones([1,256])*0.7
average_times = []
for i in range(2000):
    start_time = time.time()
    ourmethod.calculate_array_output(InputVoltage)
    stop_time = time.time()
    average_times.append(stop_time-start_time)
average_time = np.mean(average_times)
    

print("Our method time cost is {}".format(average_time))