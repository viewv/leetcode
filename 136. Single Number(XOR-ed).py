#copy from Leetcode, really a good way!
class Solution:
    def singleNumber(self, nums):
        # using XOR method
        single_num = 0
        for n in nums:
            single_num ^= n
        return single_num
'''
if two number is different like 1010 and 1010
    1010 xor 1010 = 0 so when a group of number
    is contered one number for many time use xor
    can make them to 0, but if the 1010 face 0
    like this problem single_num=0 meet a single num
    it will be a plus, 0000 xor 1010 is 1010 so finally
    the single_num will remember the single number
    really good way to solve this problem
    also you need to know a^b^c^d... can can be 
    (a^b)^(c^d)... so you don't need to worry about
    the problem of sequence, really good, great!
'''