class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        m_index = {0: -1}  
        prefix = 0
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - target) % p

            if need in m_index:
                res = min(res, i - m_index[need])

            m_index[prefix] = i

        return res if res < len(nums) else -1
