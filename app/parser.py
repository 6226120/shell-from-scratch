 
class Parser:

    userInput 
    
    def __init__(self,userInput):
        self.userInput = userInput

    def getCommand(self):
        self.userInput = self.userInput.strip()
        userCommand = re.search(r"^[^\s]+",userInput)
        userCommand = userCommand.group()


    userInputTokens = userInput.split() 
        
    arg= re.search(r"^\S+\s+(.*)",userInput)
    arg = arg.group(1)   

    single_quote = re.findall("(?<=')[^']*(?=')",arg)
    if len(single_quote) > 1:
        print(single_quote)
    elif single_quote: 
        arg = re.search("(?<=')[^']*(?=')",arg)
        arg = arg.group()
    else: 
        argToken = userInputTokens[1:]
        arg = ' '.join(argToken) 