class Solution:
    def isAnagram(s, t) -> bool:
        sorteds = sorted(s)
        sortedt = sorted(t)
        #nlogn time
        #sorting them will put both in alphabetic order

        if len(s) != len(t): #if they are not the same size, they cannot be complete anagrams
            return False
        #if they are not identical in alphabetical order, they are not anagrams
        for i in range(len(sorteds)):
            if sorteds[i] != sortedt[i]:
                return False
        return True
    
    def isAnagramspace(s,t) -> bool:

        if len(s) != len(t):
            return False
        
        hashmap = {} #store each letter and value

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1 #if the key(letter) does not exist default it to 0, and add 1 to its value
            hashmap[t[i]] = hashmap.get(t[i], 0) - 1 #for every letter in t, we are subtracting 
        #for every s value, t should erase it 
        for value in hashmap.values():
            if value != 0:
                return False #if all the values are not 0, that means there is an extra letter, so we return False
        return True
    

if __name__ == "__main__":
    s = "list"
    t = "stil"
    t2 = "rat"

    result1 = Solution.isAnagram(s, t2)
    if result1:
        print(f"{result1}")
    result2 = Solution.isAnagramspace(s, t)
    if result2:
        print(f"{result2}")


