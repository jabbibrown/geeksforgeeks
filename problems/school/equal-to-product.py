'''
Given an array of integers, check whether there are two numbers in the array that multiply to the given product.
author: jordan 

Full problem description at https://practice.geeksforgeeks.org/problems/equal-to-product/0#ExpectOP
'''
def equalToProduct(arr, product):
    divisorCache = {}  # key is divisor, value is its pair that divides evenly into X
    isProduct = "No"
    for number in arr:
        if (number != 0) and (product % number == 0):
            if product // number in divisorCache:  # check to see if its divisor pair is already saved
                # found a matching pair, break
                isProduct = "Yes"
                break
            else:
                divisorCache[number] = product // number  # integers only, save the divisor pair
    print(isProduct)


testCases = int(input())
for testCase in range(testCases):
    numOfElems, product = tuple([int(x) for x in input().split()])
    arr = [int(x) for x in input().split()]

    equalToProduct(arr, product)