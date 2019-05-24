# -*- coding: utf-8 -*-
"""
Created on Thu May 23 05:20:54 2019

@author: Jiwitesh_Sharma
"""
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import  Interpreter
from rasa_nlu.test import run_evaluation

builder = ComponentBuilder(use_cache=True)

def train_nlu(data, config_file, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(config_file))
	trainer.train(training_data)
	trainer.persist(model_dir, fixed_model_name = 'restaurantnlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/restaurantnlu', builder)
	print(interpreter.parse("hi"))
	
def evaluateNLU():
    run_evaluation('./data/data.json', './models/nlu/default/restaurantnlu')

if __name__ == '__main__':
	train_nlu('./data/data.json', 'config.yml', './models/nlu')
	run_nlu()