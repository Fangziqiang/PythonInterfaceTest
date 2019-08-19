#coding=utf-8

# 如果需要当用户在提示符下输入单词时做一些事情，并且在用户不输入单词后结束循环。可以使用下面的方法：
# 3、while True/break习语
'''
word='dummy'
while word:
    word=raw_input('Please enter a word:')
#     处理word：
    print 'The word was '+word
'''

############改进版#############
while True:
    word=raw_input('Please enter a word:')
    if not word:break
    print 'The word was '+word
# while True的部分实现了一个永远不会自己停止的循环。
