from PerformanceTester.PerformanceTester import test_time

def insert_into_dict(stones, num, new):
    if new not in stones:
        stones[new] = 0
    stones[new] += num

def get_stones_after_blink(stones, num_blinks):
    for i in range(num_blinks):
        stones_copy = stones.copy()
        for stone in stones_copy:
            if stones_copy[stone] == 0:
                continue
            stones_count = stones_copy[stone]
            stones[stone] -= stones_count

            if stone == 0:
                stones[1] = stones.get(1, 0) + stones_count
            else:
                stone_str = str(stone)
                stone_len = len(stone_str)
                if stone_len % 2 == 0:
                    half = stone_len // 2
                    l, r = int(stone_str[:half]), int(stone_str[half:])
                    stones[l] = stones.get(l, 0) + stones_count
                    stones[r] = stones.get(r, 0) + stones_count
                else:
                    new_stone = stone * 2024
                    stones[new_stone] = stones.get(stone * 2024, 0) + stones_count
    return stones

def main():
    stones = {}
    num_blinks = 25

    with open("input.txt") as file:
        for stone in map(int, file.read().strip().split()):
            stones[stone] = stones.get(stone, 1)

    print(sum(get_stones_after_blink(stones, num_blinks).values()))

if __name__ == "__main__":
    test_time(main)
