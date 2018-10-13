import png

green_rgb = [63, 101, 5]

       
conv_list = []
chars = open('char_conversions.txt')
for conv in chars:
    conv_list.append(int(conv))

bit_list = []
bit_dict = {}
for a in conv_list:
    add_thing = str(bin(a)).lstrip('0b')
    for b in range(15-len(add_thing)):
        add_thing = '0' + add_thing
    bit_list.append(add_thing)

for a in range(len(bit_list)):
    bit_dict[chr(a+ord('A'))] = bit_list[a]

bit_dict[':'] = '000010000010000'
bit_dict['3'] = '110001010001110'
bit_dict['<'] = '001010100010001'

def print_char(array, x, y, char_to_print, scale):
    for a in range(15):
        xt = (a % 3)*scale
        yt = int(a / 3)*scale
        if bit_dict[char_to_print][a] == '1':
            for val in range(scale*scale):
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3] = green_rgb[0]
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3+1] = green_rgb[1]
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3+2] = green_rgb[2]
    return array

 
def produce_image(input_text):
    max_width = 12
    max_height = 3
    max_len = max_width * max_height
    input_text = "".join(x for x in input_text if x.isalpha() or x == ' ')
    input_text = input_text.upper()
    input_text = input_text[:max_len - 5]
    input_text = ":33<" + input_text
    r=png.Reader(filename='/home/pi/Documents/img.png')

    r1 = r.read(lenient=True)

    l=list(r.read()[2])

    left_bound = 300
    top_bound = 165

    x_delta = 0
    y_delta = 0

    scale = 5
    for a in range(len(input_text)):
        x_delta = (a%max_width)*scale*4
        y_delta = int(a/max_width)*scale*10
        if input_text[a] != ' ':
            l = print_char(l, left_bound+x_delta, top_bound+y_delta, input_text[a], scale)
            

    png.Writer( r1[0], r1[1] ).write(open('/home/pi/Documents/out_img.png', 'wb+'), l)
    return 0
