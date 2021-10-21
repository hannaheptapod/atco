h, w = map(int, input().split())
a = ['#'*(w + 2)] + ['#' + input() + '#' for _ in range(h)] + ['#'*(w + 2)]
_ = [print(ai) for ai in a]