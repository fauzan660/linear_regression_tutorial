import numpy as np

def get_cases(seed=42):
    np.random.seed(seed)

    return [
        # {
        #     "name": "clean_linear_small",
        #     "X": np.array([1, 2, 3, 4, 5]),
        #     "y": np.array([2, 4, 6, 8, 10])
        # },
        {
            "name": "clean_linear_small",
            "X": np.array([1, 2, 3, 4, 5]),
            "y": np.array([2, 5, 18, 22, 27])
        },
        {
            "name": "noisy_linear_large",
            "X": np.linspace(0, 50, 500),
            "y": 3*np.linspace(0, 50, 500) + 7 + np.random.randn(500) * 5
        },
        {
            "name": "poorly_scaled",
            "X": np.array([1, 100, 1000, 10000]),
            "y": np.array([3, 300, 3000, 30000])
        },
        # {
        #     "name": "multi_feature",
        #     "X": np.array([[1, 1],
        #                    [2, 1],
        #                    [3, 2],
        #                    [4, 3],
        #                    [5, 3]]),
        #     "y": np.array([2, 3, 5, 7, 8])
        # },
        {
            "name": "very_noisy",
            "X": np.linspace(0, 10, 50),
            "y": 2*np.linspace(0, 10, 50) + 5 + np.random.randn(50) * 10
        }
    ]
