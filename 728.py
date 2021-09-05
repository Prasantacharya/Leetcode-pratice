class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right + 1):
            string = str(i)
            flag = True
            for character in string:
                number = int(character)
                if number == 0 or i % number > 0:
                    flag = False
                    break
            if flag:
                output.append(i)
        return output
            
