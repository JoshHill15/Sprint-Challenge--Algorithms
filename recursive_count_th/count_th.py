'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# def count_th(word):
#     if not word:
#         return word
#     else:
#         thing = count_th(word[1:])
#         if thing == None:
#             thing = word
#         if thing != None:
#             print(thing)

#             return thing.count("th")


def count_th(word):
    i = 0
    count = 0

    def find_th(word, i):
        if i == len(word):
            nonlocal count
            count = word.count("th")
            return word
        else:
            i += 1
            find_th(word, i)
    find_th(word, i)
    return count


print(count_th("fifth"))
