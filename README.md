# Power BI Custom Python Scatter Plot Visual

This repository contains a Power BI-ready Python script that generates a customized scatter plot visualization using `matplotlib` and `seaborn`. The visual is designed to display system-wise revenue distribution across multiple organizations, with dynamic highlighting based on user selection from a slicer in Power BI.

---

## Key Features

### 🎯 Dynamic Highlighting
- Select an organization using a slicer in Power BI.
- Selected organization points appear in **blue**.
- All other organizations turn into smaller **grey** dots.

### 🏷️ Dynamic Data Labels
- Data labels (% revenue) are displayed only for the selected organization.
- Cleaner view without cluttering the chart.

### 📊 Visual Design
- X-Axis → Systems
- Y-Axis → % Revenue Contribution
- Legend → Organizations
- Point Size → Larger for selected org, smaller for others
- Clean axis formatting with Y-axis as percentage.
- Responsive layout to Power BI filters & slicers.

---

## Visual Example

![Scatter Plot Visual]

---

## Folder Structure

