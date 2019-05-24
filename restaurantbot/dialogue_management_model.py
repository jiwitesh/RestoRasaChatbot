# -*- coding: utf-8 -*-
"""
Created on Thu May 23 05:20:15 2019

@author: Jiwitesh_Sharma
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from rasa_core.channels.slack import SlackInput
from rasa_core.utils import EndpointConfig
#from rasa_core.channels.console import ConsoleInputChannel
#from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'restaurant_domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):
	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])
	training_data = agent.load_data(training_data_file)
	agent.train(training_data)
				
	agent.persist(model_path)
	return agent


def run_restaurant_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
    agent = Agent.load('./models/dialogue', interpreter = interpreter, action_endpoint ='./endpoints.yml')
    #agent = Agent.load('./models/dialogue', interpreter = interpreter)
    input_channel = SlackInput('BOT_SLACK_API_HERE')#your bot user authentication token
    agent.handle_channels([input_channel], 5004, serve_forever=True)
    return agent
	
if __name__ == '__main__':
	#train_dialogue()
	run_restaurant_bot()
    
    
"""from IPython.display import Image

agent = Agent('restaurant_domain.yml')
agent.visualize("./data/stories.md", "story_graph2.html", max_history=2)
Image(filename="story_graph2.html")"""
