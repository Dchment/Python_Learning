# Giving a integer list,find out its sublist whose sum of elements is the largest, output its sum.
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0# 子序列，和初始化为0
        maxnum=nums[0]# 最大和
        for i in range(len(nums)):# i为计算子序列的新结尾元素
            pre=max(nums[i],pre+nums[i])
            # 计算原来的子序列加上新结尾后其和是否比这个结尾大，有就加上新结尾元素，没有就将此结尾设为新的子序列开头
            # （既然前面的所有元素加起来都没这个新结尾大，那此结尾前面的子序列的和是不可能成为最大的了！）——>判断，使用动态规划法！
            maxnum=max(maxnum,pre)# 比较现在的子序列的和是不是最大
        return maxnum

s=Solution()
print(s.maxSubArray([1,2,-1,1]))

