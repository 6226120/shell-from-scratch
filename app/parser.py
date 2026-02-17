import re 

class Parser:
    
    
    
    def __init__(self,userInput):
        self.userInput = userInput
    
    def has_quote(self,arg):
        for char in arg:
            if char == "'":
                return True
            return False 

    def get_Command(self):
        self.userInput = self.userInput.strip()
        userCommand = re.search(r"^[^\s]+",self.userInput)
        userCommand = userCommand.group()
        return userCommand

    def get_input_tokens(self):
        userInputTokens = self.userInput.split() 
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
    
    def has_quote(self):
        for char in self.userInput:
            if char == "'":
                return True
            
        return False
    
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
                
                if i == len(arg_token) - 1:
                    final_arg.append(quote_arg)
                    final_arg = ''.join(final_arg)
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
                continue
            
            if quote_counter != 0:
                quote_arg +=char
        return final_arg
