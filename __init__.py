import numpy as np

from chi2_search.model import get_chi2


def get_best_fit(x_sample: list, y_sample: list, synthetic_data: list[tuple]) -> tuple:
    min_chi2 = np.inf
    for x, y, params in synthetic_data:
        chi2 = get_chi2(x, y, x_sample, y_sample)

        if chi2 < min_chi2:
            min_chi2 = chi2

            best_fit, best_params = (x, y), params

    return best_fit, best_params
