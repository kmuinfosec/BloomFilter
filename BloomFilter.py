import math
import hashlib

class BloomFilter:
    def __init__(self, number_of_elements=100, fp_prob=0.01):
        self.filter_size = self.__calculate_filter_size(number_of_elements, fp_prob)
        self.bins = [ 0 ] * (int(self.filter_size / 64) + 1)
        self.number_of_hashes = self.__calculate_number_of_hashes(self.filter_size, number_of_elements)
        self.slice = math.ceil(math.log2(self.filter_size))
        self.mod_value = (1 << self.slice) - 1

    @classmethod
    def __calculate_filter_size(cls, number_of_elements, fp_prob):
        return int(-number_of_elements * math.log(fp_prob) / math.pow(math.log(2), 2))

    @classmethod
    def __calculate_number_of_hashes(cls, filter_size, number_of_elements):
        return int(math.ceil((filter_size / number_of_elements) * math.log(2)))

    def add(self, data):
        i = 0
        while True:
            idx = int(hashlib.blake2b(data + '{}'.format(i).encode()).hexdigest(), 16)
            for j in range(0, 512, self.slice):
                temp = idx & self.mod_value
                if temp >= self.filter_size:
                    temp -= self.filter_size
                bin_idx, bit_idx = divmod(temp, 64)
                self.bins[bin_idx] |= (1 << bit_idx)
                i += 1
                if i == self.number_of_hashes:
                    break
                idx >>= self.slice
            if i == self.number_of_hashes:
                break

    def check(self, data):
        i = 0
        while True:
            idx = int(hashlib.blake2b(data + '{}'.format(i).encode()).hexdigest(), 16)
            for j in range(0, 512, self.slice):
                temp = idx & self.mod_value
                if temp >= self.filter_size:
                    temp -= self.filter_size
                bin_idx, bit_idx = divmod(temp, 64)
                if (self.bins[bin_idx] >> bit_idx) & 1 == 0:
                    return False
                i += 1
                if i == self.number_of_hashes:
                    break
                idx >>= self.slice
            if i == self.number_of_hashes:
                break
        return True

    def __str__(self):
        return 'Filter Size : {}, Number of Hash Functions : {}'.format(self.filter_size, self.number_of_hashes)
