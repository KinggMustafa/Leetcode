class Solution:
    def subarraySum(self, nums, k: int) -> int:
        hashmap = {0: 1}
        ways = 0
        currsum = 0
        for number in nums:
            currsum += number
            difference = currsum - k
            if difference in hashmap:
                ways += hashmap.get(difference, 0)
            hashmap[currsum] = hashmap.get(currsum, 0) + 1
        return ways
        #at each index you are adding the number to your currsum
        #then you are checking if currsum - K is in the dictionary storing what numbers we have found so far, if it is then how ever many ways that difference can be found is added to ways. 
    #and then no matter what we add one way the currsum was found in our hashmap
    #the hashmap starts off with a default value of 0: 1 because if the array is just 1, 1-1 is 0 and it needs that trailing 0 for this solution to work.  