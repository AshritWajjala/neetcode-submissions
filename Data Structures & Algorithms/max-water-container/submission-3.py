class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        final = 0
        while i != j:
            current = min(heights[i], heights[j]) * (j -  i)
            final = max(final, current)
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return final