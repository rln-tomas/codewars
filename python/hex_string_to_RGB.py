import textwrap

def hex_string_to_RGB(hex_string):
	hexa = textwrap.wrap(hex_string.split('#')[1],2)
	return {k:int(h,16) for (k,h) in zip('rgb',hexa)} 
