import re

##refactor functions with just .split so there is no hanging space
def create_histogram(file):
    with open(file) as f:
        case_insenstive = f.read().lower()
        mod_str = case_insenstive.replace("_", "")
        str_list = re.split('\W+', mod_str)
        histogram = {}
        for word in str_list:
            if word:
                if word in histogram:
                    histogram[word]+=1
                else:
                    histogram[word] = 1
        return histogram

def find_unique_words(histogram):
    unique_words_int = 0
    for key in histogram:
        if histogram[key] == 1:
            unique_words_int += 1
    return unique_words_int

def find_word_frequency(word, histogram):
    frequency = 0
    for key in histogram:
        if key == word:
            frequency = histogram[key]
    return frequency




if __name__ == "__main__":
    example_histogram = create_histogram('sherlock-holmes.txt')
    # print(example_histogram)
    print(find_unique_words(example_histogram))
    print(find_word_frequency('mystery', example_histogram))
