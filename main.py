from flask import Flask,url_for,request,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/writeEdit', methods=['GET', 'POST'])
def writeEdit():
    if request.method == 'POST':
        return "post html"
    elif request.method == 'GET':
        return render_template('writhe.html')


if __name__ == '__main__':
    app.run(debug=True)