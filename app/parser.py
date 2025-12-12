# import re 

# class Parser:
    
#     def __init__(self,userInput):
#         self.userInput = userInput
        

#     def get_Command(self):
#         self.userInput = self.userInput.strip()
#         userCommand = re.search(r"^[^\s]+",self.userInput)
#         userCommand = userCommand.group()
#         return userCommand

#     def getInputTokens(input):
#         userInputTokens = input.split() 
#         return userInputTokens
    
#     def get_argument(self):  
#         arg= re.search(r"^\S+\s+(.*)",self.userInput)
#         arg = arg.group(1)   
#         return arg

#     def single_quote_parser(arg):
#         single_quote = re.findall("(?<=')[^']*(?=')",arg)
#         if len(single_quote) > 1:
#             print(single_quote)
#         else: 
#             arg = re.search("(?<=')[^']*(?=')",arg)
#             arg = arg.group()
        
        