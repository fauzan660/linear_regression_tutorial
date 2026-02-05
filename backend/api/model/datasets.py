import numpy as np

def get_cases(seed=42):
    np.random.seed(seed)

    return [
        {
            "name": "perfect_linear",
            "X": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            "y": np.array([5, 7, 9, 11, 13, 15, 17, 19, 21, 23])   # y = 2x + 3
        },
        {
            "name": "non_linear",
            "X": np.array([1,2,3,4,5,6,7,8,9,10]),
            "y": np.array([1,4,9,16,25,36,49,64,81,100])   # y = x^2
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
        {
            "name": "very_noisy",
            "X": np.linspace(0, 10, 50),
            "y": 2*np.linspace(0, 10, 50) + 5 + np.random.randn(50) * 10
        }
    ]
