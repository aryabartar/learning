def word_split(string, words_dict):
    for word in words_dict:
        if string[0:len(word)] == word:

            if len(string) == len(word):
                return [word]

            result = word_split(string[len(word):], words_dict)

            if result is not None:
                result.append(word)
                return result

            else:
                return None
    return None


print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
