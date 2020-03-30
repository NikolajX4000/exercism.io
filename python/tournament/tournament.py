from collections import defaultdict


def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    teams = defaultdict(list)
    for row in rows:
        team_1, team_2, outcome = row.split(';')
        teams[team_1].append(1 if outcome == 'win' else 0 if outcome == 'draw' else -1)
        teams[team_2].append(-1 if outcome == 'win' else 0 if outcome == 'draw' else 1)

    scores = {}
    for team, outcomes in teams.items():
        mp = w = d = l = p = 0
        for o in outcomes:
            mp += 1
            if o == 1:
                w += 1
                p += 3
            elif o == 0:
                d += 1
                p += 1
            else:
                l += 1
        scores[team] = {'MP': mp, 'W': w, 'D': d, 'L': l, 'P': p}

    tmp = sorted(list(scores.items()), key=lambda x: x[0])
    for team, stats in sorted(tmp, key=lambda x: (x[1]['P']), reverse=True):
        table.append(
            f"{team.ljust(31)}| {str(stats['MP']).rjust(2)} | {str(stats['W']).rjust(2)} | {str(stats['D']).rjust(2)}"
            f" | {str(stats['L']).rjust(2)} | {str(stats['P']).rjust(2)}")
    return table
