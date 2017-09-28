fw = open('times_comma.txt', 'w')
with open('times.txt') as f:
    for line in f.readlines():
        x = line.replace('.', ',') if '.' in line else line
        fw.write(x)

fw.close()
