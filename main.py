from flask import Flask,url_for,request,render_template
import os
import io
import addMessage
app = Flask(__name__)
userNumber={}
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
        username = userdata['username']
        if userNumber.get(username) == None:
            userNumber[username] = 0;
        addMessage.addMessage(userdata)
        userNumber[username] = userNumber[username] +1;
        print("即将返回。。。。。")
        return render_template('load.html',number=userNumber[username])
    elif request.method == 'GET':
        return render_template('load.html',number=number)
        #return render_template('load.html',img=img)

if __name__ == '__main__':
    app.run(debug=True)