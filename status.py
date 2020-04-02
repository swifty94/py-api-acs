import os
import requests
from xml.dom import minidom
from __main__ import sn

def api_call():	
	api_url="http://demo.friendly-tech.com/FTACSWS/ACSWS.asmx?wsdl"
	headers = {'content-type': 'text/xml'}
	body = """
	<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:fri="http://www.friendly-tech.com">
	   <soapenv:Header/>
	   <soapenv:Body>
	      <fri:FTCPEStatus>
			<fri:devicesn>{}</fri:devicesn>
	      </fri:FTCPEStatus>
	   </soapenv:Body>
	  </soapenv:Envelope>
	""".format(sn)

	response = requests.post(api_url,data=body,headers=headers)
	file = open("s_response.xml", "wb")
	file.write(response.content)
	file.close()

def parse():
	xml = minidom.parse('s_response.xml')
	code = xml.getElementsByTagName('ErrorCode')
	code_result = int(code[0].firstChild.data)
	if code_result == 201:
		message = xml.getElementsByTagName('Message')
		message_result = (message[0].firstChild.data)
		print(message_result)
	else:
		isOnline = xml.getElementsByTagName('Online')
		isOnline_result = (isOnline[0].firstChild.data)
		print('CPE online - ', isOnline_result)

	os.remove("s_response.xml")

def cpe_status():
	api_call()
	parse()

