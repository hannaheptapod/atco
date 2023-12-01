import sys
from collections import defaultdict


def main():
    arr_s = [line.strip() for line in sys.stdin.readlines()]
    ans = find_most_frequent_trigram(arr_s)
    print(ans)


def find_most_frequent_trigram(arr_s):
    trigram_counts = defaultdict(int)
    first_occurrence = {}
    word_index = 0

    for s in arr_s:
        words = list(map(lambda x: x.lower(), s.split()))
        for i in range(len(words) - 2):
            trigram = tuple(words[i:i+3])
            trigram_counts[trigram] += 1
            if trigram not in first_occurrence:
                first_occurrence[trigram] = word_index
            word_index += 1

    trigram, _ = min(trigram_counts.items(), key=lambda x: (-x[1], first_occurrence[x[0]]))
    return ' '.join(trigram)


if __name__ == "__main__": main()
