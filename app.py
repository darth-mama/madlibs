from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "mooncakes"
debug = DebugToolbarExtension(app)

# pull from self.prompts


@app.route('/')
def home_page():
    prompts = story.prompts
    '''Shows the form on the homepage'''
    return render_template("home_form.html", prompts=prompts)

# pull from self.text


@app.route("/story")
def show_story():
    """Show story results"""

    text = story.generate(request.args)
    return render_template("story_results.html", text=text)
