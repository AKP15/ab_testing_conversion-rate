# Project 8 — A/B Testing & Conversion Experiment Analysis

## 📌 Project Overview

This project analyzes an A/B test for an e-commerce website to determine whether a new website version (Version B) improves customer conversion compared with the existing version (Version A).

The main business question was:

> Does Version B significantly improve conversion compared with Version A?

The analysis includes data cleaning, conversion-rate comparison, statistical hypothesis testing, confidence intervals, device-level analysis, and business recommendations.

---

## 🎯 Business Objective

The company wants to decide whether to launch a new website design.

- **Version A:** Control / existing website
- **Version B:** Treatment / new website
- **Primary metric:** Conversion Rate
- **Significance level:** α = 0.05

The goal is to determine whether the difference in conversion rates is statistically significant and whether Version B should be launched.

---

## 📊 Dataset

The dataset contains **10,000 users** after cleaning.

### Main Columns

| Column | Description |
|---|---|
| User_ID | Unique user identifier |
| Group | A/B experiment group |
| Device | User device type |
| Country | User country |
| Age | User age |
| Visits | Number of visits |
| Pages_Viewed | Pages viewed during sessions |
| Session_Duration | Session duration |
| Converted | Whether the user converted |
| Revenue | Revenue generated |

---

## 🧹 Data Cleaning

The original dataset contained **10,008 rows**.

Data-quality issues included:

- 8 duplicate rows
- Missing Device values
- Missing Country values
- Missing Pages_Viewed values
- Missing Session_Duration values
- Invalid Age values

### Cleaning actions

- Removed duplicate rows
- Filled missing Country values with `Unknown`
- Filled missing categorical Device values using the mode
- Filled missing numerical values using the median
- Replaced invalid ages with the median
- Verified that no missing values remained
- Verified that no duplicate rows remained

### Final Dataset

- **Rows:** 10,000
- **Columns:** 10
- **Missing values:** 0
- **Duplicates:** 0

---

## 📈 Overall A/B Test Results

| Metric | Version A | Version B |
|---|---:|---:|
| Users | 5,013 | 4,987 |
| Conversions | 436 | 546 |
| Conversion Rate | 8.70% | 10.95% |

### Conversion Lift

**Absolute lift:**

> +2.25 percentage points

**Relative lift:**

> +22.22%

Version B achieved a higher conversion rate than Version A.

---

## 🧪 Hypothesis Testing

### Null Hypothesis (H₀)

There is no difference in conversion rates between Version A and Version B.

### Alternative Hypothesis (H₁)

There is a difference in conversion rates between Version A and Version B.

### Test

Two-proportion z-test

### Significance Level

α = 0.05

### Results

- **z-statistic:** -3.752
- **p-value:** 0.000176

Since:

> p-value < 0.05

I rejected the null hypothesis.

### Conclusion

There is statistically significant evidence that Version B has a different conversion rate from Version A.

Because Version B's conversion rate is higher, the experiment provides strong evidence that **Version B improves conversion**.

---

## 📏 95% Confidence Interval

The 95% confidence interval for the conversion-rate difference (B − A) was:

> **+1.09 to +3.42 percentage points**

The observed improvement was:

> **+2.25 percentage points**

Because the entire confidence interval is above zero, the estimated treatment effect is consistently positive.

---

## 📱 Device-Level Analysis

Conversion rates were also analyzed by device.

| Device | A Conversion | B Conversion | Difference |
|---|---:|---:|---:|
| Desktop | 9.14% | 10.88% | +1.74 pp |
| Mobile | 8.22% | 11.36% | +3.14 pp |
| Tablet | 9.20% | 8.78% | -0.42 pp |

### Mobile

- z-statistic: 3.711
- p-value: 0.000207
- Result: Statistically significant

Version B significantly improved conversion among mobile users.

### Desktop

- z-statistic: 1.889
- p-value: 0.058895
- Result: Not statistically significant

Desktop conversion was higher for Version B, but there was not enough evidence at the 5% significance level to confirm a real improvement.

### Tablet

- z-statistic: -0.211
- p-value: 0.832939
- Result: Not statistically significant

Although the conversion rate was slightly lower for Version B, there is no statistical evidence that Version B performs worse on tablets.

---

## 💡 Key Business Insights

### 1. Version B wins overall

Version B increased conversion from:

**8.70% → 10.95%**

This represents a **+2.25 percentage-point** improvement and a **+22.22% relative lift**.

### 2. Mobile is the strongest opportunity

Mobile users experienced the largest improvement:

**+3.14 percentage points**

The improvement was also statistically significant.

### 3. Desktop improvement needs more evidence

Desktop conversion increased by:

**+1.74 percentage points**

However, the p-value was 0.0589, slightly above the 0.05 threshold.

Therefore, I would not claim that Version B significantly improves desktop conversion.

### 4. Tablet is not a confirmed problem

Tablet conversion decreased slightly:

**-0.42 percentage points**

However, the p-value was 0.833.

Therefore, there is no statistical evidence that Version B performs worse for tablet users.

---

## 🎯 Business Recommendation

Based on the experiment results:

> **Launch Version B, with particular attention to the mobile experience, while continuing to monitor desktop and tablet performance.**

The overall experiment provides strong statistical evidence that Version B improves conversion.

Mobile users show the strongest statistically significant improvement.

Desktop performance should continue to be monitored because the observed improvement was positive but not statistically significant.

The tablet result should also be monitored, but the small negative difference should not be treated as a confirmed problem because it was not statistically significant.

---

## 📊 Dashboard

The final dashboard includes:

- Total Users
- Control Conversion Rate
- Treatment Conversion Rate
- Conversion Lift
- P-value
- A vs B Conversion Rate
- Conversion Rate by Device
- Statistical Significance Tests
- Key Business Insights
- Business Recommendation

### Dashboard Title

**A/B Testing & Conversion Experiment Analysis**

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Google Colab

---

## 🧠 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- KPI Development
- Conversion Rate Analysis
- A/B Testing
- Hypothesis Testing
- Two-Proportion Z-Test
- P-value Interpretation
- Confidence Intervals
- Statistical Significance
- Segment Analysis
- Business Recommendation
- Data Visualization
- Dashboard Development

---

## 📌 Key Takeaways

This project demonstrated how to move from a business question to a statistically supported decision.

The main lessons were:

1. A higher conversion rate does not automatically mean a statistically significant improvement.
2. Statistical significance should be evaluated using a hypothesis test.
3. Confidence intervals help communicate the uncertainty around an estimated effect.
4. Segment-level analysis can reveal where a treatment performs best.
5. Business recommendations should consider both statistical evidence and practical impact.

---

## 🎤 Interview Summary

> I worked on an A/B testing project for an e-commerce website to determine whether a new website version improved conversion. I cleaned the dataset, calculated conversion rates, and compared the control and treatment groups using a two-proportion z-test. Version A had an 8.70% conversion rate while Version B had 10.95%, giving a 2.25 percentage-point lift. The p-value was 0.000176, so I rejected the null hypothesis and concluded that the improvement was statistically significant. I then analyzed the results by device and found that mobile users had the strongest significant improvement, while desktop and tablet differences were not statistically significant. Based on the results, I recommended launching Version B while prioritizing the mobile experience and continuing to monitor desktop and tablet performance.
