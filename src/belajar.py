import itertools

letter = ['a', 'b', 'c']
perm = '347'
perm = [c for c in perm]
letterValue = dict(zip(letter, perm))
print(perm)
print(letterValue)

words = ["aku","pintar"]
let = list(''.join(words))
print(let)


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def combs(s, r):
    if not r:
        yield ''
    elif s:
        first, rest = s[0], s[1:]
        for comb in combs(rest, r-1):
            yield first + comb  # use first char ...
        yield from combs(rest, r)  # ... or don't

def perms(s, r):
    if not r:
        yield ''
    else:
        for comb in combs(s, r):
            for i, char in enumerate(comb):
                rest = comb[:i] + comb[i+1:] 
                for perm in perms(rest, r-1):
                    yield char + perm
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break

# for perm in permutations((1,2,3),2):
#     print(perm)

for i in reversed(range(3)):
    print(i)

cycles = list(range(10, 7, -1))
print(cycles)
print(int('1') + int ('3'))

def printAllKLengthRec(set, prefix, n, k): 
      
    # Base case: k is 0, 
    # print prefix 
    if (k == 0) : 
        print(prefix) 
        return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
    for i in range(n): 
  
        # Next character of input added 
        newPrefix = prefix + set[i] 
          
        # k is decreased, because  
        # we have added a new character 
        printAllKLengthRec(set, newPrefix, n, k - 1) 
    
set1 = ['0', '1', '2','3'] 
k = 3
print("this is new" + str(set1[len(set1)-1]))
printAllKLengthRec(set1, "", 4, k)

def permutation(word):
    if len(word) == 1:
        return [word]
    
    perms = permutation(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range (len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    
    return result

print(permutation('abc'))