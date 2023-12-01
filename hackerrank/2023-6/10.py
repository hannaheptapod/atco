def main():
    player = int(input())
    scotch_pos = int(input())

    first_moves = map(int, input().split())
    second_moves = map(int, input().split())
    bid = calculate_bid(player, scotch_pos, first_moves, second_moves)
    print(bid)


def calculate_bid(player, scotch_pos, first_moves, second_moves):
    if player == 1:
        rm = 100 - sum(first_moves)
        return min(max(0, rm - scotch_pos), rm // scotch_pos)

    rm = 100 - sum(second_moves)
    return min(max(0, rm - (10 - scotch_pos)), rm // (10 - scotch_pos))


if __name__ == '__main__': main()
