import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        userInput = input("$ ")
        if "echo" in userInput:
            userInput = userInput.replace("echo ", "")
            sys.stdout.write(f"{userInput} \n")
        elif "exit" in userInput:
            sys.exit()
        else:
            sys.stdout.write(f"{userInput}: command not found \n")
        

    pass


if __name__ == "__main__":
    main()
