from enum import Enum

class VinylState(Enum, str):
    MINT = "mint",
    NEAR_MINT = "near_mint",
    VERY_GOOD_PLUS = "very_good_plus",
    VERY_GOOD = "very_good",
    GOOD_PLUS = "good_plus",
    GOOD = "good",
    FAIR = "fair",
    POOR = "poor"