#!/usr/bin/env python
"""

  Simple stuff for simple devices.

"""
from modules import *
import modules
import os
import sys
import pprint 
import threading
import md5
import pickle
import code
import pprint as pp

class MasterUI(BaseUI):
    """ MasterUI """

    def __init__(self, prompt, intro):
        self.parent = self #stores a reference to the parent namespace
        BaseUI.__init__(self)
        self.prompt = self.make_prompt(prompt)
        self.intro = intro
        self.intro = """

            ...oooOOO The Internet of Things is idIOTic OOOooo...
   
"""
#        self.doc_header = ""
#        self.undoc_header = ""
        self.misc_header = ""
        self.ruler = "-"
        
    def do_dropshell(self, db):
        """
            Drop to an interactive Python shell.
        """
        try:
            code.interact("\n\nDropping to Python shell.", None, locals())
        except KeyboardInterrupt:
            print "Returning to '%s'..." % self.prompt

#    def do_another_UI(self, *args):
#       """ 
#           This is just reference code to show you how to make "nested" Cisco IOS style
#           commands using BaseUI class
#       """
#       AnotherUI("AnotherUI", "").cmdloop()

    def do_subcmdexample(self, *args):
    #This is temporary. Eventually we'll use the fancy dynamic monkeypatching technique
    #for command menus like we do for single commands in "load_module_cmds"
        """
           This is an example of how to do Cisco "IOS-style" sub command menus from modules
            Usage:
                just type "subcmdexample"
        """
        subcmdexample.SubCmdExample("SubCmdExample", "").cmdloop()

    def do_sucasaext(self, *args):
        """
            A more extended interactive submenu for exploitation of "sucasa" devices.
        """
        sucasa_ext.SuCasa("SuCasaEsMiCasa", "").cmdloop()
 
    def do_pdb(self, *args):
        """
            Drop into PDB.
        """
        import pdb; pdb.set_trace()
            
def load_module_cmds(classref):
#   Aight, this function is extremely ugly "under the hood" Python stuff. So here's
#   what's going on:
#
#   THE PROBLEM:
#      In Python, you make a directory a "package" when you add __init__.py to it
#      HOWEVER. There is a Catch22 because code inside a sub-package does not have
#      access to classes and code "higher up" in the parent directories. Also,
#      how do you statically code the loading of the module if you have no idea what
#      the module will be named?  So...
#
#   WHY WE NEED THIS FUNCTION:
#       We want a way to have modular code so that all we need to do is add a new .py
#       to the "modules" directory and then the next time you run idIOTic.py the new
#       code is usable without ANY modifications to idIOTic.py or the __init__.py in the
#       modules directory. All you do to "add new capabilities" is drop a new .py in the "modules" dir.
#       no code anywhere else in the tree needs to be added, updated, or changed. 
#       To achieve this, you run into the Catch22 mentioned in the paragraph above... So....
#
#   THE SOLUTION:
#      So this function solves this by using python introspection through the interpreter
#       via the getattr() setattr() builtin functions to dynamically SMASH objects from the modules INTO
#       the the namespace of idIOTic.py. It should be noted that this is done by 
#       "monkey patching" references to objects that were obtained via the Python 
#       introspectioni functions (getattr/setattr). Using this, all a "module" has to do is have a 
#       and a "execute()" method  and idIOTic.py will find it and make it a command
#       in the idIOTic CLI using the module file name itself as a command. All automagically.
#
#   For years I was doing a less elegant version of this.
#   (see: https://github.com/s7ephen/Ruxxer/blob/c98cfa7b82b4444dc577910f5a81d08cdec59182/older_versions/polycephaly/lib/rux_ui.py#L779
#
#   But this new technique is MUCH better/simpler. If anyone knows a better way to do this
#   please email me: stephen@xipiter.com
#   
#   TODO: Later I'd like to add support for the extensible "sub command menus" (see "AnotherUI" class)
#   in this code for an example. For now however, if you want a command "submenu" (Cisco IOS-style)
#   then you will have to edit the code here. See "subcmdexample" module as an example and the 
#   "do_subcmdexample" function in "MasterUI" as an example. "AnotherUI" is also a good example.
#
# --------------
    for mod in dir(modules):
        tmp = getattr(modules,mod)
#        print mod
       #print type(tmp)
        for needle in dir(tmp):
           # print needle
            if needle == "execute":
                print "Loading '%s' as a 'simple' idIOTic execute module..." % tmp.__name__
                try:
                    his = getattr(tmp,"execute")
                    setattr(classref, "do_"+tmp.__name__.split('.')[1], his)
                except:
                    pass
               #import pdb;pdb.set_trace() #debug
# -----------------
#    import modules 
#    for mod in dir(modules):
#        tmp = getattr(modules,mod)
#        print mod
        #print type(tmp)
#        for needle in dir(tmp):
#            if needle == "DoSomething":
#                #print "FOUND DoSomething in a MODULE!!! It must be ours."
#                #print ">>>",tmp.__name__
#                his = getattr(tmp,"DoSomething")
#                setattr(classref, tmp.__name__.split('.')[1]+"_obj", his())
#                newobj_in_classref=getattr(classref, tmp.__name__.split('.')[1]+"_obj")
#                try:
#                    execute_of_newobj_in_classref=getattr(newobj_in_classref,"execute")
#                except:
#                    print "Error finding 'execute' method in DoSomething class of '%s'" % tmp.__name__
#                setattr(classref, "do_"+tmp.__name__.split('.')[1], execute_of_newobj_in_classref) 
                #import pdb;pdb.set_trace() #debug

if __name__ == '__main__':
    #import pdb;pdb.set_trace()
    ui_classref = MasterUI
    load_module_cmds(ui_classref) #this dynamically patches new commands from modules into
                                  #into the class for MasterUI. See load_module_cmd comments for info.
    ui_classref("idIOTic", """""").cmdloop()
else:
    print __doc__
