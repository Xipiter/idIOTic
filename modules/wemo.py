#! /usr/bin/env python

#modified for python
# original curl request in bash by: rich@netmagi.com
#from http://moderntoil.com/file_attachments/wemo_control.sh

def execute(self,args):
    """wemo ipaddress port command\nex: wemo 10.22.22.1 49152 on\nex: wemo 10.22.22.1 49152 off"""
    import pdb; pdb.set_trace()
#    arglist=[]
#    arglist=args

#    ip=args[1][1]
#    port=args[1][2]
#    state=args[1][3]
#    print args

    import httplib
    httplib.HTTPConnection._http_vsn = 10
    httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

    if(state == "on"):
        SoapMessage = """<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>1</BinaryState></u:SetBinaryState></s:Body></s:Envelope>"""
        url=ip
        suburl="/upnp/control/basicevent1"

        webservice = httplib.HTTP(url,port)
        webservice.putrequest("POST",suburl)
        webservice.putheader("Host", url.strip("http://")+port)
        webservice.putheader("Content-type", "text/xml; charset=\"utf-8\"")
        webservice.putheader("SOAPACTION", "\"urn:Belkin:service:basicevent:1#SetBinaryState\"")
        webservice.putheader("Content-Length", "%d" % len(SoapMessage))
        webservice.endheaders()
        webservice.send(SoapMessage)

    elif(state == "off"):
        SoapMessage = """<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>0</BinaryState></u:SetBinaryState></s:Body></s:Envelope>"""
        url=ip
        suburl="/upnp/control/basicevent1"

        webservice = httplib.HTTP(url,port)
        webservice.putrequest("POST",suburl)
        webservice.putheader("Host", url.strip("http://")+port)
        webservice.putheader("Content-type", "text/xml; charset=\"utf-8\"")
        webservice.putheader("SOAPACTION", "\"urn:Belkin:service:basicevent:1#SetBinaryState\"")
        webservice.putheader("Content-Length", "%d" % len(SoapMessage))
        webservice.endheaders()
        webservice.send(SoapMessage)
