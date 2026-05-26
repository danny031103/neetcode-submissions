class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #quicker answer
       #create a dictionary with key:values where
       #frequency:list of numbers that have that frequency
       #the amount of keys will be len(nums) since most possible is
       #every number is the same
       #then count the frequency of each number and add it to the 
       #dictionary at corresponding freq such that each frequency's 
       #value is a list of the numbers that are that frequency

        #create hashmap of frequency:numbers that match it
        frequency={}
        #size is dictated by size of input array 1-size
        for i in range(1,len(nums)+1):
            frequency[i]=[]
        
        #count how many times each number appears and add it to a dictionary
        counts = {}
        for x in nums:
            #if its not already in counts add it
            if x not in counts:
                counts[x] = 0
            #otherwise increase +1
            counts[x] += 1

        #counts.items() → returns a sequence of (key, value) aka (num,frequency)
        # pairs from the dictionary
        for num, c in counts.items():
            #then appends the number to the corresponding frequency in the frequency dict
            frequency[c].append(num)
       
        #variable to return list of k most frequent elements
        res = []

        #range(start,stop,step), so we're going backwards because we want the biggest
        #frequencies first
        for f in range(len(nums), 0, -1):
            #if that key has values in it then append them
            for num in frequency[f]:
                res.append(num)
                #check if we have enough elements (k) and return
                if len(res) == k:
                    return res
        return res
       
       
        # #my solution:
        # #given k, an integer asking for the k most frequent elements
        # #create a hashmap to hold key: values where number:frequency
        # #sort the hashmap by frequency
        # #return the first k keys

        # #create dictionary
        # #number:frequency
        # freq={}

        # #iterate through nums, if i not in dict then add it as a key
        # #if it is then add to the freq
        # for i in nums:
        #     if i not in freq:
        #         freq[i]=1
        #     freq[i]+=1

        # #sort dictionary in descending order of values
        # sorted_ = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        # #return the first k keys
        # return [key for key, _ in sorted_[:k]]
