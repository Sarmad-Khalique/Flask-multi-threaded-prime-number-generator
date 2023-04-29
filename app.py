from flask import Flask, render_template, request
from finders import PrimeFinder

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('pages/generate.html')

@app.route("/generate", methods=["POST"])
def generate():
    if request.method == 'POST':
        numbers_list = []
        start = int(request.form['start'])
        end = int(request.form['end'])

        # Create a new PrimeFinder object
        finder = PrimeFinder(start, end, numbers_list)
        finder.start()

        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)