
class QuickSort:

    def __init__(self, data: list):
        self.sort(data, 0, len(data))

    def a_gt_b(self, a: str, b: str) -> bool:
        m_a, len_a, index_a = a.split('-')
        len_a = int(len_a)
        index_a = int(index_a)

        m_b, len_b, index_b = b.split('-')
        len_b = int(len_b)
        index_b = int(index_b)

        if m_a[0].lower() != m_b[0].lower():
            return a[0].lower() < b[0].lower()
        if m_a[0].isupper() and m_b[0].islower():
            return True
        if m_a[0].islower() and m_b[0].isupper():
            return False

        if len_a > 1 and len_b > 1:
            if m_a[1].lower() != m_b[1].lower():
                return a[1].lower() < b[1].lower()
            if m_a[1].isupper() and m_b[1].islower():
                return True
            if m_a[1].islower() and m_b[1].isupper():
                return False

        if len_a == len_b:
            return index_a < index_b
        return len_a < len_b

    def partition(self, data: list, low: int, high: int) -> int:
        rnd_index = high - 1
        pivot = data[rnd_index]
        i = low - 1

        for j in range(low, high-1):
            if self.a_gt_b(data[j]['data'], pivot['data']):
                i += 1
                data[i], data[j] = data[j], data[i]

        data[i+1], data[rnd_index] = data[rnd_index], data[i+1]
        return i + 1

    def sort(self, data, low, high):
        if low < high:
            pi = self.partition(data, low, high)

            self.sort(data, low, pi)
            self.sort(data, pi + 1, high)


words = input().split('0')[0].split()
data = [{}] * len(words)
for i in range(len(words)):
    tmp = words[i]
    data[i] = {'word': tmp, 'data': '{}-{}-{}'.format(tmp[:2], len(tmp), i + 1)}

QuickSort(data)
print(' '.join([item['word'] for item in data]))
