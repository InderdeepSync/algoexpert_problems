
def inner(cups, low, high):
    if not cups:
        return False

    cup = cups[0]
    cupL, cupH = cup

    res = False
    while low >= 0 and high > 0:
        res = res or inner(cups[1:], low, high)
        low -= cupL
        high -= cupH

    return res or (low <= 0 and high >= 0)



def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    measuringCups.sort(key=lambda c: c[0])
    res = inner(measuringCups, low, high)

    return res


if __name__ == "__main__":
    print(ambiguousMeasurements([
  [50, 65],
  [100, 120],
  [20, 40],
  [10, 15],
  [400, 500],
  [300, 350],
  [10, 25]
], 3000, 3300))