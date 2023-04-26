import math


def bold_word(word):
    if word:
        if len(word) == 1:
            return '<b>' + word + '</b>'
        half = math.floor(len(word)/2)
        if len(word) % 2:
            half+=1
        if word.startswith('(') or word.startswith('"'):
            half+=1
        # print(word[half:], word[:half-1])
        return '<b>'+ word[:half] + '</b>' + word[half:]
    else:
        return ''

lines = []
with open('manifesto.txt', 'r') as f:
    lines = f.readlines()
    
def bionicize(lines):
    doc = []
    for line in lines:
        new_line = ''
        for word in line.split(' '):
            if '-' in word:
                new_line += bold_word(word.split('-')[0]).strip() + '-' + bold_word(word.split('-')[1]).strip() + ' '
            else: 
                new_line += bold_word(word.strip()) + ' '
        doc.append(new_line) 
    return doc

start = '<html><head></head><body style="margin-left: 25%; width: 50%; color:  #282828; line-height: 30px; font-size: 22px; font-family:Georgia, ''Times New Roman'', Times, serif">'
end = '</body></html>'
with open('clear.html', 'w') as f:
    f.write(start)
    for line in lines:
        f.write(line)
        f.write('<br>')
    f.write(end)   
with open('result.html', 'w') as f:
    f.write(start)
    for line in bionicize(lines):
        f.write(line)
        f.write('<br>')
    f.write(end)