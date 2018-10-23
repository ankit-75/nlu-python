from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
import json

builder = ComponentBuilder(use_cache = True)
training_data = load_data('nlu.md')
trainer = Trainer(config.load('nlu_config.yml'))
trainer.train(training_data)

model_directory = trainer.persist('./models')
interpreter = Interpreter.load(model_directory)
#interpreter_clone = Interpreter.load(model_directory,builder)

message = "let's see some italian restaurants"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))