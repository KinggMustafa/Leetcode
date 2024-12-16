class Solution:
    def plusOne(digits):
        for i in range(len(digits)-1, -1,-1): #traverse backward
            if digits[i] < 9: #if the current number is not 9, we just add 
                digits[i] += 1 #and stop iterating bc we already added
                return digits
            else:
                digits[i] = 0 #keep carrying the 1 until its not 9
        return [1] + digits #if all digits are 9, we add a 1 to the list of 0's to return 100000000000000000


if __name__ == "__main__":
    digits1 = [9,9,9]
    result1 = Solution.plusOne(digits1)
    if result1:
        print(f"999 + 1 = {result1}")
    
    digits2 = [1,9]
    result2 = Solution.plusOne(digits2)
    if result1:
        print(f"19 + 1 = {result2}")
    
    digits3 = [1,9,9]
    result3 = Solution.plusOne(digits3)
    if result3:
        print(f"199 + 1 = {result1}")
    
    digits4 = [1,2,3]
    result4 = Solution.plusOne(digits4)
    if result1:
        print(f"123 + 1 = {result4}")
    
    