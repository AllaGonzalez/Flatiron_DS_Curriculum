import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

def y(x, points):
    point_at_x = list(filter(lambda point: point['x'] == x,points))[0]
    return point_at_x['y']

def squared_error(point, m, b):
    return (point['y'] - (m*point['x'] + b))**2

def rss(points, m, b):
    squared_errors = list(map(lambda point: squared_error(point, m, b), points))
    return sum(squared_errors)

def cost_chart_b(points, m, b_values):
    rss_values = list(map(lambda b: rss(points, m, b), b_values))
    return {'b_values': b_values, 'rss_values': rss_values}

# b_values = [65, 70, 75, 80, 85, 90, 95]
#
# cost_chart = cost_chart_b(shows, 1.417, b_values)


def cost_curve_at(b, m, points):
    delta = .01
    base_rss = rss(points, m, b)
    numerator = rss(points, m, b + delta) - base_rss
    slope = numerator/delta
    return {'b': b,'rss': base_rss, 'slope': slope}

def plot(traces):
    plotly.offline.iplot(traces)

def build_tangent_line(b, m, points, line_length = 5):
    curve_at_point = cost_curve_at(b, m, points)
    slope = curve_at_point['slope']
    b_minus = b - line_length
    b_plus = b + line_length
    rss_exact = curve_at_point['rss']
    rss_minus = rss_exact - slope * line_length
    rss_plus = rss_exact + slope * line_length
    return {'x': [b_minus, b, b_plus], 'y': [rss_minus, curve_at_point['rss'], rss_plus], 'mode': 'lines+text', 'text': ['    slope:' + format(slope, '.2f')], 'textposition': 'right'}



# build_tangent_line(40, rss(points, 1.417, ))
# trace = build_tangent_line(cost_chart[0], shows, 1.417, )
# plot([cost_trace, trace])

# m = cost_curve_at(100, 1.417, shows)
# tangent_lines = list(map(lambda b_value: build_tangent_line(b_value, 1.417, shows, 2), [70, 84.61, 90.85]))
# tangent_lines
# cost_trace = {'x': cost_chart['b_values'], 'y': cost_chart['rss_values'], 'mode':'line'}
# plot([cost_trace, *tangent_lines])
