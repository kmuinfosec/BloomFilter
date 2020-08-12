import math
import hashlib


class BloomFilter:
    def __init__(self, number_of_elements=100, fp_prob=0.01):
        self.filter_size = self.__calculate_filter_size(number_of_elements, fp_prob)
        self.__mod_value = (1 << self.filter_size) - 1
        self.number_of_hashes = self.__calculate_number_of_hashes(self.filter_size, number_of_elements)
        self.__slice = math.ceil(math.log2(self.filter_size))
        self.filter = 0

    @classmethod
    def __calculate_filter_size(cls, number_of_elements, fp_prob):
        return int(-number_of_elements * math.log(fp_prob) / math.pow(math.log(2), 2))

    @classmethod
    def __calculate_number_of_hashes(cls, filter_size, number_of_elements):
        return int(math.ceil((filter_size / number_of_elements) * math.log(2)))

    def add(self, data):
        i = 0
        while i < self.number_of_hashes:
            idx = int(hashlib.blake2b(data + '{}'.format(i).encode()).hexdigest(), 16)
            for j in range(0, 512, self.__slice):
                temp = idx & self.__mod_value
                self.filter |= (temp % self.filter_size)
                i += 1
                idx >>= self.__slice

    def check(self, data):
        i = 0
        while i < self.number_of_hashes:
            idx = int(hashlib.blake2b(data + '{}'.format(i).encode()).hexdigest(), 16)
            for j in range(0, 512, self.__slice):
                temp = idx & self.__mod_value
                self.filter |= (temp % self.filter_size)
                i += 1
                idx >>= self.__slice
        return True

    def __str__(self):
        return 'Filter Size : {}, Number of Hash Functions : {}'.format(self.filter_size, self.number_of_hashes)