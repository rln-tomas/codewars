def rgb(r,g,b):
    res = str()
    for i in [r, g, b]: 
        print(i)
        if (i < 0):
            i = "00"
        else:
            if (i > 255): 
                i = "ff"
            else: 
                i = format(int(hex(i), 16), 'x')
        if len(i) == 1: 
            i = "0" + i
        print(i)
        res = res + i.upper()
    return res
    
"""I prefer this version: 
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""

