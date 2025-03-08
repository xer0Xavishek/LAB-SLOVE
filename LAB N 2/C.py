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
        max_length = max(max_length, i - start + 1) # i - start + 1 is the length of the subarray how? : t

        ''''''

    return max_length  # Return the length of the longest subarray

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Find and print the length of the longest subarray
print(longest_subarray_sum(n, k, arr))

"""Key Question: Why is i - start + 1 the length?
i is the right boundary (where we are in the array).

start is the left boundary (where the valid subarray starts).

The length of the subarray is:
right_index - left_index + 1         [0 through 5 is 6 elements, not 5.]

right_index - left_index + 1 = i - start + 1

Because if start = 2 and i = 5, then the subarray is [arr[2], arr[3], arr[4], arr[5]] which has 4 elements → (5 - 2 + 1) = 4."""