import math

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getPrimes():
            output = {"a":2}
            counter = 3
            for letter in "bcdefghikjlmnopqrstuvwxyz":
                isPrime = False
                while not isPrime:
                    isPrime = True
                    for i in range(2, int(math.sqrt(counter) + 1)):
                        if counter % i == 0:
                            isPrime = False
                            counter += 1
                            break
                output[letter] = counter
                counter += 1
            return output
        
        def hashString(string, lookup):
            output = 1
            for letter in string:
                output *= lookup[letter]
            return output
        
        letterLookup = getPrimes()
        lookup = {}
        for string in strs:
            num = hashString(string,letterLookup)
            if num not in lookup:
                lookup[num] = []
            lookup[num].append(string)
        
        # go through the dictionary
        retArray = []
        for key in lookup:
            retArray.append(lookup[key])
        return retArray
