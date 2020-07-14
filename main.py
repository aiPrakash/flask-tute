from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def SamplePost():
    return render_template('post.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)
