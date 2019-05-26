from error import residual_sum_squares
def slope_at(x_values, y_values, m, b):
    delta = .0001
    base_rss = residual_sum_squares(x_values, y_values, m, b)
    delta_rss = residual_sum_squares(x_values, y_values, m + delta, b)
    numerator = delta_rss - base_rss
    slope = numerator/delta
    return {'m': m, 'slope': slope}
