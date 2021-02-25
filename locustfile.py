# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:29:10 2021

@author: LSH
"""


from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(2, 3)

    @task
    def on_start(self):
        REST = "/v2/models/SE-DKT+/versions/1/infer"
        input_json = {
                        "id": "asdfasdf",
                        "inputs": [
                            {
                                "name": "inputs",
                                "shape": [1,10,2],
                                "datatype": "INT32",
                                "data": [[1,0], [2,0], [3,0]]
                            },
                            {
                                "name": "input_c_state",
                                "shape": [1,200],
                                "datatype": "FP32",
                                "data": [0]
                            },
                            {
                                "name": "input_h_state",
                                "shape": [1,200],
                                "datatype": "FP32",
                                "data": [0]
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