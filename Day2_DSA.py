"""Day 2: recursion, dynamic programming, backtracking, greedy ideas, and bit tricks."""

from functools import lru_cache


# ------------------------------
# Bit manipulation (existing Day 2)
# ------------------------------
def rightmost_set_bit(value: int) -> int:
    """Return the lowest set bit using x & -x."""
    return value & -value


def count_set_bits(value: int) -> int:
    """Count how many bits are set in a number."""
    count = 0
    while value:
        value &= value - 1
        count += 1
    return count


def single_number(nums: list[int]) -> int:
    """Return the value that appears once while others appear twice."""
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_ii(nums: list[int]) -> int:
    """Return the value that appears once while others appear three times."""
    result = 0
    for bit in range(32):
        total = sum((num >> bit) & 1 for num in nums)
        if total % 3:
            result |= 1 << bit
    return result


def single_number_iii(nums: list[int]) -> list[int]:
    """Return the two values that appear once while others appear twice."""
    xor_all = 0
    for num in nums:
        xor_all ^= num

    diff_bit = xor_all & -xor_all
    first = second = 0

    for num in nums:
        if num & diff_bit:
            first ^= num
        else:
            second ^= num

    return [first, second]


def missing_number(nums: list[int]) -> int:
    """Find the missing number in a 0..n range using XOR."""
    result = len(nums)
    for index, value in enumerate(nums):
        result ^= index ^ value
    return result


def hamming_distance(a: int, b: int) -> int:
    """Count how many bit positions differ between two integers."""
    return count_set_bits(a ^ b)


def is_power_of_two(value: int) -> bool:
    """Check whether a positive integer is a power of two."""
    return value > 0 and (value & (value - 1)) == 0


def bitmask_to_set(mask: int) -> list[int]:
    """Return the indices of set bits from a bitmask."""
    indices: list[int] = []
    bit_index = 0

    while mask:
        if mask & 1:
            indices.append(bit_index)
        mask >>= 1
        bit_index += 1

    return indices


def generate_subsets(items: list[int]) -> list[list[int]]:
    """Generate all subsets using bitmasking for a small list."""
    result: list[list[int]] = []
    total = 1 << len(items)

    for mask in range(total):
        subset = []
        for index, value in enumerate(items):
            if mask & (1 << index):
                subset.append(value)
        result.append(subset)
    return result


def rotate_left(value: int, shifts: int, width: int = 8) -> int:
    """Rotate bits to the left while keeping the bit width fixed."""
    shifts %= width
    mask = (1 << width) - 1
    return ((value << shifts) | (value >> (width - shifts))) & mask


def swap_without_temp(a: int, b: int) -> tuple[int, int]:
    """Swap two integers without a temporary variable using XOR."""
    a ^= b
    b ^= a
    a ^= b
    return a, b


# ------------------------------
# Recursion
# ------------------------------
def factorial_recursive(n: int) -> int:
    """Compute n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n: int) -> int:
    """Compute the nth Fibonacci number using naive recursion."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def power_recursive(base: int, exponent: int) -> int:
    """Compute base^exponent using recursion."""
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)


def binary_search_recursive(nums: list[int], target: int, left: int = 0, right: int | None = None) -> int:
    """Binary search using recursion."""
    if right is None:
        right = len(nums) - 1
    if left > right:
        return -1
    middle = (left + right) // 2
    if nums[middle] == target:
        return middle
    if nums[middle] > target:
        return binary_search_recursive(nums, target, left, middle - 1)
    return binary_search_recursive(nums, target, middle + 1, right)


# ------------------------------
# Dynamic programming and memoization
# ------------------------------
@lru_cache(maxsize=None)
def fibonacci_dp(n: int) -> int:
    """Compute the nth Fibonacci number with memoization."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci_dp(n - 1) + fibonacci_dp(n - 2)


def climb_stairs(n: int) -> int:
    """Count ways to climb n stairs if you take 1 or 2 steps at a time."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1
    for step in range(2, n + 1):
        ways[step] = ways[step - 1] + ways[step - 2]
    return ways[n]


def coin_change_min_coins(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins needed to make amount, or -1 if impossible."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    inf = float("inf")
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and dp[value - coin] != inf:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return -1 if dp[amount] == inf else int(dp[amount])


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the max total value for a 0/1 knapsack."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for cap in range(capacity + 1):
            if weights[i - 1] <= cap:
                dp[i][cap] = max(
                    dp[i - 1][cap],
                    values[i - 1] + dp[i - 1][cap - weights[i - 1]],
                )
            else:
                dp[i][cap] = dp[i - 1][cap]

    return dp[n][capacity]


def longest_common_subsequence(text1: str, text2: str) -> int:
    """Return the length of the LCS between two strings."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# ------------------------------
# Backtracking and greedy
# ------------------------------
def generate_subsets_backtracking(nums: list[int]) -> list[list[int]]:
    """Generate all subsets using backtracking."""
    result: list[list[int]] = []

    def dfs(start: int, path: list[int]) -> None:
        result.append(path.copy())
        for index in range(start, len(nums)):
            path.append(nums[index])
            dfs(index + 1, path)
            path.pop()

    dfs(0, [])
    return result


def activity_selection(start_times: list[int], end_times: list[int]) -> list[tuple[int, int]]:
    """Select the maximum number of non-overlapping activities using greedy logic."""
    activities = sorted(zip(start_times, end_times), key=lambda pair: pair[1])
    selected: list[tuple[int, int]] = []
    last_end = -1

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


# ------------------------------
# Examples runner
# ------------------------------
def run_examples() -> None:
    """Run representative Day 2 examples and important DSA patterns."""
    print("Rightmost set bit of 12:", rightmost_set_bit(12))
    print("Set bits in 13:", count_set_bits(13))
    print("Single number I:", single_number([2, 2, 1, 4, 4, 5, 5]))
    print("Single number II:", single_number_ii([2, 2, 2, 3]))
    print("Single number III:", single_number_iii([1, 2, 1, 3, 2, 5]))
    print("Missing number in [0..4]:", missing_number([0, 1, 3, 4]))
    print("Hamming distance between 13 and 9:", hamming_distance(13, 9))
    print("Is 16 a power of two?", is_power_of_two(16))
    print("Set bits from mask 13:", bitmask_to_set(13))
    print("Subsets of [1, 2, 3]:", generate_subsets([1, 2, 3]))
    print("Rotate left 00001101 by 2 bits:", bin(rotate_left(13, 2, 8)))
    print("Swap 10 and 20 without temp:", swap_without_temp(10, 20))

    print("\nRecursive examples:")
    print("Factorial 5:", factorial_recursive(5))
    print("Fibonacci recursive 7:", fibonacci_recursive(7))
    print("2^6:", power_recursive(2, 6))
    print("Binary search for 8 in [1, 3, 5, 7, 9, 11]:", binary_search_recursive([1, 3, 5, 7, 9, 11], 8))

    print("\nDP examples:")
    print("Fibonacci DP 10:", fibonacci_dp(10))
    print("Ways to climb 5 stairs:", climb_stairs(5))
    print("Min coins for 11 with [1, 2, 5]:", coin_change_min_coins([1, 2, 5], 11))
    print("Knapsack max value:", knapsack_01([10, 20, 30], [60, 100, 120], 50))
    print("LCS length between ABCD and AEDF:", longest_common_subsequence("ABCD", "AEDF"))

    print("\nBacktracking and greedy:")
    print("Subsets backtracking for [1,2,3]:", generate_subsets_backtracking([1, 2, 3]))
    print("Activity selection:", activity_selection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))


if __name__ == "__main__":
    run_examples()
