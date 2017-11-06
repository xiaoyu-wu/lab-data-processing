from scipy.optimize import fsolve
from scipy.interpolate import InterpolatedUnivariateSpline

def from_y_to_x(xs, ys, y_value, guess_x_value=0):
    curve = InterpolatedUnivariateSpline(xs, ys)
    func = lambda x: curve(x) - y_value
    solution = fsolve(func, guess_x_value)[0]
    return solution