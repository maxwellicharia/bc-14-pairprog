from . forms import SignUp

from app import *

app = Flask(__name__)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
	form = SignUp()
	return render_template('auth/signup.html', form=form, title='Signup')