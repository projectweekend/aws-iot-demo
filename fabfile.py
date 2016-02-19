from fabric.api import cd, env, run, local, sudo, settings


env.use_ssh_config = True
env.user = 'pi'


def clone():
    run('git clone https://github.com/projectweekend/aws-iot-demo.git')


def update():
    with cd('aws-iot-demo'):
        run('git pull origin master')
        sudo('pip install -r requirements.txt')
