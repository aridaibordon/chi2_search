import numpy as np

from chi2_search.model import get_chi2, get_chi2_scale_factor


def get_best_fit(sample_data: list[tuple], synthetic_data: list[tuple]) -> tuple:
    output = [(None, None) for _ in range(len(sample_data))]

    for ind, (x_sample, y_sample) in enumerate(sample_data):
        min_chi2 = np.inf
        for x, y, params in synthetic_data:
            chi2 = get_chi2(x, y, x_sample, y_sample)

            if chi2 < min_chi2:
                min_chi2 = chi2

                a = get_chi2_scale_factor(x, y, x_sample, y_sample)
                output[ind] = (x, a * y), params

    return output
