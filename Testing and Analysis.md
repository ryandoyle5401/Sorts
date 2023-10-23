# Adaptive Bubble Sort Test  
## Adaptive Bubble Sort Explanation  
The Adaptive Bubble Sort is a very simple adaptive algorithm because it takes the original Bubble Sort algorithm and adds some minor modifications to it. Basically, a boolean variable is added to the algorithm to check for any swaps performed as the algorithm runs. If the algorithm makes it to the end of the first iteration without performing any swaps, this indicates the array is already in sorted order, so the code will break out of the main loop preventing the Bubble Sort from continuing further unnecessarily.  
## The Arrays  
For testing out both the normal and adaptive bubble sort algorithms, I used two different arrays both comprised of 5,000 integers. The normal bubble sort algorithm received an array of 5,000 integers that were randomly selected within a range of 1 to 100,000 using the randint() function of the random class. The adaptive bubble sort algorithm received an array of 5,000 integers that were already in sorted order, and this was done by simply having a for loop populate an array with integers as the loop reached its limit of 5,000.  

## The Execution  
Using the time() function from the time module in Python, upon executing a random array of 5,000 integers, the normal Bubble Sort had an average of xxx seconds., while the Adaptive Bubble Sort had an average of xxx seconds. As a best-case scenario, the Adaptive Bubble Sort would have a time complexity of O(n), but the worst-case complexity is still O(n<sup>2</sup>). Memory  usage also remains the same for both bubble sort algorithms at a complexity of O(1).  
BubbleSort1 time ![BubbleSort1 time](BubSort1.png)  
BubbleSort2 time ![BubbleSort2 time](BubSort2.png)
BubbleSort3 time ![BubbleSort3 time](BubSort3.png)  

# Hybrid MergeSort Test - TimSort
## TimSort Explanation
## The Arrays
## The Execution
MergeSort1 time ![MergeSort1 time](MergeSort1.png)
MergeSort2 time ![MergeSort2 time](MergeSort2.png)
MergeSort3 time ![MergeSort3 time](MergeSort3.png)
