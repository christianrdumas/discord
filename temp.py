import png
import textwrap
import json

green_rgb = [63, 101, 5]

troll_colors = {'nepeta':[63, 101, 5],
                'vriska':[0, 64, 128],
                'karkat':[108, 108, 108],
                'equius':[0, 32, 203]}

       
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

bit_dict['O'] = '111101101101111'
bit_dict[':'] = '000010000010000'
bit_dict['3'] = '110001010001110'
bit_dict['<'] = '001010100010001'
bit_dict['1'] = '010110010010111'
bit_dict['2'] = '110001010100111'
bit_dict['4'] = '101101111001001'
bit_dict['5'] = '111100010001110'
bit_dict['6'] = '011100110101010'
bit_dict['7'] = '111001010100100'
bit_dict['8'] = '010101010101010'
bit_dict['9'] = '010101011001110'

def print_char(array, x, y, char_to_print, scale, color):
    for a in range(15):
        xt = (a % 3)*scale
        yt = int(a / 3)*scale
        if bit_dict[char_to_print][a] == '1':
            for val in range(scale*scale):
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3] = color[0]
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3+1] = color[1]
                array[y+yt+int(val/scale)][(x+xt+(val%scale))*3+2] = color[2]
    return array

 
def produce_image(input_text, character):
    character = json.loads(open(character+'.json').read())
    scale = 4
    char_width = scale * 4
    char_height = scale * 10
    max_width = int((character['right']-character['left'])/char_width)
    max_height = int((character['bottom']-character['top'])/char_height)
    max_len = max_width * max_height
    input_text = "".join(x for x in input_text if x.isalpha() or x == ' ' or x.isnumeric())
    input_text = input_text.upper()
    if character['name'] == 'nepeta':
        input_text = ":33<" + input_text
    input_text = input_text[:max_len]
    input_text = textwrap.wrap(input_text, max_width)
    input_text = input_text[:max_height]
    r=png.Reader(filename='/home/pi/Documents/' + character['name'] + '.png')

    r1 = r.read(lenient=True)

    l=list(r.read()[2])

    left_bound = character['left']
    top_bound = character['top']

    x_delta = 0
    y_delta = 0

    for a in input_text:
        for b in range(len(a)):
            if a[b] != ' ':
                l = print_char(l, left_bound+x_delta, top_bound+y_delta, a[b], scale, troll_colors[character['name']])
            x_delta += char_width
        x_delta = 0
        y_delta += char_height
            

    png.Writer( r1[0], r1[1] ).write(open('/home/pi/Documents/out_img.png', 'wb+'), l)
    return 0
