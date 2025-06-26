class Solution:
    def findNumbers(self, nums) -> int:
        
        even = 0
        for num in nums:
            digits = 0
            while num > 0:
                num = num // 10 #when you do floor division with 10 it just knocks off the last digit of that number, so we just count how many times we knock it off and check if that itself is even or odd
                digits += 1
            if digits % 2 == 0: #where we check to see if the number of digits are even
                even += 1
        return even
    
if __name__ == '__main__':
    test = [12,345,2,6,7896]
    test1 = Solution().findNumbers(test)
    if test1:
        print(f"there are {test1} number/s with an even number of digits")
#this solution is O(n) bc the for loop will run n times with n indexes in the list
#the while loop will only run at most 6 times, bc the biggest number we will get is 10^5 according to the contrains given in the problem 
