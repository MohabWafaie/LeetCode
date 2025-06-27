class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        product1 = 1
        product2 = 1
        j = len(nums) -1
        for i in nums:
            product1 *= i
            prefix.append(product1)
            product2 *= nums[j]
            suffix.append(product2)
            j -= 1
        result = []
        print(suffix)
        print(prefix)
        j = 0
        for i in nums:
            if j == 0:
                result.append(suffix[-2])
                j +=1
            elif j == (len(nums) - 1):
                result.append(prefix[-2])
                return result
            else :
                val = suffix[((j+2)*-1)] * prefix[j-1]
                result.append(val)
                j += 1 
        
        