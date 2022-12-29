from queue import Empty
from turtle import pos
from flask import Flask, render_template, url_for, request, redirect
from caption import *
from jokes import *
from main import jokes_post_process
import warnings
warnings.filterwarnings("ignore")
import PIL


	
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']

		print(img)
		print(img.filename)

		img.save("static/"+img.filename)


		caption = caption_this_image("static/"+img.filename)
		
		jokes = joke_gen(caption)
		
		print("jokes", jokes)
		
		joke = jokes_post_process(caption,jokes, img.filename)
		
		if joke is None:
			joke = jokes
		
		result_dic = {
			'image' : "static/" + img.filename,
			'description' : joke
		}
	return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(debug = True)