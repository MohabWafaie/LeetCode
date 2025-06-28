class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        maxi = 0
        j = 0
        for i in nums:
            if i == 0:
                if k > 0:
                    count += 1
                    maxi = max(count, maxi)
                    k -= 1
                elif count > 0:
                    while(count >= 0):
                        if nums[j] == 1:
                            count -= 1
                            j += 1
                        else :
                            j += 1
                            break
                else : j += 1
            else:
                count += 1
                maxi = max(maxi, count)
        return maxi


        