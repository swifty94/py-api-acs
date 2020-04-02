print('Please specify the Serial Number of the CPE')
sn = input()
print('\nChose desired API method to use')
print('They are:')
api_methods = """
status           [use -  status|st|s  ]
device_info      [use -  info|di|i    ]
create backup    [use -  backup|bc|b  ]
"""
print(api_methods)
api_input = input()

from status import cpe_status
from info import cpe_info
from backup import cpe_backup

def main():
	if api_input == 'status' or api_input == 'st' or api_input == 's':
		cpe_status()
		exit()
	elif api_input == 'info' or api_input == 'di' or api_input == 'i':
		cpe_info()
		exit()
	elif api_input == 'backup' or api_input == 'bc' or api_input == 'b':
		cpe_backup()
		exit()
	else:
		print('Unknown or Illegal API method used')
		exit()

if __name__ == '__main__':
	main()