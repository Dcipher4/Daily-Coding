questions = [
    ["What is the primary purpose of a saving bank account?", "To invest in stocks", "To save money and earn interest", "To pay off loans", "To buy a car", 2],
    ["What is a credit score?", "A number that represents a person's creditworthiness", "A score given for a good investment", "The amount of credit available", "The interest rate on a loan", 1],
    ["What is the purpose of an emergency fund?", "To invest in the stock market", "To pay for vacations", "To cover unexpected expenses", "To buy a house", 3],
    ["What is the primary purpose of a hedge fund?", "To provide loans to small businesses", "To hedge against currency fluctuations", "To generate high returns through various investment strategies", "To offer low-risk investment options", 3],
    ["What does the term 'arbitrage' refer to?", "Investing in different asset classes to diversify risk", "Simultaneously buying and selling an asset to profit from price differences", "Using leverage to amplify investment returns", "Predicting market trends based on historical data", 2],
    ["What is a credit default swap (CDS)?", "A financial derivative used to hedge against the risk of credit default", "A type of loan given to high-risk borrowers", "A method for calculating a company's credit rating", "A strategy for reducing interest rates on loans", 1],
    ["What is the Efficient Market Hypothesis (EMH)?", "A theory stating that stock prices reflect all available information", "A method for calculating the intrinsic value of a stock", "A strategy for minimizing investment risk", "A technique for predicting stock market crashes", 1],
    ["What is the Capital Asset Pricing Model (CAPM) used for?", "To determine the cost of equity and the expected return on an investment", "To calculate the net present value of future cash flows", "To assess the default risk of a borrower", "To measure the liquidity of an asset", 1],
    ["What is the Sharpe Ratio?", "A measure of the volatility of an asset", "A metric for comparing the risk-adjusted return of an investment", "An index for tracking stock performance", "A technique for diversifying a portfolio", 2],
    ["What is a 'junk bond'?", "A bond with a high credit rating", "A bond issued by a government", "A high-yield, high-risk bond", "A bond with no fixed interest rate", 3],
    ["What does 'beta' measure in finance?", "The market capitalization of a company", "The creditworthiness of a borrower", "The sensitivity of a stock's returns to market returns", "The liquidity of an asset", 3],
    ["What is the Modigliani-Miller Theorem?", "A theory on the impact of dividends on stock prices", "A theory on capital structure irrelevance in a perfect market", "A method for valuing derivative securities", "A framework for pricing options", 2],
    ["What is 'alpha' in investment performance?", "The average return of the market", "The excess return of an investment relative to the return of a benchmark index", "The volatility of an investment's returns", "The correlation of an investment's returns with the market returns", 2],
    ["What is the difference between the 'delta' and 'gamma' of an option?", "Delta measures the price sensitivity to changes in the underlying asset, while gamma measures the rate of change of delta", "Delta measures time decay, while gamma measures volatility", "Delta measures volatility, while gamma measures interest rate sensitivity", "Delta measures the price sensitivity to changes in interest rates, while gamma measures the price sensitivity to changes in the underlying asset", 1],
    ["What is the meaning of the term 'convexity' in bond investing?", "The rate at which the duration of a bond changes with interest rates", "The sensitivity of a bond's price to interest rate changes", "The measure of a bond's credit risk", "The difference between a bond's yield and its coupon rate", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}") 
    print(f"a. {question[1]}   b. {question[2]} ")
    print(f"c. {question[3]}   d. {question[4]} ") 
    reply = int(input("Enter your answer (1-4): "))
    if reply == question[5]:
        print(f"Correct answer!! Congratulations! You have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer! Game over!")
        break
