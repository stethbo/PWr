import multiprocessing as mp
import time


def naive_aproach(words_list, corpus):
    mistakes = 0
    for word in words_list:
        if word not in corpus:
            mistakes += 1

    return mistakes


if __name__ == '__main__':
    result = 0

    with open('corpus.txt', 'r') as f:
        all_words = f.readlines()
    all_words = [w.replace('\n', '') for w in all_words]

    with open('words.txt', 'r') as f:
        word_list = f.readlines()
    word_list = [w.replace('\n', '') for w in word_list]

    with mp.Pool(processes=7) as pool:
        start = time.time()
        print('start')
        p = mp.Process(target=naive_aproach, args=(word_list[:50000], all_words))
        p.run()

    print('end')
    end = time.time()
    print(end-start)
