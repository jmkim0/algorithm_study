class Solution:
    # 스택을 활용하여 수면이 갱신될 때 마다 추가하는 방식
    def trap(self, height):
        n = len(height)
        s = []
        result = 0
        
        if n == 0:
            return 0
              
        for i in range(n):
            while s and height[s[-1]] < height[i]:
                prev = s.pop()
                
                if not s:
                    break
                
                result += (min(height[i], height[s[-1]]) - height[prev]) * (i - s[-1] - 1)
                
            s.append(i)
                                 
        return result
    
    # 제일 높은 기둥을 기준으로 하고 양 옆에서 접근하면서 수면높이를 맞추는 방식
    # 양 옆에서 접근하는 방식(two pointer, dp 등)은 거의 다 비슷한 것 같은데 이 방법이 제일 무식하고 쉬운 듯
    def trap2(self, height):
        n = len(height)
        
        if n == 0:
            return 0
        
        temp = sum(height)
        max_index = 0
        max_height = height[0]
        
        for i in range(1, n):
            if height[i] > max_height:
                max_height = height[i]
                max_index = i
        
        for i in range(max_index-1):
            if height[i+1] < height[i]:
                height[i+1] = height[i]
        
        for i in range(n-max_index-2):
            if height[-i-2] < height[-i-1]:
                height[-i-2] = height[-i-1]
                                 
        return sum(height) - temp