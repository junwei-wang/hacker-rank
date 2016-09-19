#!/usr/bin/env python

def init_key_map(ciphers, dictionary):
    longest = max(ciphers, key=len)
    tmp = filter(lambda x: len(x) == len(longest) and len(set(x)) == len(set(longest)), dictionary)

    def is_match(word):
        t = dict()
        for i, c in enumerate(longest):
            if c in t:
                t[c].add(i)
            else:
                t[c] = set([i])

        for v in t.values():
            if len(v) > 1 and len(set([word[i] for i in v])) > 1:
                return False
        return True

    if len(tmp) > 1:
        tmp = filter(is_match, tmp)

    # TODO still more than one
    key_map = dict()
    for i, v in enumerate(longest):
        key_map[v] = tmp[0][i]

    return key_map


def find_a_easy_gussing_word(key_map, cipher, ignored):
    to_be_removed = set()
    chars_in_key = set(key_map.keys())
    min_diff = len(chars_in_key)
    ret = None

    for word in cipher.difference(ignored):
        diff_chars = set(word).difference(chars_in_key)
        if len(diff_chars) == 0:
            to_be_removed.add(word)
        elif len(diff_chars) == 1:
            ret = word
            min_diff = 1
            break
        elif len(diff_chars) < min_diff:
            ret = word
            min_diff = len(diff_chars)

    cipher.difference_update(to_be_removed)
    return ret


def find_alternative_words(key_map, cipher_word, dictionary):
    len_cipher_word = len(cipher_word)
    def is_match(word):
        if len(word) != len_cipher_word:
            return False

        word = word.lower()
        for i, c in enumerate(cipher_word):
            if c in key_map and not(key_map[c] == word[i]):
                return False
        return True

    return filter(is_match, dictionary)

def refine_key_map(key_map, cipher_word, dict_word):
    for i, c in enumerate(cipher_word):
        if c not in key_map:
            key_map[c] = dict_word[i].lower()

if __name__ == '__main__':
    dictionary = open("dictionary.lst").read().split()
    input = raw_input()
    ciphers = set(input.split())

    # init key map
    key_map = init_key_map(ciphers, dictionary)

    # refine key map
    ignored_words = set()
    while len(key_map) < 26:
        word = find_a_easy_gussing_word(key_map, ciphers, ignored=ignored_words)
        if not word or len(ciphers) <= 0:
            break
        alternative_word = find_alternative_words(key_map, word, dictionary)
        if len(alternative_word) > 1:
            ignored_words.add(word)
            continue

        # TODO: there might be more than 1 alternative_word
        refine_key_map(key_map, word, alternative_word[0])

    output = ''
    for c in input:
        if c == ' ':
            output += c
        else:
            output += key_map[c]
    print output
