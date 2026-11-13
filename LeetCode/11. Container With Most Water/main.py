'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        # a = h * w

        while left < right:
            weight = ( right - left)
            lenght = min(height[left], height[right])
            area = lenght * weight
            if area > maxarea:
                maxarea = area
            elif height[left] < height[right] :
                left += 1
            else:
                right -= 1
        return maxarea 
