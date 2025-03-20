
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static') # Specify the template folder

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)