id-IOT-ic Modules:
=====

There are two kinds of modules:
## Basic Modules
Basic Modules should import nothing and just have an `execute()` function. When idiotic next loads, whatever you named the file (i.e. newmod.py) will become the command `newmod` in idIOTic. When the user executes the command `newmod` from idIOTic, the `execute()` function in `newmod` will run with any arguments the user provided passed into your execute function. This happens automatically and does not require editing *ANY* other code in the idIOTic source tree. (If you are curious how this is done, see `load_module_cmds()` in idIOTic.py

## SubMenu Command Modules
The other kind of module is actually a subcommand menu. for a template example of this please see subcommandexample.py. You'll also need to add a command to idIOTic to invoke the submenu. Eventually you won't and the same method we use to dynamically load "Basic Modules" we'll apply to the SubMenu modules. 
Here is a simple terminal trace to explain:
```
tachiro:idIOTic s7$ cat modules/subcmdexample.py
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

tachiro:idIOTic s7$ ./idIOTic.py 
Loading 'modules.sucasa' as a idIOTic module...
Loading 'modules.wemo' as a idIOTic module...


            ...oooOOO The Internet of Things is idIOTic OOOooo...
   

idIOTic.>> help

Documented commands (type help <topic>):
----------------------------------------
EOF  dropshell  exit  help  hist  pdb  subcmdexample  sucasa  wemo

idIOTic.>> help subcmdexample

           This is an example of how to do Cisco "IOS-style" sub command menus from modules
            Usage:
                just type "subcmdexample"
        
idIOTic.>> subcmdexample
idIOTic.SubCmdExample.>> help

Documented commands (type help <topic>):
----------------------------------------
EOF  dotheotherthing  dothething  exit  help  hist  thing

idIOTic.SubCmdExample.>> help dothething

            To do the thing, just enter the command "dothething"
idIOTic.SubCmdExample.>> dothething
I just did the thing. Underwhelming huh?
args: 
idIOTic.SubCmdExample.>> dothething with a bunch of args
I just did the thing. Underwhelming huh?
args: with a bunch of args
idIOTic.SubCmdExample.>> dotheotherthing
I just did the OTHER thing. Let's do t again sometime!
args: 
idIOTic.SubCmdExample.>> dotheotherthing with a bunch of args
I just did the OTHER thing. Let's do t again sometime!
args: with a bunch of args
idIOTic.SubCmdExample.>> exit

Exiting...
idIOTic.>> help

Documented commands (type help <topic>):
----------------------------------------
EOF  dropshell  exit  help  hist  pdb  subcmdexample  sucasa  wemo

idIOTic.>> 
``` 
