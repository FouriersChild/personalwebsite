from flask import Flask,render_template, url_for, flash, redirect
from setup import app

@app.route('/')
def home():
    return render_template("template.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")
if __name__ == '__main__':
    app.run(debug=True)
