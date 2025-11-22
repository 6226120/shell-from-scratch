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
        if userInput[0] == "" or userInput[0] == " ":
            continue
        
        userInputTokens = userInput.split()
        userCommand = userInputTokens[0]
        argToken = userInputTokens[1:]
        arg = ' '.join(argToken)

        handle_commands(userCommand,arg,command_list,userInput)
    

def command_not_found(userInput):
    sys.stdout.write(f"{userInput}: command not found \n")


def handle_commands(userCommand,arg,command_list,userInput):
    if is_echo(userCommand):
        sys.stdout.write(f"{arg}\n")
    elif is_exit(userCommand):
        sys.exit()
    elif is_type(userCommand):
        if arg in command_list:
            sys.stdout.write(f"{command_list[arg]}\n")
        else:
            search_for_path(arg)
    else: 
        command_not_found(userInput)


def search_for_path(userCommand):
    for paths in separate_directories():
        file_path= os.path.join(paths,userCommand)
        if os.path.isfile(file_path) and os.access(file_path,os.X_OK):
            sys.stdout.write(f"{userCommand} is {file_path}\n")
            return 
    
    return f"{userCommand} not found\n"
        

    
def separate_directories():
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
