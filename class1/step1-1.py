def binary_search(word, dict):
    left = 0
    right = len(dict) - 1
    mid_list = []
    n = len(dict)

    while left <= right:
        mid = (right + left) // 2
        mid_word = dict[mid][0]
        #アナグラムを見つけたら複数個あるか確認
        if dict[mid][0] == word:
            mid_list.append(mid) 
            i = 1
            while (mid+i) < n and dict[mid+i][0] == word:
                mid_list.append(mid+i)
                i += 1
            i = 1
            while (mid-1) >= 0 and dict[mid-i][0] == word:
                mid_list.append(mid-i)
                i += 1
            return mid_list
        elif mid_word < word:
            left = mid_word + 1
        else:
            right = mid_word - 1
            
        return mid_list
    
def better_solution(random_word, dictionary):
    sorted_random_word = sorted(random_word)
    new_dictionary = []
    for word in dictionary:
        new_dictionary.append((sorted(word), word))
    new_dictionary.sort()

    ans = binary_search(sorted_random_word, new_dictionary)
    if ans:
        print('\nanagram:')
        for i in ans:
            print(new_dictionary[i][1]) 
    else:
        print('There\'s no anagram.')


random_word = input()
dictionary = list(input().split())
better_solution(random_word, dictionary)

