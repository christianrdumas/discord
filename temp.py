import png

green_rgb = [63, 101, 5]

       
conv_list = []
chars = open('char_conversions.txt')
for conv in chars:
    conv_list.append(int(conv))

bit_list = []
for a in conv_list:
    add_thing = str(bin(a)).lstrip('0b')
    for b in range(15-len(add_thing)):
        add_thing = '0' + add_thing
    bit_list.append(add_thing)

def print_char(array, x, y, char_to_print, scale):
    for a in range(15):
        xt = (a % 3)*scale
        yt = int(a / 3)*scale
        if bit_list[char_to_print][a] == '1':
            for val in range(scale*scale):
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3] = green_rgb[0]
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3+1] = green_rgb[1]
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3+2] = green_rgb[2]
    return array

 
def produce_image(input_text):
    input_text = "".join(x for x in input_text if x.isalpha())
    input_text = input_text.upper()
    input_text = input_text[:11]
    r=png.Reader(filename='/home/pi/Documents/img.png')

    r1 = r.read(lenient=True)

    l=list(r.read()[2])

    xval = 300
    yval = 200
    for a in input_text:
        if a != ' ':
            l = print_char(l, xval, yval, ord(a)-ord('A'), 5)
        xval += 5 * 4


    png.Writer( r1[0], r1[1] ).write(open('/home/pi/Documents/out_img.png', 'wb+'), l)
    return 0
