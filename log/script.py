fw = open('rpm.txt', 'w')
with open('gokart_log.txt') as f:
    for line in f.readlines():
        line_splitted = line.split()
        if(line_splitted[1] == "0CF11E05"):
            rpm_lsb = int(line_splitted[3], base=16)
            rpm_msb = int(line_splitted[4], base=16)
            rpm_dec = rpm_msb * 256 + rpm_lsb
            print (rpm_dec)
            fw.write(str(rpm_dec)+'\n')

fw.close()
