import numpy as np
import im_juggler_ex

MACHINE = im_juggler_ex

for setting in MACHINE.SETTING_LIST:
    setting.caliculate_no_coin_probability()
    probability_list = []
    coins_list = []
    for payment in setting:
        probability_list.append(payment.probability)
        coins_list.append(payment.coins)
    # print(probability_list)
    # print(coins_list)
    # 3000G遊戯を500回行って獲得枚数の標本平均を出力
    sample_list = []
    for _ in range(500):
        earned_coins = 0
        for _ in range(3000):
            # 1回転毎に必ず3枚減少
            earned_coins = earned_coins - 3
            pay_coins = np.random.choice(coins_list, p=probability_list)
            earned_coins = earned_coins + pay_coins
        sample_list.append(earned_coins)
    print(f"{setting.__name__}獲得差枚数平均:{np.average(sample_list)}枚")
