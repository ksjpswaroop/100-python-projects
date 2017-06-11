
def mergesort(n):
    if len(n) > 1:
        first = n[:len(n)//2]
        last = n[len(n)//2:]
        mergesort(first)
        mergesort(last)

        i = 0
        j = 0
        z = 0
        while i < len(first) and j < len(last):
            if first[i] < last[j]:
                n[z] = first[i]
                i = i + 1
            else:
                n[z] = last[j]
                j = j + 1
            z = z + 1

        while i < len(first):
            n[z] = first[i]
            i = i + 1
            z = z + 1

        while j < len(last):
            n[z] = last[j]
            j = j + 1
            z = z + 1
    return n


def bubblesort(n):
    return 1







mylist = [59,13,2,95,46,37,49,82,26]
print(mergesort(mylist))
print(bubblesort(mylist))
