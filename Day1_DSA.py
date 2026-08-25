"""Day 1: Array mastery and advanced manipulation."""

from collections import Counter
from itertools import accumulate


def build_prefix_sums(numbers: list[int]) -> list[int]:
	"""Return the running sum at each position."""
	return list(accumulate(numbers))


def range_sum(prefix_sums: list[int], start: int, end: int) -> int:
	"""Return the inclusive range sum using a prefix-sum array."""
	before_start = prefix_sums[start - 1] if start > 0 else 0
	return prefix_sums[end] - before_start


def apply_range_updates(
	size: int, updates: list[tuple[int, int, int]]
) -> list[int]:
	"""Apply inclusive range additions in O(size + len(updates)) time."""
	difference = [0] * (size + 1)

	for start, end, value in updates:
		difference[start] += value
		difference[end + 1] -= value

	result: list[int] = []
	current = 0
	for value in difference[:size]:
		current += value
		result.append(current)
	return result


def subarray_sum_count(numbers: list[int], target: int) -> int:
	"""Count contiguous subarrays whose sum equals target."""
	prefix_frequency = Counter({0: 1})
	prefix_sum = 0
	count = 0

	for number in numbers:
		prefix_sum += number
		count += prefix_frequency[prefix_sum - target]
		prefix_frequency[prefix_sum] += 1

	return count


def search_rotated(numbers: list[int], target: int) -> int:
	"""Return target's index in a rotated sorted array, or -1 if absent."""
	left, right = 0, len(numbers) - 1

	while left <= right:
		middle = (left + right) // 2
		if numbers[middle] == target:
			return middle

		if numbers[left] <= numbers[middle]:
			if numbers[left] <= target < numbers[middle]:
				right = middle - 1
			else:
				left = middle + 1
		elif numbers[middle] < target <= numbers[right]:
			left = middle + 1
		else:
			right = middle - 1

	return -1


def run_examples() -> None:
	"""Run representative Day 1 examples."""
	numbers = [1, 2, 3, 4]
	prefix_sums = build_prefix_sums(numbers)
	print("Prefix sums:", prefix_sums)
	print("Range sum [1, 3]:", range_sum(prefix_sums, 1, 3))

	updates = [(1, 3, 2), (2, 4, 3)]
	print("Difference-array updates:", apply_range_updates(5, updates))

	print("Subarrays summing to 3:", subarray_sum_count([1, 2, 1, 2], 3))
	print("Rotated-array index of 0:", search_rotated([4, 5, 6, 7, 0, 1, 2], 0))


if __name__ == "__main__":
	run_examples()
