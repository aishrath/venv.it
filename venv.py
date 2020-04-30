import subprocess
import logging
import sys

log = logging.getLogger("venv")
log.setLevel(logging.INFO)

def shell(cmd):
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, _ = p.communicate()
    return output

if __name__ == '__main__':
   log.info('Initializing virtualenv generator')

   venv = input('Enter name of folder where venv will be generated: ')
   log.info(f'Venv will be created in: {venv}')

   cmd = f'mkdir {venv} && cd {venv}'
   exit_code = shell(cmd)
   log.debug('Exit code: {exit_code}')
