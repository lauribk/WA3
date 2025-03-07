#goal: want to find a partition of both arrays where:
#   the left of the first array is less than the right of the second
#   the left of the second array is less than the right of the first
#       then we have found the middle of the combined array without combining and sorting



def findMedianSortedArrays(nums1, nums2):

    m = len(nums1)
    n = len(nums2)

    #check to find smallest array for BONUS QUESTION optimization
    if m > n:
        return (findMedianSortedArrays(nums2, nums1))

    #interval for best partition, will hone into the correct partition
    partMin = 0
    partMax = m

    totalLength = m + n
    # using integer addition since the values will be used for the index and must be integers
    mid = (m + n + 1) // 2

    #binary search until a correct partition for each array is found
    while partMin <= partMax:
        #trial partition indexes
        split1 = (partMin + partMax) // 2
        split2 = mid - split1

        #set the left and right of both array partitions to be less than and greater than any values that could be encountered
        left1, left2, right1, right2 = -100000000, -100000000, 100000000, 100000000
        #set to represent the elements directly to the left and right of the partition of each vector
        if split1 < m:
            right1 = nums1[split1]
        if split2 < n:
            right2 = nums2[split2]
        if split1 - 1 >= 0:
            left1 = nums1[split1 - 1]
        if split2 - 1 >= 0:
            left2 = nums2[split2 - 1]

        #the main goal partition to find -- check and see if it is found
        if left1 <= right2 and left2 <= right1:
            #the partition is found and we can compute the median
            if totalLength % 2 == 1:
                #if it is odd, then the median is just the biggest element on the left
                return max(left1, left2)
            else:
                #if it is even we need the average of the two middle
                return (float(max(left1, left2))+float(min(right1,right2))) / 2.0
        #if the partition is not correct, then adjust it by moving it higher or lower
        elif left1 > right2:
            partMax = split1 - 1
        else:
            partMin = split1 + 1
    return 0
if __name__ == "__main__":
    nums1 = [1, 3, 9, 14, 19, 38, 59]
    nums2 = [2]

    m = len(nums1)
    n = len(nums2)

    #deal with edge case - one array is empty
    if m == 0:
        if n % 2 == 1:
            #if it is odd, then the median is in the middle
            print(nums2[(n)//2])
        else:
            if n == 1:
                print(n[1])
            else:
                #if it is even we need the average of the two middle
                print(((float(nums2[(n)//2])+float(nums2[((n)//2)-1])) / 2.0))

    elif n == 0:
        if m % 2 == 1:
            #if it is odd, then the median is in the middle
            print(nums1[(m)//2])
        else:
            if m == 1:
                print(m[1])
            else:
                #if it is even we need the average of the two middle
                print(((float(nums1[(m)//2])+float(nums1[((m)//2)-1])) / 2.0))
    else:
        median = findMedianSortedArrays(nums1, nums2)
        print(median)