class Solution:
    def addDigits(self, num: int) -> int:

        helper = str(num)
        number = 0

        for x in helper:
            number = number + int(x)
        number_helper = str(number)

        if len(number_helper) > 1:
            return self.addDigits(number)
        return number

if __name__ == '__main__':
    test = False
    if Solution().addDigits(387) == 9:
        test = True
    print("Test1: Aufgabe: 387, heraus kam " + str(Solution().addDigits(387)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(9) == 9:
        test = True
    print("Test1: Aufgabe: 9, heraus kam " + str(Solution().addDigits(9)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(0) == 0:
        test = True
    print("Test1: Aufgabe: 0, heraus kam " + str(Solution().addDigits(0)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(1) == 1:
        test = True
    print("Test1: Aufgabe: 1, heraus kam " + str(Solution().addDigits(1)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(10) == 1:
        test = True
    print("Test1: Aufgabe: 10, heraus kam " + str(Solution().addDigits(10)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(11) == 2:
        test = True
    print("Test1: Aufgabe: 11, heraus kam " + str(Solution().addDigits(11)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(12) == 3:
        test = True
    print("Test1: Aufgabe: 12, heraus kam " + str(Solution().addDigits(12)) + " dies ist " + str(test))
    test = False
    if Solution().addDigits(13) == 4:
        test = True
    print("Test1: Aufgabe: 13, heraus kam " + str(Solution().addDigits(13)) + " dies ist " + str(test))