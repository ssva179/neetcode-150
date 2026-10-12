class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right= 0, len(heights)-1
        m_area = 0

        while left < right:
            curr_area = (right-left) * min(heights[left], heights[right])
            m_area = max(m_area, curr_area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right -=1
        return m_area
