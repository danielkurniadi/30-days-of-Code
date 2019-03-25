def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = int((low + high)/2)
        if array[mid] > value:
            return binary_search(array, value, low, mid-1)
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid

if __name__ == '__main__':
    array = []
    answers = []
    f = open("inputbinsearch.txt", "r")
    for i in range(10000):
        array.append(int(f.readline()))
    for i in range(10000):
        value = int(f.readline())
        answer = binary_search(array, value, 0, 9999)
        answers.append(answer)
    f.close()
    fh = open("outputbinsearch.txt", "w")
    for answer in answers:
        fh.write("{}\n".format(answer))
    fh.close()
