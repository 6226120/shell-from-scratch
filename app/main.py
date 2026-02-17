import sys
import os
import subprocess
import re
from parser import Parser


def main():
      
    command_list = {
        "echo": "echo is a shell builtin",
        "exit": "exit is a shell builtin",
        "type": "type is a shell builtin",
        "pwd": "pwd is a shell builtin",
        "cd": "cd is a shell builtin"
    }
    while True:
        userInput = input("$ ")
        p = Parser(userInput)
        userCommand = p.get_Command()
        userInputTokens = p.get_input_tokens()
        arg= p.get_argument()

        argToken = userInputTokens[1:]
        arg = ' '.join(argToken) 

        handle_commands(userCommand,arg,command_list,userInputTokens,p)
    

def command_not_found(userInput):
    sys.stdout.write(f"{userInput}: command not found \n")


def handle_commands(userCommand,arg,command_list,userInputTokens,p):
    if userCommand == "echo":
        if p.has_quote():
             sys.stdout.write(f"{p.single_quote_parser(arg)}\n")
        else:
            sys.stdout.write(f"{arg}\n")
    elif userCommand == "exit":
        sys.exit()
    elif userCommand == "type":
        file_path_for_cmd = file_path(arg)
        if arg in command_list:
            sys.stdout.write(f"{command_list[arg]}\n")
        elif file_path_for_cmd == None:
            sys.stdout.write(f"{arg} not found\n")
        else:
            sys.stdout.write(f"{arg} is {file_path_for_cmd}\n")
    elif userCommand == "pwd":
        sys.stdout.write(f"{os.getcwd()}\n")
    elif userCommand == "cd":
        command_cd(arg)
    else: 
        run_program(userCommand,userInputTokens)


def single_quote(arg):
    re.findall("(?<=')[^']*(?=')",arg)

def command_cd(arg):
    if arg == "~":
            os.chdir(os.path.expanduser("~"))
    elif os.path.splitroot(arg)[1] == "": 
        if current_or_parent(arg) == "current":
            try:
                os.chdir(arg)
            except OSError:
                sys.stdout.write(f"cd: {arg}: No such file or directory\n")
        elif type(current_or_parent(arg)) is int:
            for _ in range(current_or_parent(arg)):
                os.chdir("..")
        else: 
            sys.stdout.write(f"cd: {arg}: No such file or directory (shouldn't get here)\n")
    else : 
        try:
            os.chdir(arg)
        except OSError:
            sys.stdout.write(f"cd: {arg}: No such file or directory\n")

def file_path(userCommand):
    for path in paths():
        path_for_file= os.path.join(path,userCommand)
        if is_executable_file(path_for_file):
            return path_for_file
    return None
        
def current_or_parent(arg):
    path_split = arg.split("/")
    number_of_dots = 0
    if path_split[0] == ".":
        return "current"
    elif path_split[0] == "..": 
        for amount in path_split:
            if amount == "..":
                number_of_dots += 1
        return number_of_dots
    else: 
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

def help():
    sys.stdout.write("GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)\nThese shell commands are defined internally.  Type `help' to see this list.\nType `help name' to find out more about the function `name'.\nUse `info bash' to find out more about the shell in general.\nUse `man -k' or `info' to find out more about commands not in this list.")
    sys.stdout.write("A star (*) next to a name means that the command is disabled.")
    sys.stdout.write(""" JOB_SPEC [&]                       (( expression ))
 . filename [arguments]             :
 [ arg... ]                         [[ expression ]]
 alias [-p] [name[=value] ... ]     bg [job_spec ...]
 bind [-lpvsPVS] [-m keymap] [-f fi break [n]
 builtin [shell-builtin [arg ...]]  caller [EXPR]
 case WORD in [PATTERN [| PATTERN]. cd [-L|-P] [dir]
 command [-pVv] command [arg ...]   compgen [-abcdefgjksuv] [-o option
 complete [-abcdefgjksuv] [-pr] [-o continue [n]
 declare [-afFirtx] [-p] [name[=val dirs [-clpv] [+N] [-N]
 disown [-h] [-ar] [jobspec ...]    echo [-neE] [arg ...]
 enable [-pnds] [-a] [-f filename]  eval [arg ...]
 exec [-cl] [-a name] file [redirec exit [n]
 export [-nf] [name[=value] ...] or false
 fc [-e ename] [-nlr] [first] [last fg [job_spec]
 for NAME [in WORDS ... ;] do COMMA for (( exp1; exp2; exp3 )); do COM
 function NAME { COMMANDS ; } or NA getopts optstring name [arg]
 hash [-lr] [-p pathname] [-dt] [na help [-s] [pattern ...]
 history [-c] [-d offset] [n] or hi if COMMANDS; then COMMANDS; [ elif
 jobs [-lnprs] [jobspec ...] or job kill [-s sigspec | -n signum | -si
 let arg [arg ...]                  local name[=value] ...
 logout                             popd [+N | -N] [-n]
 printf [-v var] format [arguments] pushd [dir | +N | -N] [-n]
 pwd [-LP]                          read [-ers] [-u fd] [-t timeout] [
 readonly [-af] [name[=value] ...]  return [n]
 select NAME [in WORDS ... ;] do CO set [--abefhkmnptuvxBCHP] [-o opti
 shift [n]                          shopt [-pqsu] [-o long-option] opt
 source filename [arguments]        suspend [-f]
 test [expr]                        time [-p] PIPELINE
 times                              trap [-lp] [arg signal_spec ...]
 true                               type [-afptP] name [name ...]
 typeset [-afFirtx] [-p] name[=valu ulimit [-SHacdfilmnpqstuvx] [limit
 umask [-p] [-S] [mode]             unalias [-a] name [name ...]
 unset [-f] [-v] [name ...]         until COMMANDS; do COMMANDS; done
 variables - Some variable names an wait [n]
 while COMMANDS; do COMMANDS; done  { COMMANDS ; }
")""")
                     
        
if __name__ == "__main__":
    main()
