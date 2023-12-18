class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.freq2 = {}

    def add(self, number: int) -> None:
        if number not in self.freq:
            self.freq[number] = 0
        temp = self.freq[number]
        self.freq[number] += 1
        if self.freq[number] not in self.freq2:
            self.freq2[self.freq[number]] = 0
        self.freq2[self.freq[number]] += 1

        if temp in self.freq2:
            self.freq2[temp] -= 1
       

    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] != 0:
            temp = self.freq[number]
            self.freq[number] -= 1

            if self.freq[number] not in self.freq2:
                self.freq2[self.freq[number]] = 0
            self.freq2[self.freq[number]] += 1
            self.freq2[temp] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq2 and self.freq2[frequency] > 0:
            return True
        return False
        
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)