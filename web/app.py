from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	opinion = "ugly"
	return render_template("index.html", opinion=None)

@app.route('/list')
def list_view():
	lis = ["potato", "sukuma", "oranges", 'onions']
	cars = ["range rover", "jaguar"]
	return render_template('list.html', items=lis, magari=cars)


@app.route('/about')
def about():
	return "THis is the about page"


@app.route('/profile/<username>')
def profile(username):
	return "Your username is {}".format(username)


@app.route('/posts/<int:post_id>')
def post(post_id):
	return "My post id is {}".format(post_id)