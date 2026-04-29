class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        result = []
        for _, end in intervals:
            idx = bisect_left(sorted_starts, (end, -float('inf')))
            
            if idx < n:
                result.append(sorted_starts[idx][1])
            else:
                result.append(-1)
                
        return result
