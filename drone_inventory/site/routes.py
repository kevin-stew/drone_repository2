from flask import Blueprint, render_template
from flask_login import login_required


"""
Note that in the above code some arguments are specified in the Blueprint object,
the first argument, 'site' is the blueprint's name,
which is used by flask's rounting mechanism.
the second argument, __name__, is the blueprints' resource
"""

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')