import sys


def main():

    while True:
        userInput = input("$ ")
        
        # We want to tokenize the input so we can differentiate the command from the args
        userInputTokens = userInput.split()
        command = userInputTokens[0]
        arg = userInputTokens[1:]

        # We are checking to see what the firs token is and responding accordingly 
        if "echo" == command:
            sys.stdout.write(f"{arg}\n")
        elif "exit" == command:
            sys.exit()
        else:
            command_not_found(userInput)
    

def command_not_found(userInput):
    sys.stdout.write(f"{userInput}: command not found \n")


if __name__ == "__main__":
    main()
