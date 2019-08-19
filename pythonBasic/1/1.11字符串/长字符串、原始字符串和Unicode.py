#coding=utf-8
# 1、长字符串
# 可以使用三引号"""string""",或者'''string''''.
# 2、原始字符串
# 例如\n表示换行符，如下所示：
print 'Hello \nworld'
path='C:\nwindows'
# 正确应该这么写path='C:\\nwindows'
# 对于长路径，可以这么写：
print r'E:\QQMusicCache\musiccache'

# 如果最后一个字符是反斜线可以这么写：
print r'E:\QQMusicCache\musiccache' '\\'
# 3、Unicode字符串使用u前缀。
print u"Hello world"
