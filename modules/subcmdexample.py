"""
Sub Command Example.

This is an idIOTic submenu command example. 
1. You create a class that inherits from "AnotherUI"
2. Give that same class a docstring (this will be the 'help' in the CLI)
3. Any method of that class that starts with "do_" will be automatically
    a command in the submenu. 
4. The docstring of the method will be the help for the command.
5. You'll have to edit idIOTic.py adding a command to the toplevel idIOTic menu (see "do_subcmdexample()")
    in idIOTic.py for an example.
6. That's it.

  Note: eventually we will use the "automatic import" technique that we use for basic "execute()" style
        modules, so that you dont have to modify idIOTic.py to have a command to invoke...it will
        be done automatically...but for now I am being lazy, so this is how it is done.

"""
from mods import * #Any modules that plan to be idIOTic submenu command need this line

class SubCmdExample(AnotherUI):
    """
    This prints as the help string of the command submenu in idIOTic
    """
    def do_dothething(self,args): 
        """
            To do the thing, just enter the command "dothething"
        """
        print "I just did the thing. Underwhelming huh?"
        print "args: %s" % args
    
    def do_dotheotherthing(self, args):
        """
            To do the OTHER thing, just enter the command "dotheotherthing"
        """
        print "I just did the OTHER thing. Let's do t again sometime!"
        print "args: %s" % args

