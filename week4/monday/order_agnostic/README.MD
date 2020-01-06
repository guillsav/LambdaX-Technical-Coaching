# Order Agnostic Binary Search

Given a sorted array of numbers, find if a given number target is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.

Write a function to return the index of the target if it is present in the array, otherwise return -1.

Example 1:

```
Input: [4, 6, 10], target = 10
Output: 2
```

Example 2:

```
Input: [1, 2, 3, 4, 5, 6, 7], target = 5
Output: 4
```

Example 3:

```
Input: [10, 6, 4], target = 10
Output: 0
```

Example 4:

```
Input: [10, 6, 4], target = 4
Output: 2
```
