import docker
import os
import subprocess
'''def dockersandbox():

    client = docker.from_env()
    image = client.images.pull("jimrhh/rce2:latest")

    container = client.containers.run(
        image=image,
        volumes={os.getcwd(): {'bind': '/App', 'mode': 'rw'}},
        remove=True,
        stdout=True,

    )

    output = container.decode('utf-8')
    
    return output
   


dockersandbox()'''


