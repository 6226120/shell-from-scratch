import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        userInput = input("$ ")
        if "echo" in userInput:
            userInput = userInput.replace("echo", "")
            sys.stdout.write(f"{userInput}")

        

    pass


if __name__ == "__main__":
    main()
