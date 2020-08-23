from flask import Flask
# __name__ is just a special variable in python that is just a name of the module
# name looks for if __name__ = 'main'. this how flask knows where to look for your templates, static files and things like that
app = Flask(__name__)


# decorator needed here to show what we are going to have on our website main page
@app.route("/")  # '/' = homepage (http://localhost:5000/)
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# the following condition only works if we run "python flaskblog.py"
# the app can be also run with "flask run" since we've assigned the name
# of this file to env variable with "export FLASK_APP=flaskblog.py"
if __name__ == "__main__":
    app.run(debug=True)
