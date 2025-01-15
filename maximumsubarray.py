class Solution:
    def maxSubArray(self, nums) -> int:
        subarray = [0] * len(nums)
        subarray[0] = nums[0]
        maximumsubarray = nums[0]
        for i in range(1,len(nums)):
            subarray[i] = max(nums[i], nums[i] + subarray[i-1])
            maximumsubarray = max(maximumsubarray, subarray[i])
        return maximumsubarray
#this solution is correct, has a time complexity of o(n) but has a space complexity of o(n) as well. 
    def maxSubArrayOptimal(self, nums) -> int:
        maximumsubarray = nums[0] #base case for maximum subarray will be the first one in the list
        everysum = nums[0]
        for i in range(1,len(nums)):
            everysum = max(nums[i], nums[i] + everysum) 
            maximumsubarray = max(maximumsubarray, everysum)
        return maximumsubarray
#example [-2,1,-3,4,-1,2,1,-5,4]
#everysum = -2, 1, -2, 4, 3, 5, 6, -1, 4
#maximum = -2, 1, 1, 4, 4, 5, 6 ,6, 6

if __name__ == "__main__":
    example = [-2,1,-3,4,-1,2,1,-5,4]
    res1 = Solution.maxSubArray(example)
    if res1: 
        print(f'{res1}')
    res2 = Solution.maxSubArrayOptimal(example)
    if res2: 
        print(f'{res2}')