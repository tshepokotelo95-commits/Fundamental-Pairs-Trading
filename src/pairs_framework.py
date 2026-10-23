import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

class FundamentalPairsTrader:
    def __init__(self, asset_a: str, asset_b: str, start_date: str, end_date: str):
        self.asset_a = asset_a
        self.asset_b = asset_b
        self.start = start_date
        self.end = end_date
        self.data = None
        self.hedge_ratio = None
        
    def fetch_market_data(self):
        """Ingests historical daily closing prices from Yahoo Finance API."""
        print(f"[#] Ingesting market architecture for {self.asset_a} and {self.asset_b}...")
        df = yf.download([self.asset_a, self.asset_b], start=self.start, end=self.end)['Adj Close']
        self.data = df.dropna()
        return self.data

    def verify_cointegration(self) -> tuple:
        """
        Executes Engle-Granger two-step cointegration test.
        Establishes long-term fundamental relationship viability.
        """
        score, p_value, _ = coint(self.data[self.asset_a], self.data[self.asset_b])
        
        # Calculate structural hedge ratio via Ordinary Least Squares (OLS) regression
        X = sm.add_constant(self.data[self.asset_b])
        model = sm.OLS(self.data[self.asset_a], X).fit()
        self.hedge_ratio = model.params[self.asset_b]
        
        return score, p_value, self.hedge_ratio

    def generate_execution_signals(self, window: int = 20, entry_z: float = 2.0, exit_z: float = 0.0):
        """
        Generates dynamic z-score signals based on rolling spread deviations.
        """
        # Spread = Asset_A - (Hedge_Ratio * Asset_B)
        spread = self.data[self.asset_a] - (self.hedge_ratio * self.data[self.asset_b])
        
        rolling_mean = spread.rolling(window=window).mean()
        rolling_std = spread.rolling(window=window).std()
        
        z_score = (spread - rolling_mean) / rolling_std
        
        signals = pd.DataFrame(index=self.data.index)
        signals['Spread'] = spread
        signals['Z-Score'] = z_score
        
        # Execution Matrix Logic
        signals['Long_Signal'] = (z_score < -entry_z).astype(int)
        signals['Short_Signal'] = (z_score > entry_z).astype(int)
        signals['Exit_Signal'] = (np.abs(z_score) <= exit_z).astype(int)
        
        return signals

if __name__ == "__main__":
    # Institutional Configuration: Visa vs. Mastercard Duopoly Tracking
    trader = FundamentalPairsTrader(asset_a="V", asset_b="MA", start_date="2023-01-01", end_date="2026-01-01")
    trader.fetch_market_data()
    
    score, p_val, hedge = trader.verify_cointegration()
    print(f"\n[+] Cointegration Verification Architecture:")
    print(f"    - P-Value: {p_val:.4f} (Threshold: < 0.05 for statistical significance)")
    print(f"    - Structural Hedge Ratio: {hedge:.4f}")
    
    if p_val < 0.05:
        print("    - Status: Fundamental relationship verified. Cointegration confirmed.")
    else:
        print("    - Status: High divergence risk. Spreading could represent structural breakdown.")
