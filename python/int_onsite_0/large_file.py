import sys, os

# NEEDED ONLY TO GENERATE THE INPUT
def create_big_file(filename, one_large_sentence):
    sentence = 'My name is Amol Kokje. '

    with open(filename, 'w') as fh:
        fh.write(sentence)

    for _ in range(10000):
        with open(filename, 'a') as fh:
            if one_large_sentence:
                fh.write(sentence)
            else:
                fh.write(sentence + "\n")


def process_file(input_filename, replace_str, replace_words, output_filename):
    with open(output_filename, 'w') as outputfh:
        with open(input_filename) as inputfh:
            # process chunk by chunk
            for chunk in read_in_chunks(inputfh, 128):
                new_chunk = process_chunk(chunk, replace_str, replace_words)
                outputfh.write(new_chunk)


def read_in_chunks(fh, chunk_size):
    while True:
        # read file by specified chunk size
        chunk = fh.read(chunk_size)
        # if there is no more left break
        if not chunk:
            break
        # lazy processing - create a generator so a only a chunk is returned at a time
        yield chunk


def process_chunk(chunk, replace_str, replace_words):
    # handle: . , :
    new_chunk = ''
    for word in chu
    for word in replace_words:
        chunk = chunk.replace(word, replace_str)
    return chunk


if __name__ == '__main__':
    input_filename = 'input_file.log'
    output_filename = 'output_file.log'

    input_words_file = 'input_words.txt'
    replace_str = '*'

    # GENERATE INPUT LOG FILE
    create_big_file(input_filename, False)

    # read the words to replace
    replace_words = None
    with open(input_words_file) as fh:
        replace_words = [w.strip() for w in fh.readlines()]
    print 'Words to Replace With = {}'.format(replace_words)

    process_file(input_filename, replace_str, replace_words, output_filename)

    # REMOVE LOG FILES
    log_files = filter(lambda x:x.endswith('.log'), os.listdir(os.getcwd()))
    for file in log_files:
        os.remove(file)

