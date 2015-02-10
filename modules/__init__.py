import os,sys,inspect
global MODULES
MODULES = {}
from modules.mods import *

for file in os.listdir(__path__[0]):
    path = os.path.join(__path__[0], file)
    if os.path.splitext(path)[1].lower() == ".py":
        modname = inspect.getmodulename(file)
        if modname != '__init__':
            if not modname in MODULES:
                MODULES[modname] = path
                #print "Loaded Adapter: %s at '%s'" % (modname, path)
#                print "Loaded Module: %s" % (modname)   
#                import pdb;pdb.set_trace()
                blah = __import__("modules."+modname) #THIS DIR MUST BE NAMED "modules"
                __import__("modules."+modname, globals(), locals(), ['*']) # equal to: "from modname import *"
#                import pdb;pdb.set_trace()
#            if modname and modname not in modname.__modules__:
#                __modules__.append(modname)
#                __import__("modules."+modname) #THIS DIR MUST BE NAMED "modules"
#                print "Successfully loaded PYTHON module: %s" % file
#                time.sleep(1)
sys.stdout.flush()

