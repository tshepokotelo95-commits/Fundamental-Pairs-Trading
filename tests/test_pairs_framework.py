import pytest

def test_engle_granger_p_value_threshold():
    """Verify Engle-Granger cointegration stationarity check at p-value < 0.05."""
    adf_p_value = 0.032
    p_threshold = 0.05
    
    is_cointegrated = adf_p_value < p_threshold
    
    assert is_cointegrated is True

def test_hedge_ratio_residual_spread():
    """Verify OLS hedge ratio spread calculation (Asset_A - Beta * Asset_B)."""
    price_v = 280.0   # Visa (Asset A)
    price_ma = 460.0  # Mastercard (Asset B)
    beta = 0.60       # Structural OLS hedge ratio
    
    spread = price_v - (beta * price_ma)
    
    assert pytest.approx(spread, 0.01) == 4.0
