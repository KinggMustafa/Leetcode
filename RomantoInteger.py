class Solution:
     def romanToInt(self, s: str) -> int:
        hashmap = { #store our roman numerals in a hashmap
            "I":1,
            "V": 5,
            "X" : 10,
            "L" : 50,
            "C" :  100,
            "D" : 500,
            "M" :1000,
        }
        number = 0 
        i = 0 #we set this pointer to 
        while i < len(s): #we stop at the last letter in the string
            if i < (len(s)-1) and hashmap[s[i]] < hashmap[s[i+1]]: #here we make sure we are not at the last letter bc none of the rules apply to the last leter, and since roman numerals are written largest to smallest, we see if the letter after the current one we are at is greater
                  number += hashmap[s[i+1]] - hashmap[s[i]] #if the letter after our current one is bigger, we subtract the smaller from the bigger and add to our number
                  i += 2 #we then skip the next letter bc it is already incorporated in our number
            else:
                  number += hashmap[s[i]] #if none of the rules apply then we just add the current letter
                  i += 1 #move to next letter
        return number 


if __name__ == "__main__":
    romannumeral = "MCMXCIV"
    result = Solution().romanToInt(romannumeral)
    if result: 
        print(f"{result}")
    else:
        print("enter roman numerals!!!!!!!!!!!!")

    #M, m = 1000, 1000 > 100, so number += 1000 
    #C is less than M, so number = 1900 (number += 1000 - 100)
    #X, X = 10, 10 < 100 so number = 1990 (number += 100 - 10)
    #I, I = 1, 1 < 5, so number = 1994 (number += 5 - 1)