#coding:utf-8

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str.replace(",", "")
str.replace(".", "")
words = str.split()

list = []

for word in words:
    list.append(len(word))
print list