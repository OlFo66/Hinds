import sys
import os
import requests
import subprocess
import base64
from itertools import batched

def sendMessage(url, count='', chrunk='', messageToSend=''):
    if count:
        content = str(count)
    elif chrunk:
        content = str(chrunk)
    elif messageToSend:
        content = str(messageToSend)
    else:
        return False

    payload = {'content': str(content)
               }
    response = requests.post(url, json=payload)
    #print("%s - %s" %(response.status_code, response.text))
def launchCommand(command):
    result = subprocess.run(args=command,
                            universal_newlines=True,
                            stdout=subprocess.PIPE)
    return(result.returncode, result.stdout)
def sendChrunkedMessage(url, dataToChrunk):
    size = int((len(dataToChrunk)/2000)+1)
    sendMessage(url, count=size)

    chrunk = list(batched(str(dataToChrunk), 2000))
    for i in range(0, len(chrunk)):
        string = ''.join(chrunk[i])
        sendMessage(url, chrunk=string)
def encodeFile(providedFile):
    with open(providedFile, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    my_string = my_string.decode('utf-8')
    return my_string
if __name__ == '__main__':
    try:
        with open(os.path.dirname(sys.argv[0])+'/.webhook') as file:
            webHook = file.read()
    except:
        sys.exit(1)

    if len(sys.argv) < 3 or (sys.argv[1] != "-c" and sys.argv[1] != "-f"):
        sys.exit(1)
    elif sys.argv[1] == "-c":
        commandToLaunch = []
        for i in range(2, len(sys.argv)):
            commandToLaunch.append(sys.argv[i])
        returncode, stdout = launchCommand(commandToLaunch)
        if returncode == 0:
            sendMessage(webHook, messageToSend=stdout)
    elif sys.argv[1] == "-f":
        for i in range(2, len(sys.argv)):
            encodedFile = encodeFile(sys.argv[i])
            sendChrunkedMessage(webHook, encodedFile)