def main():
    score = float(input("Enter score: "))
    print(get_score(score))


def get_score(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 50 and score < 90:
            return "Passable"
        elif score >= 90:
            return "Excellent"
        elif score < 50:
            return "Bad"


main()
