#coding=utf-8

import pysnooper



# @pysnooper.snoop('log/file.log')
# 先创建好log目录，然后将日志输出到file文件中。

# @pysnooper.snoop(prefix='removeDuplicates: ')
# 给调试的行加个前缀名便于辨识和定位，这个参数适用于如果同时调试多个函数使用，我这里的例子是使用了函数名称来作为前缀名，

# @pysnooper.snoop(variables=('foo.bar', 'self.whatever'))
# 查看非本地变量

@pysnooper.snoop(depth=2)
# 显示函数中调用函数的snoop行

# @pysnooper.snoop()
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    flag = 0
    i=1
    while i<len(nums):
        if nums[i]==nums[i-1]:
            flag+=1
            i+=1
            if flag>=2:
                del nums[i-1]
                i-=1
        else:
            i+=1
            flag=0
    return len(nums)

nums = [1,1,1,2]
print(removeDuplicates(nums))