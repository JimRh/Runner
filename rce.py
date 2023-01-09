from flask import Flask, request,Response
import docker

import os
import sandbox
import pika
app = Flask(__name__)

flag=False

@app.get('/run')
def test():
    return 'running'


@app.get('/getoutput')
def codeexecute():
    output=sandbox.dockersandbox()
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

'''from flask import Flask,request,Response
import pika

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.post('/run')
def add():
    lang = 'python'
    language = request.data
    code = language.decode('utf-8')

    if lang == 'python':
        file = open('input.py', 'w')
        file.write(code)

    else:
        file = open('input.cpp', 'w')
        file.write(code)
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body='run_docker_container',
       )
    def dockerrunner():
        for body in channel.consume():
            yield body
            break



    connection.close()
    return Response(dockerrunner(), direct_passthrough=True)


if __name__ == '__main__':
    app.run(debug=True)'''

