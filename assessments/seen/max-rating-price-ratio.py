"""
Problem Statement:

You are given two lists of equal length: prices (a list of positive floats or integers representing item prices) and ratings (a list of non-negative floats or integers representing item ratings). 
Find and return the highest ratio of ratings[i] / prices[i] for any i where prices[i] != 0.

Assumptions:
- The lists are non-empty and of equal length; otherwise, raise ValueError.
- If all prices are zero or the lists are invalid, raise ValueError.
- Prices are positive, but the code skips zeros to avoid division by zero.

Example:
prices = [10.0, 20.0, 15.0]
ratings = [4.5, 4.0, 4.8]
Output: 0.32  (from 4.8 / 15.0)
"""

def max_rating_price_ratio(prices, ratings):
    if len(prices) != len(ratings) or not prices:
        raise ValueError("Lists must be non-empty and of equal length")
    
    # Using generator to compute ratios, skipping zero prices
    ratios = (r / p for p, r in zip(prices, ratings) if p != 0)
    
    try:
        return max(ratios)
    except ValueError:
        raise ValueError("No valid ratios (all prices zero?)")

# Example usage (for testing):
if __name__ == "__main__":
    prices = [10.0, 20.0, 15.0]
    ratings = [4.5, 4.0, 4.8]
    result = max_rating_price_ratio(prices, ratings)
    print(result)  # Output: 0.32
