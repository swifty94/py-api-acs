import os
import requests
from xml.dom import minidom
from __main__ import sn

def apiCall():	
	api_url="http://demo.friendly-tech.com/FTACSWS/ACSWS.asmx?wsdl"
	headers = {'content-type': 'text/xml'}
	body = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:fri="http://www.friendly-tech.com">
        <soapenv:Header/>
        <soapenv:Body>
            <fri:FTBackup>                
                <fri:devicesn>{}</fri:devicesn>
                <fri:push>1</fri:push>                          
            </fri:FTBackup>
        </soapenv:Body>
        </soapenv:Envelope>
	""".format(sn)

	response = requests.post(api_url,data=body,headers=headers)
	file = open("b_response.xml", "wb")
	file.write(response.content)
	file.close()

def parse():
	xml = minidom.parse('b_response.xml')
	code = xml.getElementsByTagName('ErrorCode')
	code_result = int(code[0].firstChild.data)
	if code_result == 201:
		message = xml.getElementsByTagName('Message')
		message_result = (message[0].firstChild.data)
		print(message_result)
	elif code_result == 100:
		print('Backup has been created')

	os.remove("b_response.xml")

def cpe_backup():
    apiCall()
    parse()