import sys
import os


def main():

    command_list = {
        "echo": "echo is a shell builtin",
        "exit": "exit is a shell builtin",
        "type": "type is a shell builtin"
    }


    while True:
        userInput = input("$ ")
        # if "invalid" in userInput:
        #     print(userInput)

        if userInput[0] == "":
            continue
        if userInput[0] == " ":
            userInput.strip()
        
        userInputTokens = userInput.split()
        userCommand = userInputTokens[0]
        argToken = userInputTokens[1:]
        arg = ' '.join(argToken)    


        handle_commands(userCommand,arg,command_list,userInput)
    

def command_not_found(userInput):
    sys.stdout.write(f"{userInput}: command not found \n")


def handle_commands(userCommand,arg,command_list,userInput,file_path):
    if is_echo(userCommand):
        sys.stdout.write(f"{arg}\n")
    elif is_exit(userCommand):
        sys.exit()
    elif is_type(userCommand):
        file_path = file_path_for_cmd(arg)
    
        if arg in command_list:
            sys.stdout.write(f"{command_list[arg]}\n")
        else:
            if is_executable_file(file_path):
                sys.stdout.write(f"{arg} is {file_path}\n")
            else:
                sys.stdout.write(f"{arg} not found\n")

    else: 
        command_not_found(userInput)


def file_path_for_cmd(userCommand):
    for path in paths():
        path_for_file= os.path.join(path,userCommand)
        if is_executable_file(path_for_file):
            return path_for_file
    return None
        

def is_executable_file(file_path_for_cmd):
    return os.path.isfile(file_path_for_cmd) and os.access(file_path_for_cmd,os.X_OK)


def paths():
    paths = os.environ['PATH'].split(os.pathsep)
    return paths


def is_echo(userCommand):
    return userCommand == "echo"
        

def is_exit(userCommand):
    return userCommand == "exit"
       
    
def is_type(userCommand):
    return userCommand == "type"

if __name__ == "__main__":
    main()
