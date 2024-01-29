"""Madlib Generator"""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey999"
debug = DebugToolbarExtension(app)


@app.route('/home')
def home():
    """Displays the homepage with the Madlibs form to fill out"""

    prompts = story.prompts
    return render_template("home.html", prompts=prompts)

@app.route('/story')
def create_story():
    """Displays the story based on the users Madlib input"""

    text = story.generate(request.args)
    return render_template("story.html", text=text)