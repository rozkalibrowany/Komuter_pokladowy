import colorsys

def temp_to_rgb(temperature):
    r = 0
    g = 0
    b = 0

    if temperature <= 127:
        r = temperature*2
        g = 255
    else:
        r = 255
        g = (255 - temperature)*2

    return (r,g,b)

def temp_to_rgb_blue(temperature):
    r = 0
    g = 0
    b = 0

##    if temperature <= 127:
##          g = temperature*2
##          b = 255 - g
##
##    else:
##          r = (temperature-128)*2
##          g = 255 - r


    if temperature <= 63:
        b = 255
        g = temperature * 4
    elif temperature > 63 and temperature <= 127:
        g = 255
        b = 255 - (temperature - 64)*4
    elif temperature > 127 and temperature <= 191:
        r = (temperature - 128)*4
        g = 255
    else:
        r = 255
        g = 255 - (temperature - 192)*4
    
    return (r,g,b)

def format_temp_with_color(temperature):
    rgb_color = str(temp_to_rgb(temperature))
    return '<html><head/><body><p style="color: rgb' + rgb_color + '">' + str(temperature) + ' <span style=" vertical-align:super;">o</span>C</p></body></html>'

def format_temp(temperature):
    return '<html><head/><body><p>' + str(temperature) + ' <span style=" vertical-align:super;">o</span>C</p></body></html>'


N = 5
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

print(RGB_tuples)
