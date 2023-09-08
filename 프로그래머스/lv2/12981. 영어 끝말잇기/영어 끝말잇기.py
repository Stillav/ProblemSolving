def solution(n, words):
    answer = [0, 0]

    word_dict = {}
    
    for i, word in enumerate(words):
        if i != 0 and words[i - 1][-1] != words[i][0] or word_dict.get(word) is not None:
            return [i % n + 1, i // n + 1]
        else:
            word_dict[word] = 1

    return answer