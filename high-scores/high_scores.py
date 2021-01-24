def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse = True)
    if len(scores) < 3:
        return scores
    a = scores[0]
    b = scores[1]
    c = scores[2]
    return [a,b,c]
