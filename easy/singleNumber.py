class Solution:
    def singleNumber(self, nums) -> int:
        #use xor operand to cancel out dupllicate numbers in the list
        #xor returns 1 if the bits are not the same
        #1 xor 3 equals 2 bc only 1 bit gets canceled out 
        operand = 0 #anything xor 0 is the number itself
        for num in nums:
            operand = num ^ operand
        return operand
    
if __name__ == '__main__':
    #easiest testcase to visualize
    list1 = [2,2,1]
    #xor 2,2 = 0 xor 1 is just 1
    test1 = Solution().singleNumber(list1)
    if test1:
        print(f' single number: {test1}')

    list2 = [4,1,2,1,2]
    #even tho its not in order, the total operand is the cumulitive of all numbers, meaning xor is done to all number and even though its at different times the same bits will cancel out leaving just the single number
    test2 = Solution().singleNumber(list2)
    if test2:
        print(f'single Number: {test2}')
#things to note:
    #if there was more than just a single number without a duplicate xor would add those numbers together 