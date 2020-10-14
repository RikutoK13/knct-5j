# 利回りシミュレーション

YEARS = 10
AVE_YIELD = 0.05
PRINCIPAL = 100000
RESERVE = 10000

def main():
    money = PRINCIPAL
    print(money)
    for year in range(YEARS * 12):
        money += RESERVE
        money += (AVE_YIELD * money)
        print(money)
    print(money)


if __name__ == "__main__":
    main()