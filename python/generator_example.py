
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
            
input_file = 'testfile.csv'
if __name__ == "__main__":
    print '--> read each line of text file'
    for line in read_file_lines(input_file):
        print line
        
    print '--> read each word of text file'
    for word in read_file_words(input_file, sep=','):
        print word
        