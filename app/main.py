import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        userInput = input("$ ")
        sys.exit() if userInput == "exit 0" else sys.stdout.write(f"{userInput}: command not found \n")
        

    pass


if __name__ == "__main__":
    main()
