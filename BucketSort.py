import math
DEFAULT_BUCKET_SIZE = 5
def insertionSort(arr):
    for pos in range(1,len(arr)):
        nextpos=pos
        while nextpos>0 and arr[nextpos]<arr[nextpos-1]:
            arr[nextpos],arr[nextpos-1]=arr[nextpos-1],arr[nextpos]
            nextpos-=1
            

def sort(array, bucketSize=DEFAULT_BUCKET_SIZE):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = min(array)
    maxValue = max(array)

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    #Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])

    #Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    for i in range(0, len(array)):
        print(array[i])

print("Enter the list of elements to be sorted: ",end=' ')
l=[int(x) for x in input().split()]
sort(l)
