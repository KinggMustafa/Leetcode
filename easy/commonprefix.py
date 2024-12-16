class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        commonprefix = ""

        for i in range(len(strs[0])):#loop through the first word in the list
            for word in strs: #now for each word, we are going to compare
                if i >= len(word) or word[i] != strs[0][i]:
                    return commonprefix
            commonprefix += strs[0][i]
        return commonprefix


if __name__ == "__main__":
    test1 = ["dog", "do"]
    test2 = ["dog", "racecar"]

    result1 = Solution().longestCommonPrefix(test1)
    if result1: 
        print(f"{result1}")
    result2 = Solution().longestCommonPrefix(test2)
    if result2:
        print(f"{result2}")

#for each letter in the first word, we are checking to see if every other word matches, and if it does match that current index, it is added to the longest common prefix, we simply stop if it doesnt

#dog, d in dog matches, o in dog matches, but since i (2) >= the len(do), we return the longest common prefix of do

#dog, d in dog matches, r does not match so you return the longest common subsequence and it is "" bc we didnt go through all words to add the d yet

