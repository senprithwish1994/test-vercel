from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 

@app.route('/')
def home():
    return "Hello from vercel"
 

    
@app.route('/')
def about():
    return "Hello about"
