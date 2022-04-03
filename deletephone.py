import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

cucm = sys.argv[1]
cmuser = sys.argv[2]
cmpass = sys.argv[3]
mac = sys.argv[4]
version = sys.argv[5]


def remove_phone(cucm, cmuser, cmpass,mac, version):
    xml = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/'''+version+'''">
             <soapenv:Header/>
             <soapenv:Body>
             <ns:removePhone sequence="?">
             <name>'''+mac+'''</name>
             </ns:removePhone>
             </soapenv:Body>
             </soapenv:Envelope>'''

    headers = {'Content-type': 'text/xml', 'SOAPAction': 'CUCM:DB ver='+version+' removePhone'}
    resp = requests.post('https://' + cucm + ':8443/axl/', data=xml,
                                headers=headers, auth=HTTPBasicAuth(cmuser, cmpass), verify=False)

    if resp.status_code == 200:
        result = 'Phone: {0} successfully deleted'.format(mac)
        return result
    elif resp.status_code == 500:
        result = 'Phone: {0} not found'.format(mac)
        return result
    else:
        result = 'Phone could not be deleted'
        return result

      
      
