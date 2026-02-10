import numpy as np

np.random.seed(0)

scores = np.random.randint(50, 101, size=(5, 3))
print("original scores:")
print(scores)

mean_scores = np.mean(scores, axis=0)

centered_scores = scores - mean_scores
print("\nCentered scores:")
print(centered_scores)