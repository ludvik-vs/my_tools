import os
import subprocess

os.listdir()

with open('requirements.txt', 'r') as file:
    packages = [line.strip() for line in file]

for packageName in packages:
    try:
        subprocess.call(f'echo remove {packageName}', shell=True)
        subprocess.call('pip3.11 uninstall -y ' + packageName, shell=True)
    except FileNotFoundError as e:
        print(e)
        print("\n")

# pip freeze > requirements.txt
