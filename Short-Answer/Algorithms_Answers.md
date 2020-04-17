#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n)


b)O(nlogn) - but maybe O(n^2)


c)O(n)

## Exercise II
def throwEggs(building,f):
  floor = 0
  for i in building:
    if i == f:
      floor = i
    else:
      "egg didn't break"
  return floor