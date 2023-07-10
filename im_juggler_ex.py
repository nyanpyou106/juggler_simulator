import enum

# ベルとピエロは狙わないのでないものとして扱う。
BIG_COIN = 252
REG_COIN = 96
GRAPE_COIN = 8
CHERRY_COIN = 1
REPLAY_COIN = 3
NO_COIN = 0  # 外れを引いた時


class SETTING_1(enum.Enum):
    BIG = (1 / 273.1, BIG_COIN)
    REG = (1 / 439.8, REG_COIN)
    GRAPE = (1 / 6.02, GRAPE_COIN)
    CHERRY = (1 / 35.62, CHERRY_COIN)
    REPLAY = (1 / 7.3, REPLAY_COIN)
    NO = (0, NO_COIN)

    def __init__(self, probability, coins) -> None:
        self.probability = probability
        self.coins = coins

    @classmethod
    def caliculate_no_coin_probability(self):
        """
        外れの確率を計算して値を投入する。
        """
        p = (
            1
            - self.BIG.probability
            - self.REG.probability
            - self.GRAPE.probability
            - self.CHERRY.probability
            - self.REPLAY.probability
        )
        self.NO.probability = p


class SETTING_2(enum.Enum):
    BIG = (1 / 269.7, BIG_COIN)
    REG = (1 / 399.6, REG_COIN)
    GRAPE = (1 / 6.02, GRAPE_COIN)
    CHERRY = (1 / 35.62, CHERRY_COIN)
    REPLAY = (1 / 7.3, REPLAY_COIN)
    NO = (0, NO_COIN)

    def __init__(self, probability, coins) -> None:
        self.probability = probability
        self.coins = coins

    @classmethod
    def caliculate_no_coin_probability(self):
        """
        外れの確率を計算して値を投入する。
        """
        p = (
            1
            - self.BIG.probability
            - self.REG.probability
            - self.GRAPE.probability
            - self.CHERRY.probability
            - self.REPLAY.probability
        )
        self.NO.probability = p


class SETTING_3(enum.Enum):
    BIG = (1 / 269.7, BIG_COIN)
    REG = (1 / 331.0, REG_COIN)
    GRAPE = (1 / 6.02, GRAPE_COIN)
    CHERRY = (1 / 35.62, CHERRY_COIN)
    REPLAY = (1 / 7.3, REPLAY_COIN)
    NO = (0, NO_COIN)

    def __init__(self, probability, coins) -> None:
        self.probability = probability
        self.coins = coins

    @classmethod
    def caliculate_no_coin_probability(self):
        """
        外れの確率を計算して値を投入する。
        """
        p = (
            1
            - self.BIG.probability
            - self.REG.probability
            - self.GRAPE.probability
            - self.CHERRY.probability
            - self.REPLAY.probability
        )
        self.NO.probability = p


class SETTING_4(enum.Enum):
    BIG = (1 / 259.0, BIG_COIN)
    REG = (1 / 315.1, REG_COIN)
    GRAPE = (1 / 6.02, GRAPE_COIN)
    CHERRY = (1 / 35.62, CHERRY_COIN)
    REPLAY = (1 / 7.3, REPLAY_COIN)
    NO = (0, NO_COIN)

    def __init__(self, probability, coins) -> None:
        self.probability = probability
        self.coins = coins

    @classmethod
    def caliculate_no_coin_probability(self):
        """
        外れの確率を計算して値を投入する。
        """
        p = (
            1
            - self.BIG.probability
            - self.REG.probability
            - self.GRAPE.probability
            - self.CHERRY.probability
            - self.REPLAY.probability
        )
        self.NO.probability = p


class SETTING_5(enum.Enum):
    BIG = (1 / 259.0, BIG_COIN)
    REG = (1 / 255.0, REG_COIN)
    GRAPE = (1 / 6.02, GRAPE_COIN)
    CHERRY = (1 / 35.62, CHERRY_COIN)
    REPLAY = (1 / 7.3, REPLAY_COIN)
    NO = (0, NO_COIN)

    def __init__(self, probability, coins) -> None:
        self.probability = probability
        self.coins = coins

    @classmethod
    def caliculate_no_coin_probability(self):
        """
        外れの確率を計算して値を投入する。
        """
        p = (
            1
            - self.BIG.probability
            - self.REG.probability
            - self.GRAPE.probability
            - self.CHERRY.probability
            - self.REPLAY.probability
        )
        self.NO.probability = p


class SETTING_6(enum.Enum):
    BIG = (1 / 255.0, BIG_COIN)
    REG = (1 / 255.0, REG_COIN)
    GRAPE = (1 / 5.78, GRAPE_COIN)
    CHERRY = (1 / 35.62, CHERRY_COIN)
    REPLAY = (1 / 7.3, REPLAY_COIN)
    NO = (0, NO_COIN)

    def __init__(self, probability, coins) -> None:
        self.probability = probability
        self.coins = coins

    @classmethod
    def caliculate_no_coin_probability(self):
        """
        外れの確率を計算して値を投入する。
        """
        p = (
            1
            - self.BIG.probability
            - self.REG.probability
            - self.GRAPE.probability
            - self.CHERRY.probability
            - self.REPLAY.probability
        )
        self.NO.probability = p


SETTING_LIST = [SETTING_1, SETTING_2, SETTING_3, SETTING_4, SETTING_5, SETTING_6]
