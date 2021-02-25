# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:29:10 2021

@author: LSH
"""

import random
from locust import HttpUser, task, between

def generate_input(input_length):
    inputs = []
    for i in range(input_length):
        skill_id = random.randint(1, 544)
        correctness = i%2
        inputs.append([skill_id, correctness])
        
    return inputs

def generate_state():
    state = []
    for i in range(200):
        state.append(random.random())
        
    return state
    

class QuickstartUser(HttpUser):
    wait_time = between(2, 3)

    @task
    def on_start(self):
        input_length = random.randint(1,10)
        REST = "/v2/models/SE-DKT+/versions/1/infer"
        input_json = {
                        "id": "asdfasdf",
                        "inputs": [
                            {
                                "name": "inputs",
                                "shape": [1,input_length,2],
                                "datatype": "INT32",
                                "data": generate_input(input_length)
                            },
                            {
                                "name": "input_c_state",
                                "shape": [1,200],
                                "datatype": "FP32",
                                "data": generate_state()
                            },
                            {
                                "name": "input_h_state",
                                "shape": [1,200],
                                "datatype": "FP32",
                                "data": generate_state()
                            }
                        ],
                        "outputs":[
                            {"name":"preds"},
                            {"name":"output_c_state"},
                            {"name":"output_h_state"}
                        ]
                    }
        response = self.client.post(REST, input_json)
        print("Response status code:", response.status_code)
        print("Response text:", response.text)