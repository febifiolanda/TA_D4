from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/profile")
def profile():
	return render_templates('profile.html')
if __name__ == "__main__":
	app.run()