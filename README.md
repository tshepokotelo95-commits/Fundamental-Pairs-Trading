![CI Pipeline](https://github.com/tshepokotelo95-commits/Fundamental-Pairs-Trading/actions/workflows/ci.yml/badge.svg)

# Relative Value Equity Pairs Trading Framework

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A systematic statistical arbitrage environment built to exploit structural pricing dislocations within closely coupled corporate duopolies. This framework implements an Engle-Granger two-step cointegration pipeline to bypass superficial price correlations, isolating pure fundamental relative value anomalies.

---

## 🏛️ Investment Thesis: The Visa (V) vs. Mastercard (MA) Duopoly

Trading individual equity names exposes capital to severe macro, interest rate, and idiosyncratic sector risks. This framework targets a structural duopoly—Visa (V) and Mastercard (MA)—to mitigate broad market beta and harvest clean alpha.

### 1. Economic Moat & Structural Alignment
* **Network Parallelism:** Both corporations operate near-identical capital-light payment processing tollbooths, scaling synchronously with global consumption and inflation layers.
* **Operating Leverage:** Because their cost structures are highly fixed, variations in their respective gross processing volumes (GPV) directly flow to operating margins under identical macroeconomic conditions.

### 2. Relative Value Dislocation
While their long-term underlying business economics are cointegrated, short-term price spreads diverge due to transitory institutional flow imbalances, localized earnings reporting variances, or asymmetric liquidity shocks. This framework programmatically quantifies these temporary pricing gaps to execute market-neutral mean-reversion trades.

---

## 🛠️ Quantitative Architecture & Signal Mechanics

The model abandons naive chart-pattern tracking in favor of a mathematically rigorous relative value framework.

### 1. Engle-Granger Two-Step Cointegration Test
To prevent entering "spurious regressions" (assets that look correlated but have zero economic linkage), the engine continuously verifies the stationarity of the spread:
* **OLS Regression Analysis:** Runs an Ordinary Least Squares (OLS) regression of $Asset_A$ against $Asset_B$ to dynamically calculate the structural Hedge Ratio ($\beta$).
* **Augmented Dickey-Fuller (ADF):** Tests the residual spread tracking error for stationarity. If the p-value falls below 0.05, the relationship is fundamentally verified as mean-reverting.

---

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/tshepokotelo95-commits/Fundamental-Pairs-Trading.git](https://github.com/tshepokotelo95-commits/Fundamental-Pairs-Trading.git)
cd Fundamental-Pairs-Trading

# Run pairs trading framework
python src/pairs_framework.py
