# -*- coding: utf-8 -*-
"""
Created on Thu May 23 05:22:14 2019

@author: Jiwitesh_Sharma
"""
import logging

from rasa_core.policies import KerasPolicy, MemoizationPolicy
from rasa_core.agent import Agent


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    training_data_file = './data/stories.md'
    model_path = './models/dialogue'
    agent = Agent('restaurant_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()], action_endpoint = './endpoints.yml')
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    model_directory = agent.persist(model_path)
    
    
#agent = Agent.load(model_path, interpreter=model_directory)

"""print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_text(a)
    for response in responses:
        print(response["text"])"""
        
