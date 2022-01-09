# this while with else-if will run a command of your choice
import os
prompt = "cmd => "
while True:
    command = 'notepad.exe'
    if command == "exit!":
        break
    else:
        os.system(command)