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
	      <fri:FTGetDeviceInfo>
			<fri:devicesn>{}</fri:devicesn>
	      </fri:FTGetDeviceInfo>
	   </soapenv:Body>
	  </soapenv:Envelope>
	""".format(sn)

	response = requests.post(api_url,data=body,headers=headers)
	file = open("di_response.xml", "wb")
	file.write(response.content)
	file.close()

def parse():
	xml = minidom.parse('di_response.xml')
	code = xml.getElementsByTagName('ErrorCode')
	code_result = (code[0].firstChild.data)
	if int(code_result) == 201:
		message = xml.getElementsByTagName('Message')
		message_result = (message[0].firstChild.data)
		print(message_result)
	else:
		tags = ["Id", "Serial", "RootObject", "ProductClassId", "ManufacturerName", "ModelName", "Created", "Updated", "FirmwareVersion"]
		tags_values = []
		for x in tags:
			tag = xml.getElementsByTagName(x)
			value = (tag[0].firstChild.data)
			print(x, "---",value)
	
	os.remove("di_response.xml")


def cpe_info():
	api_call()
	parse()
