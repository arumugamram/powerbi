import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Sample data with all months
data = {
    'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': [
        500_000, 620_000, 700_000, 850_000,
        1_600_000, 1_800_000, 2_000_000, 2_200_000,
        1_000_000, 1_100_000, 1_250_000, 1_400_000
        
    ]
}
df = pd.DataFrame(data)

# Column names
x_col = 'Date'
y_col = 'Revenue'

# Custom Y-axis formatter (M for thousands, MM for millions)
def custom_formatter(x, pos):
    if x >= 1_000_000:
        return f'{x/1_000_000:.1f}MM'
    elif x >= 1_000:
        return f'{x/1_000:.1f}M'
    else:
        return str(int(x))

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df[x_col], df[y_col], marker='o', linestyle='-', color='royalblue')

# Custom formatting
ax.yaxis.set_major_formatter(ticker.FuncFormatter(custom_formatter))
ax.set_title(f'{y_col} Over Time')
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
