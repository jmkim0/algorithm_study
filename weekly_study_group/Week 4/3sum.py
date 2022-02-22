class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n <= 2:
            return []
        
        result = set()
        passed_a = {}
        
        for i in range(n-2):
            a = nums[i]
            
            if a in passed_a:
                continue
                
            passed_b = {}
            
            for j in range(i+1, n):
                b = nums[j]
                target = -(a + b)
                if target in passed_b:
                    result.add(tuple(sorted([a, b, target])))
                passed_b[b] = True  
                
            passed_a[a] = True
            
        # return list(map(list, result))
        return result

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         result = []
        
#         nums = sorted(nums)
        
#         for i in range(n-2):
#             if i >= 1 and nums[i] == nums[i-1]:
#                 continue
            
#             target = -nums[i]
#             j = i+1
#             k = n-1
            
#             while j < k:
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     j += 1
#                     continue    
#                 if k < n-1 and nums[k] == nums[k+1]:
#                     k -= 1
#                     continue
                
                
#                 partsum = nums[j] + nums[k]
                
#                 if target == partsum:
#                     result.append([nums[i], nums[j], nums[k]])
#                     k -= 1
#                     j += 1
#                 elif target < partsum:
#                     k -= 1
#                 else:
#                     j += 1
            
#         return result
            