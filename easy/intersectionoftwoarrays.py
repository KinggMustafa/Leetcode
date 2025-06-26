class Solution:
    def intersection(self, nums1, nums2):
        #if we just have two sets, lookup is o(1) time and it will draw out the unique elements in both
        setnums1 = set(nums1)
        #nvm we only create one set bc you cant iterate through a set like a list
        uniquelist = []
        for num in nums2:
            if num in setnums1:
                uniquelist.append(num) 
                setnums1.remove(num)
        return uniquelist

        #time complexity O(n+m)
        #n is making the set, m is iterating through the list. 
        #lookup and removal in a set is O(1) bc it uses hash values

if __name__ == '__main__':
    nums1 = [1,2,3,4]
    nums2 = [4,1]
    solution = Solution().intersection(nums1,nums2)
    if solution:
        print(f'intersecting numbers: {solution}') 