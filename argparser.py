#!usr/bin/python3

# argparser.py
# Version 1.0.0
# 1/14/23

# Written By: Mason R. Ware

# This is an argument parser to serve as a substitute for pythons argparse.
# It is also heavily influenced in architecture and naming convention by the aforementioned library.
# It works to expect user-configured arguments and, based on the user's actual cli args, 
# returns an object with boolean attributes corresponding to each user-configured arg.

from ast import List
import sys
from typing import Set


class Argument:
    name: str = ""
    help: str = ""
    param: bool = False
    description: str = ""

    def __init__(
        self, kwarg: str, help: str = "", param: bool = False, description: str = ""
    ):
        self.name = kwarg
        self.help = help
        self.param = param
        self.description = description

    def __eq__ (self, other):
        return self.name == other.name
    
    def __nq__ (self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return f"Argument: {self.name}"

class Namespace:
    def __init__(self, *args):
        for idx, item in enumerate(args):
            setattr(self, f"{idx}", item)

class ArgumentParser:
    description: str = ""
    targetFile: str = ""
    known_args: Set = set()

    def __init__(self, description: str="", target: str=""):
        self.description = description
        self.targetFile = target

    def add_argument(
        self, kwarg: str, help: str = "", param: bool = False, description: str = ""
    ):
        self.known_args.add(Argument(kwarg=kwarg, help=help, param=param, description=description))

    # check runtime arguments (user_args) against known args and create namespace
    def _create_namespace(self, user_args: List):
        true_args: Set = set()
        
        # replace each user_arg string with an argument object for comparison to known arguments
        for idx, user_arg in enumerate(user_args):
            user_args[idx] = Argument(user_arg)
        
        user_args = set(user_args)
        
        # implemented Set.Union method because union wasn't working
        for known_arg in self.known_args:
            for user_arg in user_args:
                # use built in __eq__
                if user_arg == known_arg:
                    true_args.add(known_arg)
                
        # check if there are any unknown/invalid arguments 
        invalid_args = set()
        for user_arg in user_args:
            if user_arg not in true_args:
                invalid_args.add(user_arg)

        # throw exception
        if len(invalid_args)>0:
            raise Exception(f"The following arguments are unknown/invalid: {', '.join(str(v) for v in invalid_args)}")
                    
        # TODO populate Namespace object
        # add all true arguments
        
        # add all false arguments
        
        # return created namespace object
                
        return set(user_args)
    
    def parse_args(self):
        ## TODO add text to test.py
                
        self._create_namespace(sys.argv[1:])
            
