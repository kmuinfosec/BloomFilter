# BloomFilter

#### How to use
```python
from BloomFilter import BloomFilter

number_of_elements = 100
fp_prob = 0.01

bf = BloomFilter(number_of_elements, fp_prob)
print('Bloom Filter Status')
print(bf)

print('Add Data')
bf.add(b'junnyung')
bf.add(b'want')
bf.add(b'to')
bf.add(b'go')
bf.add(b'JEJU')

print('Check Data')
print(b'junnyung', 'in', 'BF :', bf.check(b'junnyung'))
print(b'want', 'in', 'BF :', bf.check(b'want'))
print(b'to', 'in', 'BF :', bf.check(b'to'))
print(b'go', 'in', 'BF :', bf.check(b'go'))
print(b'SEOUL', 'in', 'BF :', bf.check(b'SEOUL'))
```

#### Result
```
Bloom Filter Status
Filter Size : 958, Number of Hash Functions : 7
Add Data
Check Data
b'junnyung' in BF : True
b'want' in BF : True
b'to' in BF : True
b'go' in BF : True
b'SEOUL' in BF : False
```