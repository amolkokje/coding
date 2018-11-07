
def read_file_lines(file):
    with open(file, 'r') as fh:
        ## instead of: return fh.readlines()
        ## this will return an iterator on which you can iterate on, like list comprehension
        for line in fh.readlines():
            yield line

def read_file_words(file, sep=' '):
    for line in read_file_lines(file):
        ## instead of: return line.split(sep)
        ## this will return an iterator on which you can iterate on, like list comprehension
        for word in line.split(sep):
            yield word

stream = []

def stream_put(stream):
    print 'start stream put thread ...'
    c = 0
    while True:
        stream.append('c={}'.format(c))
        c += 1
        time.sleep(0.5)
    
def stream_read(stream):
    for line in stream:
        yield line

        
input_file = 'testfile.csv'
if __name__ == "__main__":
    import time
    from threading import Thread

    th0 = Thread( target=stream_put, args=[stream] )
    th0.start()
    print 'reading stream ...'
    for line in stream_read(stream):
        print 'line={}'.format(line)
        time.sleep(0.5)
        
    #print '--> read each line of text file'
    #for line in read_file_lines(input_file):
    #    print line
    #    
    #print '--> read each word of text file'
    #for word in read_file_words(input_file, sep=','):
    #    print word
        