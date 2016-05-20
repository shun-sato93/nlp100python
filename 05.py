#coding:utf-8


def n_gram(input, n):
    print(input)
    word = []
    length = len(input)
    # if type(input) == str:
    #     print("str")
    #     for i in xrange(0, length):
    #         end = length if i+n >= length else i+n
    #         word.append(input[i:end])
    # elif type(input) == list:
    #     print("list")

    for i in xrange(0, length):
        end = length if i + n >= length else i + n
        word.append(input[i:end])

    return word

text = "I am an NLPer"
print n_gram(text, 2)

text = text.split()
print n_gram(text, 2)