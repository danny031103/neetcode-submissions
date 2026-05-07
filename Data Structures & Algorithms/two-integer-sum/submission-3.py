class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #my brute force solution
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j]==target):
        #             return [i,j]

        #using a hashmap
        #hashmap to add elements as we visit them
        #value:index pairs
        prevMap={}

        #enumerate lets you loop through the items
        for i,n in enumerate(nums):
            #difference is the number we're looking for within the hashmap because with it, the target can be reached
            #where n is the current number we're on
            diff=target-n

            #check in the diff is in the hashmap already aka have we visited it
            if diff in prevMap:
                #yes, so then return the indexes, the diff index first since its the lesser index as requested in problem
                return [prevMap[diff],i]

            #if not then continue, but first add the current number into the hashmap so we can refer to it later
            prevMap[n]=i            


            #time complexity: O(n) because we can worst case visit until the end of the array checking the hashmap once each time
            #space complexity: O(n) because we create a hashmap with potentially all the elements in it 
