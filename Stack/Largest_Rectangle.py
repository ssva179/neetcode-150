class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestArea = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                largestArea = max(largestArea, height* (i-index))
                start = index
            stack.append([start, heights[i]])
        for i, h in stack:
            largestArea = max(largestArea, h*(len(heights)-i))
        return largestArea
