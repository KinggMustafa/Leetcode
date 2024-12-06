class Solution:
    def isPalindromeconvertingtostring(self, x: int) -> bool:
        if x < 0:
            return False
        numberstring = str(x) #convert number to string
        reversednumberstring = numberstring[::-1] #reverse the string of the original number
        return reversednumberstring == numberstring #if the reversed is equal to the original 
        
    def ispalindromereversing(self, x:int) -> bool:
        if x < 0:
            return False
        reconstructed_reversed_number = 0 #variable to store reversed number
        original_number = x #store the original because we are going to break x down by each decimal place

        while x != 0:
            reconstructed_reversed_number = reconstructed_reversed_number * 10 + x % 10 #in this step, you multiply by 10 to get to the correct decimal place, (even if we start at 0, it will mean we are at the 1's place) then we add x remainder 10, meaning we add the number in x's current decminal place.
            x = x // 10 #divide x by 10 to continiously break it down
        return reconstructed_reversed_number == original_number #return the relationship between the reversed number and the original x
    
if __name__ == "__main__":
    x = 121
    print(f"Using string conversion relationship holds: {Solution().isPalindromeconvertingtostring(x)}")
    #this converts 121 to a string, then reverses that string to 121, and then compares 121 to 121 to return True

    print(f"Using the reverse reconstruction method, the relationship holds: {Solution().ispalindromereversing(x)}")
    #this breaks down 121 decimal place by decminal place. 
    #reversed number first adds 1 (reversed number *10 is 0)
    #then we break down x from 121 to 12 (floor division)
    #reversed number takes the 2 and adds it to the 1's place. (1*10, + 2) = 12
    #break down x from 12 to 1 
    #reversed number is now (12*10, = 120 + 1 %10 = 1) = 121
    #this algo does not add numbers in verse, it reconstructs the number in reverse. 