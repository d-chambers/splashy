# AUTOGENERATED! DO NOT EDIT! File to edit: 010_finite_diff.ipynb (unless otherwise specified).

__all__ = ["get_stencil", "apply_stencil"]

# Cell
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# define functions for getting stencile


def _get_dx_factors(num_points):
    """
    returns the factors of dx for each sampled point.

    EG, f(x - dx) + f(x) + f(x + dx) would return -1, 0, 1
    """
    assert num_points % 2 == 1, "must use an odd number of points!"
    forward = np.arange(1, num_points // 2 + 1)
    backward = -forward[::-1]
    return np.concatenate([backward, [0], forward])


# export
def get_stencil(derivative: int, num_points: int, dx: float = 1.0) -> np.ndarray:
    """
    Create a symetric stencile for a defined derivative with a certain number of points.

    """

    dx_factors = _get_dx_factors(num_points)

    power = np.power.outer(dx_factors, np.arange(len(dx_factors))).T
    fact = np.atleast_2d(factorial(np.abs(dx_factors)))

    kernel = power / fact

    y = np.zeros(len(kernel))
    y[derivative] = factorial(derivative) / (dx ** derivative)

    out = np.linalg.inv(kernel) @ y
    return out


# export
def apply_stencil(array, stencil):
    """Apply the stencil."""
    center_ind = len(stencil) // 2
    out = np.convolve(array, stencil[::-1], mode="same")
    return out
