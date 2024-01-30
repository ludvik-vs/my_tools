import subprocess
import re

with open('requirements.txt', 'r') as file:
    packages = [line.strip() for line in file]

for package in packages:
    subprocess.call(['pip', 'uninstall', '-y', package])


# pip freeze > requirements.txt
