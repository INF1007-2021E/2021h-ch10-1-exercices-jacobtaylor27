#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import random as r
import matplotlib.pyplot as plt

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(x**2 + y**2), np.arctan2(y, x)) for x,y in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.absolute(values - number).argmin()


def plot_points():
    x = np.linspace(-1, 1, 250)
    y = x**2 * np.sin(1 / x**2) + x

    plt.scatter(x, y)
    plt.show()


def plot_pi_monte_carlo(iteration=5000):
    plt.title("Calcul de pi par la méthode de Monte Carlo.")
    plt.xlabel('X')
    plt.ylabel('Y')

    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for i in range(iteration):
        x = np.random.random()
        y = np.random.random()

        if np.sqrt(x*x + y*y) <= 1.0:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    plt.scatter(x_inside, y_inside)
    plt.scatter(x_outside, y_outside)
    plt.show()
    return len(x_inside) / iteration * 4

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(coordinate_conversion(np.array([(15,30), (11,15), (8,12)])))
    print(find_closest_index(np.array([18,10,15,16]), 10.5))
    # plot_points()
    print(plot_pi_monte_carlo(iteration=10000))
