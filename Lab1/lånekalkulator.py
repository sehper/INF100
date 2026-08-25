house_price = 1_500_000
deductible = 280_000
yearly_interest_rate_pct = 7.5
years = 30
monthly_fee = 65


# Computation
loan = house_price - deductible
months = years * 12

yearly_rate = yearly_interest_rate_pct / 100
monthly_rate = yearly_rate / 12

discount_factor = (1 - (1 + monthly_rate) ** -months) / monthly_rate
monthly_term_amount = loan / discount_factor + monthly_fee
monthly_term_amount = round(monthly_term_amount, 2)


# Output
print(f'Monthly term amount: {monthly_term_amount}')


'''Endre input-seksjonen av programmet slik at

huset koster 1.5 millioner,
egenkapitalen er 280 000,
renten er 7.5%, og
nedbetalingstiden er 30 år.
Hvilken verdi får variabelen discount_factor?

Ta et skjermbilde som du navngir discount_factor.png eller discount_factor.jpg. Bildet skal vise:

et skjermbilde av Visual Studio Code, der
debug-modus er aktivt, og
variabelen discount_factor med tilhørende verdi er synlig i variabel-vinduet.
'''