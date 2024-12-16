class Solution:
    def isValid(s):
        hashmap = {
            ')': '(',
            '}': '{',
            ']': '['
        } #we store the closers as the keys, bc as we traverese through, we are only adding the starting ones to started list
        started = []
        for i in range(len(s)):
            if s[i] in hashmap: 
                if started and hashmap[s[i]] == started[-1]: #we check to see if it is a closer, and it the coresponding starter was last added
                    started.pop() #if so we remove, treat started as a stack
                else:
                    return False #we return false bc if we have a closer with no opener then it is not valid
            else:
                started.append(s[i]) #if its not a closer, its an opener and we add to started
        if len(started) != 0:
            return False #if we still have some started, return False
        return True #return true if all started were closed properly
if __name__ == "__main__":
    test1 = "([])"
    result1 = Solution.isValid(test1)
    if result1:
        print(f"{result1}")