#coding:utf-8

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str.replace(".", "")
str.replace(",", "")
str = str.split()

single = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dictionary = {}
for i, word in enumerate(str):
    if single.__contains__(i + 1):
        dictionary[word[:1]] = i
    else:
        dictionary[word[:2]] = i

#sort by value
for k, v in sorted(dictionary.items(), key=lambda x:x[1]):
    print k, v
#print dictionary