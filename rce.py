from flask import Flask, request,Response

import os
import sandbox

app = Flask(__name__)

flag=False

@app.get('/run')
def test():
    return 'running'


@app.get('/getoutput')
def codeexecute():
    #output=sandbox.dockersandbox()
    output=''
    file=os.listdir()
    if 'input.py' in file:
        os.remove('input.py')
    if 'input.cpp' in file:
        os.remove('input.cpp')
    return output

@app.post('/run')
def handle_request():

    # Get the code snippet and programming language from the request


    #output = sandbox.dockersandbox()
    #os.remove('input.py')



    data = request.data.decode('utf-8')
    data=data.split('`')
    language=data[0].split(':')
    lang=language[1]
    code=data[1].split(':')
    code=code[1]

    extension = '.py' if lang == 'python' else '.cpp'
    # Create a .py or .cpp file with the code snippet
    with open('input' + extension, 'w') as f:
        f.write(code)
    return 'Code execution is Completed'



if __name__ == '__main__':
    app.run(debug=True)



