from flask import Flask, Response, request
import random
import requests

app = Flask(__name__)


@app.route('/animal', methods=['GET'])
def animal():
    animals= ["dog", "cat", "cow", "pig"]
    choice = random.choice(animals)
    return Response(choice, mimetype='text/plain')


@app.route('/noise', methods=['GET', 'POST'])
def noise():
    animal = request.data.decode('utf-8')
    if animal == "dog":
        noise = "woof"
    elif animal == "cat":
        noise = "meow"
    elif animal == "cow":
        noise = "moo"
    elif animal == "pig":
        noise = "oink"
    else:
        noise = "none"
    return Response(noise, mimetype='text/plain')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
