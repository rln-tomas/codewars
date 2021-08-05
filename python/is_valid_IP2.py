import re
def is_valid_IP(strng):
	return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))

print(is_valid_IP('0192.144.0.255'))
