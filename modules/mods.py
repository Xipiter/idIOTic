from cmd import *
import pprint

class BaseUI(Cmd):
    """

        The base User Interface object.

    """
    path =[] #this is how we fake the "path" of commands.
    name = ""

    def __init__(self):
        Cmd.__init__(self)

    def make_prompt(self, name=""):
        test_str = self.get_prompt()
        if test_str.endswith(name+"."):
            test_str += ">> "
            return(test_str)
        #the above is a little hack to test if the path
        #is already set for us, incase this object instance
        #is actually getting reused under the hood.
        self.path.append(name)
        tmp_name = ""
        tmp_name = self.get_prompt()
        tmp_name += ">> "
        return(tmp_name)

    def get_prompt(self):
        tmp_name = ""
        for x in self.path: #iterate through object heirarchy
            tmp_name += (x + ".")
        return tmp_name

    def do_help(self, args):
        """
           Getting help on "help" is kinda retarded dont you think?
        """
        #The only reason to define this method is for the help text in the
        #docstring   
        Cmd.do_help(self, args)

    def do_hist(self, args):
        """

            Display command history. 

        """
#        n = 0
#        for i in self._hist:
#            print "%d: %s" % (n, i)
#            n+=1 
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self._hist)

    def emptyline(self):
        """
            Do nothing on empty input line
        """
        pass
    def preloop(self):
        """
            Initialization before prompting user for commands.
            Despite the claims in the Cmd documentaion, Cmd.preloop() is not a
            stub.
        """
        Cmd.preloop(self)   ## sets up command completion
        self._hist    = []      ## No history yet
        self._locals  = {}      ## Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """
            Take care of any unfinished business.
            Despite the claims in the Cmd documentaion, Cmd.postloop() is not a
            stub.
        """
        Cmd.postloop(self)   ## Clean up command completion
        print "\nExiting..."

    def precmd(self, line):
        """ 
            This method is called after the line has been input but before
            it has been interpreted. If you want to modifdy the input line
            before execution (for example, variable substitution) do it here.

        """
        self._hist+=[line.strip()]
        return line

    def postcmd(self, stop, line):
        """
            If you want to stop the console, return something that evaluates to
            true. If you want to do some post command processing, do it here.

        """
        return stop

    def default(self, line):
        """
            Called on an input line when the command prefix is not recognized.
            In that case we execute the line as Python code.

        """
        try:
            exec(line) in self._locals, self._globals
        except Exception, e:
            #print e.__class__, ":", e
            print "\nBad command (%s)'" % (e)

    def do_exit(self, args):
        """
            Exit/Quit. 
        """
        return -1

    do_EOF = do_exit

class AnotherUI(BaseUI):
    """ This is Another UI example of nested Cisco IOS style command menu
    for how to use it, see do_another_ui() inside MasterUI class. """
    def __init__(self, prompt, intro):
        BaseUI.__init__(self)
        self.prompt = self.make_prompt(prompt)
        self.intro = intro

#        self.doc_header = ""
#        self.undoc_header = ""
        self.misc_header = ""
        self.ruler = "-" 
    
    def do_thing(self, *args):
        """ Do the thing """
        print "thing"
