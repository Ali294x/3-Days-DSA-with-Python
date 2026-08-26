"""Day 2: bit manipulation and core DSA bit tricks."""


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


def run_examples() -> None:
    """Run representative Day 2 examples and special DSA bit patterns."""
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


if __name__ == "__main__":
    run_examples()
