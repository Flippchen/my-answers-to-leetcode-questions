#This Programm should be able to compare the Hamming Distance of two strings. The Hamming Distance is the number of positions at which the corresponding symbols are different. The Hamming Distance is only defined for strings of equal length. The Hamming Distance is also known as the Point Mutation Distance.

class HammingDistance:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        self.counter = 0
        if len(self.string1) == len(self.string2):
            for i in range(len(self.string1)):
                if self.string1[i] != self.string2[i]:
                    self.counter += 1
        else:
            print("Strings are not of equal length")
    def __str__(self):
        return str(self.counter)



