import pandas as pd
import numpy as np
from happytransformer import HappyGeneration
from happytransformer import GENSettings


# from transformers import GPT2LMHeadModel,  GPT2Tokenizer, GPT2Config, GPT2LMHeadModel
# from transformers import AdamW, get_linear_schedule_with_warmup

#defining the language generation algorithm settings
args = GENSettings(max_length = 40, do_sample = True, early_stopping=True, no_repeat_ngram_size=2, top_k=50, temperature=0.7)


#importing happy generation class
happy_gen = HappyGeneration(model_type="GPT-NEO", model_name="EleutherAI/gpt-neo-125M", load_path="C:/Users/mandi/Downloads/ML-Models-Flask-master/Deploy Image Captioning/model_weights/testhkhk")

text = "#generate a joke about cats"
result = happy_gen.generate_text(text, args=args)
print(text + result.text)



def joke_gen(caption):
	joke = happy_gen.generate_text(caption, args=args)
	print(joke)
	return (caption + joke.text)

	




