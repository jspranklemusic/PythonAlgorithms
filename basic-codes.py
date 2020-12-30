import re

def toCelsius(fahr):
    return (fahr - 32)*5/9
    
def toFahrenheit(cels):
    return (cels*9/5)+32

def reverseString(str):
    i = 1
    revStr=""
    for x in str:
        revStr+=str[-i]
        i+=1
    return revStr

def longestWord(str):
    splits = str.split(" ")
    splits.sort(reverse=True, key=len)
    return splits[0]

def repeatStr(str, num):
    return str*num

def truncateString(str, num):
    if num < 0:
        return None
    return str[0:(int(num))]

def chunkArrayInGroups(arr,num):
    i=0
    j=0
    newArr=[]
    while i < len(arr):
        if not len(newArr) > j:
            newArr.append([])
        newArr[j].append(arr[i])
        if len(newArr[j]) == num:
            j+=1
        i+=1
    return newArr

def mutation(arr):
  for char in arr[1]:
      if not char in arr[0]:
          return False
  return True

def getIndexToIns(arr, num):
    arr.sort()
    for x in arr:
        if x > num:
            return arr.index(x) 
def sumAll(arr):
    arr.sort()
    i = arr[0]
    while i < arr[1]:
         i+=1
         arr[0]+=i
    return arr[0]

def diffArray(arr1, arr2):
    differences = []
    for x in arr1:
        if not x in arr2:
            differences.append(x)

    for x in arr2:
        if not x in arr1:
            differences.append(x)
    return differences

def destroyer(*args):
    items = list(args)
    arr = items[0]
    newArr = []
    del items[0]
    for x in arr:
        if not x in items:
            newArr.append(x)
    return newArr
    
def whatIsInAName(collection, source):
    for prop in source:
        for x in collection:
            if x[prop] == source[prop]:
                return x

def spinalCase(str):
    return re.sub("[\s_]","-",str).lower()

def bubbleSort(arr):
    for x in arr:
        i = 0
        while i<len(arr) - 1:
            if arr[i] > arr[i+1]:
                swap = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=swap
            i+=1
    return arr

def insertionSort(arr):
    i=1
    while i<len(arr):
        if arr[i-1]>arr[i]:
            j=i-1
            while j > 0:
                if arr[j] > arr[j+1]:
                    swap = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = swap
                    j-=1
                else:
                    j=0

        i+=1
    return arr















