# this while with else-if will hog resources
import os
prompt = "cmd => "
while True:
    command = input(prompt)
    if command == "exit!":
        break
    else:
        os.system(command)