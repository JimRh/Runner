import docker
import os

def dockersandbox():

    client = docker.from_env(base_url='unix://var/run/docker.sock')
    image = client.images.pull("jimrhh/rce2:latest")

    container = client.containers.run(
        image=image,
        volumes={os.getcwd(): {'bind': '/App', 'mode': 'rw'}},
        remove=True,
        stdout=True,

    )

    output = container.decode('utf-8')
    
    return output
   


dockersandbox()


