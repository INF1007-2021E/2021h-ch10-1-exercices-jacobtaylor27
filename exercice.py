#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(x**2 + y**2), np.arctan2(y, x)) for x,y in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.absolute(values - number).argmin()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(coordinate_conversion(np.array([(15,30), (11,15), (8,12)])))
    print(find_closest_index(np.array([18,10,15,16]), 10.5))
