from collections import defaultdict
import operator


def tournamentWinner(competitions, results):
    # Write your code here.
    points = {}
    enum = {0: 1, 1: 0}
    for idx, competition in enumerate(competitions):
        winner_idx = enum[results[idx]]  # 0 or 1
        winner = competition[winner_idx]
        points[winner] = points.get(winner, 0) + 3

    tournament_winner = max(points.items(), key=operator.itemgetter(1))[0]
    return tournament_winner


if __name__ == "__main__":
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    winners = [0, 0, 1]
    print(tournamentWinner(competitions, winners))
