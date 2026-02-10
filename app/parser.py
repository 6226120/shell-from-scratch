import re 

class Parser:
    
    def __init__(self,userInput):
        self.userInput = userInput
        

    def get_Command(self):
        self.userInput = self.userInput.strip()
        userCommand = re.search(r"^[^\s]+",self.userInput)
        userCommand = userCommand.group()
        return userCommand

    def get_input_tokens(input):
        userInputTokens = input.split() 
        return userInputTokens
    
    def get_argument(self):  
        arg= re.search(r"^\S+\s+(.*)",self.userInput)
        arg = arg.group(1)   
        return arg

    def tokenizer(self,arg):
        token = list(arg) 
        return token
    
    def value_is_even_or_odd(self,value):
        if value % 2 != 0:
            return False
        return True
    
    def single_quote_parser(self,arg):
        arg_token = self.tokenizer(arg)
        quote_counter = 0
        quote_arg = ''

        final_arg = []
        for i,char in enumerate(arg_token):
            if char == "'":
                quote_counter += 1
                if quote_counter == 1:
                    continue
                if self.value_is_even_or_odd(quote_counter):
                    final_arg.append(quote_arg)
                    quote_arg = ''
                    continue
                else:
                    if str.isspace(quote_arg):
                        final_arg.append(" ")
                        quote_arg = ''
                        continue 
                    elif quote_arg == '':
                        continue
                    else:  
                        " ".join(quote_arg.split())
                        final_arg.append(quote_arg)
                        quote_arg = ''
                        continue
                    
            if i == len(arg_token) - 1:
                quote_arg +=char
                final_arg.append(quote_arg)
                final_arg = ''.join(final_arg)
                print(final_arg)
                continue
            
            if quote_counter != 0:
                quote_arg +=char
                             


    
userInput = input("$ ")
p = Parser(userInput)
p.single_quote_parser("'shell     example' 'hello'      'script' world''test")