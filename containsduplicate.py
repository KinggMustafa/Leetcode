class Solution:
    def containsDuplicate(self, nums):
        stored = set() #o(n) space for storing the list of numbers
        for i in range(len(nums)): #o(n) for looping through the list of n size
            if nums[i] in stored:
                return True

            else:
                stored.add(nums[i])
        return False
    #first solution, O(n) space and time

    #by trying to save space complexity, you can resort to sorting. 
    def containsDuplicateviasorting(self, nums):
        sorted_nums = sorted(nums) #this sorts (O(nlogn)) time complexity
        for i in range(len(sorted_nums)):
            if i < len(sorted_nums)-1:
                if sorted_nums[i] == sorted_nums[i+1]:
                    return True
        return False
    #this algorithm has an nlogn time complexity, but the space complexity is o(1) because we are not storing.


if __name__ == "__main__":
    test1= [1,2,3,4]
    test2 = [1,2,1,2,1,2]
    result_1 = Solution().containsDuplicate(test1)
    if result_1:
        print(f'storing way: {result_1}')
    result_2 = Solution().containsDuplicate(test2)
    if result_2:
        print(f'storing way: {result_2}')
    result_3 = Solution().containsDuplicateviasorting(test1)
    if result_3:
        print(f'sorting {result_3}')
    result_4 = Solution().containsDuplicateviasorting(test2)
    if result_4:
        print(f'sorting {result_4}')
    