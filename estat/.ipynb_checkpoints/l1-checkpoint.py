import pandas as pd
from scipy import stats

# Defining the data manually based on the file, for simplicity here
data = {
    "Group": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Height": [166, 171, 162, 164, 158, 163, 145, 161, 165, 162, 164, 172, 163, 164, 164, 160, 170, 148, 159, 161, 153, 155, 168, 160, 159, 165, 159, 160, 175, 162, 162, 169, 165, 172, 163, 171, 163, 160, 163, 168, 165, 173, 166, 165, 159, 169, 169, 170, 167, 166, 164, 170, 165, 172, 160, 168, 170, 176, 157, 169],
    "Arm Span": [164, 174, 161, 174, 165, 164, 144, 166, 162, 166, 170, 182, 166, 169, 165, 164, 170, 163, 158, 168, 158, 161, 174, 167, 159, 173, 164, 163, 179, 162, 162, 168, 167, 172, 170, 171, 170, 169, 167, 175, 174, 173, 171, 170, 164, 177, 175, 180, 172, 172, 161, 174, 175, 178, 166, 167, 175, 180, 162, 175],
}

# Create a pandas dataframe
df = pd.DataFrame(data)

# Splitting the data into two groups
group1 = df[df["Group"] == 1]
group2 = df[df["Group"] == 2]

# Performing t-test to compare the height and arm span of both groups
t_stat_height, p_val_height = stats.ttest_ind(group1["Height"], group2["Height"])
t_stat_span, p_val_span = stats.ttest_ind(group1["Arm Span"], group2["Arm Span"])

t_stat_height, p_val_height, t_stat_span, p_val_span
