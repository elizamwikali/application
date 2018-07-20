from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	my_app = "Andela Bits"
	return render_template("index.html",show=my_app)


	if __name__ == "__main__":
		app.run()
