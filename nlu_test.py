# from rasa_nlu.model import Interpreter
# import json
# interpreter = Interpreter.load("./models/nlu/default/weather")
# message = "let's see some italian restaurants"
# result = interpreter.parse(message)
# print(json.dumps(result, indent=2))


from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter
from rasa_nlu.components import ComponentBuilder

builder = ComponentBuilder(use_cache=True)      # will cache components between pipelines (where possible)


training_data = load_data('data.json')
trainer = Trainer(config.load("nlu_config.yml"),builder)
trainer.train(training_data)
model_directory = trainer.persist('./projects/default/')

# where model_directory points to the model folder
interpreter = Interpreter.load(model_directory)

interpreter.parse(u"The text I want to understand")

