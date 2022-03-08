import sys
from itertools import combinations


def pw_gen(l, c, letters):
    if l < 3:
        return []

    all_vowels = set('aeiou')
    vowels = []
    consonants = []
    result = []
    
    for letter in letters:
        if letter in all_vowels:
            vowels.append(letter)
        else:
            consonants.append(letter)
    
    n = len(vowels)
    m = len(consonants)

    for i in range(n):
        for j in range(m-1):
            for k in range(j+1, m):
                rest = vowels[i+1:] + consonants[k+1:]
                
                if len(rest) < l-3:
                    break
                
                for comb in combinations(rest, l-3):
                    temp = [vowels[i], consonants[j], consonants[k]] + list(comb)
                    result.append(''.join(sorted(temp)))
    
    return sorted(result)

l, c = map(int, sys.stdin.readline().split())

letters = sys.stdin.readline().split()

for pw in pw_gen(l, c, letters):
    print(pw)