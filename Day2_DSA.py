"""Day 2: bit manipulation and low-level optimization."""


def rightmost_set_bit(value: int) -> int:
    """Return the lowest set bit using the bit trick x & -x."""
    return value & -value


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


def run_examples() -> None:
    """Run representative Day 2 examples."""
    print("Rightmost set bit of 12:", rightmost_set_bit(12))
    print("Single number I:", single_number([2, 2, 1, 4, 4, 5, 5]))
    print("Single number II:", single_number_ii([2, 2, 2, 3]))
    print("Single number III:", single_number_iii([1, 2, 1, 3, 2, 5]))
    print("Is 16 a power of two?", is_power_of_two(16))
    print("Set bits from mask 13:", bitmask_to_set(13))


if __name__ == "__main__":
    run_examples()
