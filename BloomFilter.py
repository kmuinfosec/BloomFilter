import mmh3
import math


class BloomFilter:
    def __init__(self, number_of_elements=100, fp_prob=0.01):
        self.filter_size = self.__calculate_filter_size(number_of_elements, fp_prob)
        self.number_of_hashes = self.__calculate_number_of_hashes(self.filter_size, number_of_elements)
        self.filter = 0

    @classmethod
    def __calculate_filter_size(cls, number_of_elements, fp_prob):
        return int(-number_of_elements * math.log(fp_prob) / math.pow(math.log(2), 2))

    @classmethod
    def __calculate_number_of_hashes(cls, filter_size, number_of_elements):
        return int(math.ceil((filter_size / number_of_elements) * math.log(2)))

    def add(self, data):
        for i in range(self.number_of_hashes):
            idx = mmh3.hash(data, i) % self.filter_size
            self.filter |= (1 << idx)

    def check(self, data):
        for i in range(self.number_of_hashes):
            idx = mmh3.hash(data, i) % self.filter_size
            if (self.filter >> idx) & 1 == 0:
                return False
        return True

    def __str__(self):
        return 'Filter Size : {}, Number of Hash Functions : {}'.format(self.filter_size, self.number_of_hashes)