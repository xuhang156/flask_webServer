from flask import Flask,url_for,request,render_template
import os
import io
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/load', methods=['GET', 'POST'])
def writeEdit():
    # root_dir = os.path.abspath(os.path.dirname(__file__))
    # img_path = root_dir+'\static'+'\img'
    # figfile = io.BytesIO(open(img_path, 'rb').read())
    # img = base64.b64encode(figfile.getvalue()).decode('ascii')
    number = 43
    if request.method == 'POST':
        userdata= request.json
        print(userdata)
        return "post html"
    elif request.method == 'GET':
        return render_template('load.html',number=number)
        #return render_template('load.html',img=img)

if __name__ == '__main__':
    app.run(debug=True)