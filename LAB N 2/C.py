def longest_subarray_sum(n, k, arr):
    max_length = 0  # Initialize the maximum length of the subarray
    current_sum = 0  # Initialize the current sum of the subarray
    start = 0  # Initialize the start of the window

    for i in range(n):  # Iterate through the array with 'i' as the end of the window
        current_sum += arr[i]  # Add the current element to the current sum

        # Adjust the window if the current sum exceeds 'k'
        while current_sum > k:
            current_sum -= arr[start]  # Subtract the element at 'start' from the current sum
            start += 1  # Move the start of the window to the right

        # Update the maximum length of the subarray
        max_length = max(max_length, i - start + 1)

    return max_length  # Return the length of the longest subarray

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Find and print the length of the longest subarray
print(longest_subarray_sum(n, k, arr))