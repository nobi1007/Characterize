#from colored import fg,attr
#rst = attr('reset')

codes = (
    '#000000',
    '#800000',
    '#008000',
    '#808000',
    '#000080',
    '#800080',
    '#008080',
    '#c0c0c0',
    '#808080',
    '#ff0000',
    '#00ff00',
    '#ffff00',
    '#0000ff',
    '#ff00ff',
    '#00ffff',
    '#ffffff',
    )

codes_dict = {}
for i in range(len(codes)):
    codes_dict[codes[i]] = i
'''
for i in range(len(codes)):
    color = fg(codes_dict[codes[i]])
    print(color+"Hello World!" +rst)
'''
    