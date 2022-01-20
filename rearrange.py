import random, sys


if __name__ == "__main__":
    params = sys.argv[1:]
    random.shuffle(params)
    print(params)

