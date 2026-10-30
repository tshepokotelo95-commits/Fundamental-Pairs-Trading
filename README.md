# Relative Value Equity Pairs Trading Framework

![CI Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A systematic statistical arbitrage environment built to exploit structural pricing dislocations within closely coupled corporate duopolies. This framework implements an Engle-Granger two-step cointegration pipeline to bypass superficial price correlations, isolating pure fundamental relative value anomalies.

## 🏛 Investment Thesis: The Visa (V) vs. Mastercard (MA) Duopoly

Trading individual equity names exposes capital to severe macro, interest rate, and idiosyncratic sector risks. This framework targets a structural duopoly—Visa (V) and Mastercard (MA)—to mitigate broad market beta and harvest clean alpha.

### 1. Economic Moat & Structural Alignment
* **Network Parallelism:** Both corporations operate near-identical capital-light payment processing tollbooths, scaling synchronously with global consumption and inflation layers.
* **Operating Leverage:** Because their cost structures are highly fixed, variations in their respective gross processing volumes (GPV) directly flow to operating margins under identical macroeconomic conditions.

### 2. Relative Value Dislocation
While their long-term underlying business economics are cointegrated, short-term price spreads diverge due to transitory institutional flow imbalances, localized earnings reporting variances, or asymmetric liquidity shocks. This framework programmatically quantifies these temporary pricing gaps to execute market-neutral mean-reversion trades.

## 🛠 Quantitative Architecture & Signal Mechanics

The model abandons naïve chart-pattern tracking in favor of a mathematically rigorous relative value framework.

### 1. Engle-Granger Two-Step Cointegration Test
To prevent entering "spurious regressions" (assets that look correlated but have zero economic linkage), the engine continuously verifies the stationarity of the spread:
* **OLS Regression Analysis:** Runs an Ordinary Least Squares (OLS) regression of asset prices to derive the hedge ratio ($\beta$).
* **Augmented Dickey-Fuller (ADF) Test:** Evaluates the residuals of the cointegrating regression to confirm mean-reverting properties.

### 2. Z-Score Execution Banding
* **Dynamic Spread Normalization:** Calculates rolling Z-scores of the cointegration residuals.
* **Execution Triggers:** Automatically scales entries when the spread exceeds historical volatility thresholds ($\pm 2.0\sigma$) and exits upon mean reversion to baseline parity.

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/tshepokotelo95-commits/Fundamental-Pairs-Trading.git](https://github.com/tshepokotelo95-commits/Fundamental-Pairs-Trading.git)
cd Fundamental-Pairs-Trading

# Install
