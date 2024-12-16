def twosum(target, nums):
    #target is a target integer and nums is a list of numbers
    #return the indicies that have the numbers that will add up to the target

    hashmap = {} #we will store the number as the key, index as the value
    for i in range(len(nums)):
        difference = target - nums[i] #take the difference from the current number you are on
        if difference in hashmap: #we check if this number is in the keys of our hashmap
            return hashmap[difference], i #return the value (the index) and i the current index we are on
        else:
            hashmap[nums[i]] = i #if the difference is not yet found, store what we have so far in the hashmap

#test cases
if __name__ == "__main__":
    target1 = 9
    nums1 = [2, 7, 1, 2, 3]
    result = twosum(target1, nums1)
    if result:
        print(f"found! indicies are {result}")
    else:
        print("NOO")


