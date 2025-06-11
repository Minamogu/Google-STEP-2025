def make_dictionary(word):
    alphabet = {}
    for i in word:
        if i in alphabet.keys():
            alphabet[i] += 1
        else:
            alphabet[i] = 1
    return alphabet

def find_anagram(word, dict_list):
    word_alphabet = make_dictionary(word)
    highest_score = 0
    anagram = ''

    for k in dict_list:
        match = True

        dict_alphabet = k[1]
        for i, j in dict_alphabet.items():
            if i not in word_alphabet or j > word_alphabet[i]:
                match = False
                break
        if match:
            score = evaluate_score(dict_alphabet, score_dict)
            if score > highest_score:
                highest_score = score
                anagram = k[0]
    return anagram


def evaluate_score(word_alphabet, score_dict):
    score = 0

    for i,j in word_alphabet.items():
        score += score_dict[i] * j
    return score

score_dict = {'j':4, 'k':4, 'q':4, 'x':4, 'z':4, 'b':3, 'f':3, 'g':3, 'p':3, 'v':3, 'w':3, 'y':3,\
'c':2, 'd':2, 'l':2, 'm':2, 'u':2, 'a':1, 'e':1, 'h':1, 'i':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1}

if __name__ == '__main__':  
    with open('words.txt', 'r') as f:
        dict_list = []
        for line in f:
            dict_list.append((line.rstrip('\n'), make_dictionary(line.rstrip('\n'))))

    with open('small.txt', 'r') as sf, open('anagram.txt', 'a') as df:
        for line in sf:
            anagram = find_anagram(line.rstrip('\n'), dict_list)
            if anagram:
                df.write(anagram + '\n')
