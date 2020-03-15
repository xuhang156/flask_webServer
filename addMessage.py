import os.path
import sys
import datetime
from pathlib import Path

def addMessage(decobj):
    print('hello world')
    username = decobj['username']

    fn = getattr(sys.modules['__main__'], '__file__')
    root_path = os.path.abspath(os.path.dirname(fn))

    times = datetime.datetime.now().strftime('%Y_%m_%d') 
    filepath = root_path+"/files/"+ username
    print(filepath)
    my_file = Path(filepath)
    if os.path.exists(my_file) == False:
        print('检测到文件夹不存在')
        os.makedirs(filepath)
    filepath = filepath +"/"+ times+'.csv'
    print(filepath)
    str = decobj['submitTime'] +','+decobj['inputLocations']+','+decobj['inputDescribes'] +'\n'
   
    print(str)
    with open(filepath,mode='a',encoding='utf-8') as ff:
        ff.write(str)
        ff.close
    
    
