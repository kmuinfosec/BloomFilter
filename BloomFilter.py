import mmh3
import math


class BloomFilter:
    def __init__(self, number_of_elements=100, fp_prob=0.01):
        self.filter_size = self.__calculate_filter_size(number_of_elements, fp_prob)
        self.number_of_hashes = None
        self.filter = (1 << self.filter_size)

    @classmethod
    def __calculate_filter_size(cls, number_of_elements, fp_prob):
        return int(-number_of_elements * math.log(fp_prob) / math.pow(math.log(2), 2))

    def add(self, data):
        for i in range(self.number_of_hashes):
            idx = mmh3.hash_bytes(data, i, signed=True) % self.number_of_hashes
            self.filter |= (1 << idx)

    def check(self, data):
        for i in range(self.number_of_hashes):
            idx = mmh3.hash_bytes(data, i, signed=True) % self.number_of_hashes
            if (self.filter >> idx) & 1 == 0:
                return False
        return True
