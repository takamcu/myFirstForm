from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start.html")

@app.route('/procForm', methods=['POST'])
def processPost():
    msg1 = request.form['msg1']
    msg2 = request.form['msg2']
    msg = int(msg1) + int(msg2)
    return render_template("result.html", message=msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)