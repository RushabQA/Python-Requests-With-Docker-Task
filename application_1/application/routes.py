from flask import render_template, url_for, redirect, request
from application import app


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')


@app.route('/generate', methods = ['GET'])
def generate():
    form = AnimalForm()
    if form.validate_on_submit():
        formData = Animal(
                animal = form.animal.data,
                noise = form.noise.data
                )
    return render_template('home.html', title='Home')

