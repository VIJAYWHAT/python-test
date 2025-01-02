from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    name = "VJ"
    return render_template('home.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render provides a PORT environment variable
    app.run(debug=False, host='0.0.0.0', port=port)
