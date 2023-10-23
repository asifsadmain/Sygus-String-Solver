import numpy as np
from scipy import stats

# Your list of integers
data = [3682,1672,652,16885,2391,13871,2722,2464,24336,740,1150,5585]

# Calculate the mean and standard error of the mean
mean = np.mean(data)
std_error = np.std(data, ddof=1) / np.sqrt(len(data))

# Degrees of freedom (n-1 for a sample)
degrees_of_freedom = len(data) - 1

# Confidence level (95%)
confidence_level = 0.95

# Calculate the t-score for the given confidence level and degrees of freedom
t_score = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)

# Calculate the margin of error
margin_of_error = t_score * std_error

# Calculate the confidence interval
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print(f"Mean: {mean}")
print(f"95% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
