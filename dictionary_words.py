import random, sys

def sentence(word_count):
    with open('/usr/share/dict/words') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        rand_sent = random.choices(lines, k=word_count)
        for i in rand_sent:
            print(str(i), end=" ")


if __name__ == '__main__':
    params = int(sys.argv[1])
    sentence(params)