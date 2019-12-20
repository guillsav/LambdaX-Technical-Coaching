# Inserting a Node Into a Sorted Doubly Linked List

Given a reference to the head of a doubly-linked list and an integer, `data`, create a new DoublyLinkedListNode object having data value `data` and insert it into a sorted linked list while maintaining the sort.

### Function Description

Complete the `sortedInsert()` function in the editor below. It must return a reference to the head of your modified DoublyLinkedList.

`sortedInsert()` has two paramters:

1. head: A reference to the head of doubly-linked list of _DoublyLinkedListNode_ objects.
2. data: An integer denoting the of the `data` field for the DoublyLinkedListNode you must insert into the list.

#### Note

> Recall that an empty list (ie., where _head_ = `null`) and a list with one element are sorted lists.

### Input Format

The first line contains an integer _t_, the number of test cases.

Each of the test case is in the following format:

-   The first line contains an integer _n_, the number of elements in the linked list.
-   Each of the next _n_ lines contains an integer, the data of each node of the linked list.
-   The last line contains an integer `data` which needs to ve inserted into the sorted doubly-linked list.

## **Example:**

```python
Sample input:

1  # ------- Number of test cases.
4  # ------- Length of the linked list.

1  # ------- Element in the Linked list.
3  # ------- Element in the Linked list.
4  # ------- Element in the Linked list.
10 # ------- Element in the Linked list.

5  # ------- Element to insert in the Linked list.

Sample output:
1 3 4 5 10
```

# Explanation

The initial doubly linked list is:

> `1 <-> 3 <-> 4 <-> 10 -> null`

The doubly linked list after insertion is:

> `1 <-> 3 <-> 4 <-> 5 <-> 10 -> null`
