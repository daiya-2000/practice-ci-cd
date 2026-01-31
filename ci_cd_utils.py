"""CI/CD向けの小さなサンプル関数集。"""

from __future__ import annotations


def calculate_total(price: float, tax_rate: float = 0.1) -> float:
    """
    税込み価格を計算する。

    例:
        price=1000, tax_rate=0.1 -> 1100.0
    """

    # 入力は数値である必要がある
    if not isinstance(price, (int, float)):
        raise ValueError("price must be a number")
    if not isinstance(tax_rate, (int, float)):
        raise ValueError("tax_rate must be a number")

    # マイナス値は許可しない
    if price < 0:
        raise ValueError("price must be non-negative")
    if tax_rate < 0:
        raise ValueError("tax_rate must be non-negative")

    # 税込み価格 = 価格 × (1 + 税率)
    return price * (1 + tax_rate)
