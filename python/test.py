import time
input_file = 'testfile.csv'

c = 0
while True:
    with open(input_file, 'a') as fh:
        print c
        fh.write('{},{},{},'.format(c,c,c))
        c += 1
        time.sleep(0.5)