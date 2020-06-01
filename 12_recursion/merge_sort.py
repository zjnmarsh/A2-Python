def merge(S1, S2, S):
    """Merge two sorted python lists S1 and S2 into properly sized list S."""

    i=j=0
    while i+j < len(S):
        if j == len(S2) or (i<len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]
            j += 1

def mergeCheat(S1, S2, S):
    """cheat to do merge using Python builtin function"""
    for i in range(len(S1+S2)):
        S[i] = sorted(S1 + S2)[i]

def merge_sort(S):
    num_elements = len(S)
    if num_elements < 2:
        return

    mid = num_elements//2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

array1 = [19,2,5,1,6,4,8,9,11,2]
print(array1)
merge_sort(array1)
print(array1)

