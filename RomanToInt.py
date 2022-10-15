class Solution:
    def romanToInt(self, s: str) -> int:
        romanint = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        helper = 0
        leange = len(s)
        woerter = 0
        while woerter < leange-1:
            if s[woerter] == "I" and s[woerter + 1] == "V":
                helper = helper + romanint["V"] - romanint["I"]
                woerter += 2
            elif s[woerter] == "I" and s[woerter + 1] == "X":
                helper = helper + romanint["X"] - romanint["I"]
                woerter += 2
            elif s[woerter] == "X" and s[woerter + 1] == "L":
                helper = helper + romanint["L"] - romanint["X"]
                woerter += 2
            elif s[woerter] == "X" and s[woerter + 1] == "C":
                helper = helper + romanint["C"] - romanint["X"]
                woerter += 2
            elif s[woerter] == "C" and s[woerter + 1] == "D":
                helper = helper + romanint["D"] - romanint["C"]
                woerter += 2
            elif s[woerter] == "C" and s[woerter + 1] == "M":
                helper = helper + romanint["M"] - romanint["C"]
                woerter = woerter + 2

            else:
                helper = helper + romanint[s[woerter]]
                woerter += 1
        if woerter == leange-1:
            helper = helper + romanint[s[woerter]]
            woerter += 1
        return helper


if __name__ == '__main__':
    test = False
    if Solution().romanToInt("MCMXCIV") == 1994:
        test = True
    print("Test1: Aufgabe: 1994, heraus kam " + str(Solution().romanToInt("MCMXCIV")) + " dies ist " + str(test))
    test = False
    if Solution().romanToInt("MCDXCVIII") == 1498:
        test = True
    print("Test1: Aufgabe: 1498, heraus kam " + str(Solution().romanToInt("MCDXCVIII")) + " dies ist " + str(test))
    test = False
    if Solution().romanToInt("LXII") == 62:
        test = True
    print("Test1: Aufgabe: 62, heraus kam " + str(Solution().romanToInt("LXII")) + " dies ist " + str(test))
