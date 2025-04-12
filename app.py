from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle

app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__': 
    app.run(debug=True)