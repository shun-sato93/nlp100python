#coding:utf-8

def xyz(x, y, z):
    return "%s時の%sは%s" % (str(x), str(y), str(z))

def n_gram(input, n):
    word = []
    length = len(input)
    
    for i in xrange(0, length):
        end = length if i + n >= length else i + n
        word.append(input[i:end])
    
    return word

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(n_gram(str1, 2))
Y = set(n_gram(str2, 2))

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

print "se" in X
print "se" in Y

print xyz(12, "気温", 22.4)