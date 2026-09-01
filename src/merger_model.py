def calculate_merger(
    buyer_net_income,
    target_net_income,
    purchase_price,
    cash_financing,
    debt_financing,
    stock_financing,
    interest_rate,
    tax_rate,
    synergies,
    buyer_shares,
    new_shares,
):
    interest_expense = (
        debt_financing * interest_rate
    )

    after_tax_interest = (
        interest_expense * (1 - tax_rate)
    )

    pro_forma_net_income = (
        buyer_net_income
        + target_net_income
        + synergies
        - after_tax_interest
    )

    pro_forma_shares = (
        buyer_shares + new_shares
    )

    pro_forma_eps = (
        pro_forma_net_income
        / pro_forma_shares
    )

    buyer_eps = (
        buyer_net_income
        / buyer_shares
    )

    accretion_dilution = (
        pro_forma_eps / buyer_eps - 1
    )

    return {
        "purchase_price": purchase_price,
        "cash_financing": cash_financing,
        "debt_financing": debt_financing,
        "stock_financing": stock_financing,
        "interest_expense": interest_expense,
        "after_tax_interest": after_tax_interest,
        "pro_forma_net_income": pro_forma_net_income,
        "pro_forma_shares": pro_forma_shares,
        "buyer_eps": buyer_eps,
        "pro_forma_eps": pro_forma_eps,
        "accretion_dilution": accretion_dilution,
    }
