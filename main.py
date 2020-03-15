from flask import Flask,redirect,url_for,request,render_template
import os
import io
import addMessage
app = Flask(__name__)
userNumber={}
userNumber['未知用户'] = 1
number = 0
@app.route('/load', methods=['GET', 'POST'])
def writeEdit():
    # root_dir = os.path.abspath(os.path.dirname(__file__))
    # img_path = root_dir+'\static'+'\img'
    # figfile = io.BytesIO(open(img_path, 'rb').read())
    # img = base64.b64encode(figfile.getvalue()).decode('ascii')
    
    if request.method == 'POST':
        userdata= request.json
        print(userdata)
        username = userdata['username']
        if userNumber.get(username) == None:
            userNumber[username] = 0;
        addMessage.addMessage(userdata)
        userNumber[username] = userNumber[username] +1;
        print("即将返回。。。。。")
        print(userNumber[username])
        return str(userNumber[username])
    elif request.method == 'GET':
        return render_template('load.html',number=number)
        #return render_template('load.html',img=img)
@app.route('/')
def hello_world():
    return render_template('load.html',number=number)
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80,debug=True)