def sherlockAndAnagrams(s):
    # Write your code here
    
    # creates a list of letters to primes
    def generatePrimes():
        output = {"a":2}
        i = 3
        for letter in "bcdefghijklmnopqrstuvwxyz":
            prime = False
            while not prime:
                prime = True
                for j in range(2, int(math.sqrt(i) + 1)):
                    if i % j == 0:
                        prime = False
                        i += 1
                        break
            output[letter] = i
            i += 1
        return output
    # function to hash the string
    def hashString(string, lookup):
        num = 1
        for character in string:
            num *= lookup[character]
        return num
    # calc here 
    letterLookup = generatePrimes()
    # print(letterLookup)
    lookup = {}
    counter = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            num = hashString(s[i:j], letterLookup)
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
    for key in lookup:
        if lookup[key] > 1:
            counter += int((lookup[key] - 1)*(lookup[key]) * 0.5)
    return counter
