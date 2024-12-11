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

            if stone == 0:
                insert_into_dict(stones, stones_count, 1)
                stones[0] -= stones_count

            else:
                stone_str = str(stone)
                stone_len = len(stone_str)
                if stone_len % 2 == 0:
                    l, r = int(stone_str[:stone_len//2]), int(stone_str[stone_len//2:])
                    insert_into_dict(stones, stones_count, l)
                    insert_into_dict(stones, stones_count, r)
                    stones[stone] -= stones_count
                else:
                    insert_into_dict(stones, stones_count, stone*2024)
                    stones[stone] -= stones_count
    return stones

def main():
    stones = dict()
    num_blinks = 25

    with open("input.txt") as file:
        for stone in file.read().strip().split(" "):
            stone_int = int(stone)
            if stone_int not in stones:
                stones[stone_int] = 0
            stones[stone_int] += 1

    print(sum(get_stones_after_blink(stones, num_blinks).values()))

if __name__ == "__main__":
    test_time(main)
