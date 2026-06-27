import numpy as np

# A vector - same as what 3b1b draws as an arrow
v = np.array([3, -2])

# The two basis vectors i-hat and j-hat
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])

# Linear combination: 3*i_hat + (-2)*j_hat should equal v
result = 3 * i_hat + (-2) * j_hat

print("v =", v)
print("3*i + (-2)*j =", result)
print("They match:", np.array_equal(v, result))