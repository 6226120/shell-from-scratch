import sys


def main():

    commandList = {
        "echo": "echo is a shell builtin",
        "exit": "exist is a shell builtin",
        "type": "type is a shell bultin"
    }

    while True:
        userInput = input("$ ")
        
        # We want to tokenize the input so we can differentiate the command from the args
        userInputTokens = userInput.split()
        userCommand = userInputTokens[0]
        argToken = userInputTokens[1:]
        arg = ' '.join(argToken)

        handle_commands(userCommand,arg,commandList,userInput)
    

def command_not_found(userInput):
    sys.stdout.write(f"{userInput}: command not found \n")


def handle_commands(userCommand,arg,commandList,userInput):
    if is_echo(userCommand,arg):
        sys.stdout.write(f"{arg}\n")
    elif is_exit(userCommand):
        sys.exit()
    elif is_type(userCommand):
        if arg in commandList:
            sys.stdout.write(f"{commandList[arg]}\n")
        else:
            sys.stdout.write(f"{arg}: not found\n")
    else: 
        command_not_found(userInput)


def is_echo(userCommand):
    if userCommand == "echo":
        return True
    return False
        

def is_exit(userCommand):
    if userCommand == "exit":
        return True
    return False

    
def is_type(userCommand):
    if userCommand == "type":
        return True
    return False

if __name__ == "__main__":
    main()
