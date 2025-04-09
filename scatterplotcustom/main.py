import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

# Rename columns explicitly (helps if same name from diff tables)
dataset.rename(columns={
    'Organization_x': 'Organization', 
    'Revenue_x': 'Revenue_Calc', 
    'System_x': 'System',
    'Org_filter_x': 'Org_filter'  # from slicer input
}, inplace=True)

full_data = dataset

# Detect selected Org from slicer
selected_orgs = full_data['Org_filter'].unique()
selected_org = selected_orgs[0] if len(selected_orgs) == 1 else None

# Apply color mapping
full_data['Color'] = full_data['Organization'].apply(lambda x: 'red' if x == selected_org else 'black')
full_data['Size'] = full_data['Organization'].apply(lambda x: 150 if x == selected_org else 50)

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=full_data,
    x='System',
    y='Revenue_Calc',
    hue='Color',
    size='Size',
    sizes=(50, 200),
    palette={'red':'red', 'black':'black'},
    legend=False
)

# Show label only for selected Org rows
if selected_org:
    selected_data = full_data[full_data['Organization'] == selected_org]
    for i in range(selected_data.shape[0]):
        plt.text(
            selected_data['System'].iloc[i],
            selected_data['Revenue_Calc'].iloc[i] + 0.01,
            f"{int(selected_data['Revenue_Calc'].iloc[i] * 100)}%",
            ha='center',
            size=8,
            color='black',
            rotation=0
        )

plt.title(f'Revenue Contribution by System\nHighlighting: {selected_org}', fontsize=14, fontweight='bold')
plt.xlabel('System')
plt.ylabel('% Revenue')
plt.ylim(0, 0.4)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
