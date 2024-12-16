class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+= 1
        return k

if __name__ == "__main__":
      test1 = [0,0,1,1,1,2,2,3,3,4]
      result = Solution.removeDuplicates(test1)
      if result:
          print(f"{result}")
    #in this k = 1, i = 1
    #compare i with k-1, since they are the same we keep going
    #nums[i] (1), with nums[k-1] (0), since it is now distinct k[1] (0) is now 1 and we keep going forward
    #it shifts every dinstinct to the left in increasing order, althought the array does not completley get rid of duplicates, it returns the disinct ones and then whatever follows is the duplciates which is fine in the problem directions. 
    #this solution is better than using a set because it does not consume memory 0(1) space but 0(n) time