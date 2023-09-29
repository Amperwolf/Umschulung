# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


def sort_list(item):
    return (item[1], item[0])


if __name__ == "__main__":
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        names_scores.append([name, score])

    print(sorted(names_scores, key=sort_list))

    