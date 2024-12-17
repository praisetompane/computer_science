def search(value, arr):
    def recurse(upperBound, lowerBound):
        midpoint = (lowerBound + upperBound) // 2
        if value < arr[midpoint]:
            return recurse(lowerBound, midpoint - 1)
        elif value > arr[midpoint]:
            return recurse(midpoint + 1, upperBound)
        elif value == arr[midpoint]:
            return midpoint
        return None

    return recurse(0, len(arr) - 1)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(8, data))
