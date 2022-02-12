# Exercise 7: More Printing
print("Mary had a little lamb.")
# a best pratice, we will use single quotes when is a short string, line a word
print("Its fleece was white as {}." .format('snow'))
print("And everywhere that Mary went.")
# Will print 10 times the character "."
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# the end = ' ', join together the next print(), with a space
# add the first six letters
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
# add the last six letters
print(end7 + end8 + end9 + end10 + end11 + end12)
