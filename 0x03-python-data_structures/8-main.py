#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
sen = "" 
length, first = multiple_returns(sentence)
lengthe, firste = multiple_returns(sen)
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(lengthe, firste))

