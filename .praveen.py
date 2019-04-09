import json

def get_dict():
	output = """	input module:  syslog
	    interface: ether1
	    proto:     tcp
	    port:      514
	    interface: ether1
	    proto:     udp
	    port:      514

	input module:  jsondfsf
	    interface: ether1
	    proto:     tcp
	    port:      515
	    interface: ether1
	    proto:     udp
	    port:      515
	input module:  syslogfdsf
	    interface: ether1
	    proto:     tcp
	    port:      514
	    interface: ether1
	    proto:     udp
	    port:      514

	input module:  jsonfsfs
	    interface: ether1
	    proto:     tcp
	    port:      515
	    interface: ether1
	    proto:     udp
	    port:      515
	input module:  syslogfsfs
	    interface: ether1
	    proto:     tcp
	    port:      514
	    interface: ether1
	    proto:     udp
	    port:      514

	input module:  jsonfsfs
	    interface: ether1
	    proto:     tcp
	    port:      515
	    interface: ether1
	    proto:     udp
	    port:      515
	    """


	output = filter(lambda k: bool(k.strip()), output.splitlines())

	index = 0
	result = dict()

	while index < len(output):

		while 'input module' not in output[index]:
			index += 1

		_, input_module = map(lambda k: k.strip(), output[index].split(':'))
		result[input_module] = list()
		temp_dict = dict()
		index += 1

		values = set()

		while index < len(output) and 'input module' not in output[index]:

			key, value = map(lambda k: k.strip(), output[index].split(':'))
			predef_values = set(['interface', 'proto', 'port'])

			values.add(key)
			temp_dict[key] = value
			if values == predef_values:
				result[input_module].append(temp_dict)
				values.clear()
				temp_dict = dict()

			index += 1

	return result

print json.dumps(get_dict(), indent=4)