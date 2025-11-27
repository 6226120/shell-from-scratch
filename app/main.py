import sys
import os
import subprocess


def main():

    command_list = {
        "echo": "echo is a shell builtin",
        "exit": "exit is a shell builtin",
        "type": "type is a shell builtin"
    }


    while True:
        userInput = input("$ ")

        if userInput[0] == "":
            continue
        if userInput[0] == " ":
            userInput.strip()
        
        userInputTokens = userInput.split()
        if len(userInputTokens) > 1:
            userCommand = userInputTokens[0]
            argToken = userInputTokens[1:]
            arg = ' '.join(argToken)   
        else:
            userCommand = userInputTokens[0]

        handle_commands(userCommand,arg,command_list,userInputTokens)
    

def command_not_found(userInput):
    sys.stdout.write(f"{userInput}: command not found \n")


def handle_commands(userCommand,arg,command_list,userInputTokens):
    if is_echo(userCommand):
        sys.stdout.write(f"{arg}\n")
    elif is_exit(userCommand):
        sys.exit()
    elif is_type(userCommand):
        file_path_for_cmd = file_path(arg)
        if arg in command_list:
            sys.stdout.write(f"{command_list[arg]}\n")
        elif file_path_for_cmd == None:
            sys.stdout.write(f"{arg} not found\n")
        else:
                sys.stdout.write(f"{arg} is {file_path_for_cmd}\n")
    else: 
        run_program(userCommand,userInputTokens)


def file_path(userCommand):
    for path in paths():
        path_for_file= os.path.join(path,userCommand)
        if is_executable_file(path_for_file):
            return path_for_file
    return None
        

def is_executable_file(file_path):
    return os.path.isfile(file_path) and os.access(file_path,os.X_OK)

def run_program(cmd,userInputTokens):
    program_file_path = file_path(cmd)
    if program_file_path != None:
        program = subprocess.run(userInputTokens,capture_output=True, text=True)
        if program.returncode  == 0:
            sys.stdout.write(program.stdout)
        else:
            sys.stdout.write(program.stderr)
        
    else: 
        command_not_found(cmd)


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
