import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
df=pd.read_csv('data/ab_cleaned.csv')
df.columns=df.columns.str.strip().str.title ()
print(df.columns.tolist())
c=['User', 'Group', 'Device', 'Country', 'Age', 'Visits', 'Pages_Viewed', 'Session_Duration', 'Converted', 'Revenue']

###Caculate Conversion Rate = Converted Users ÷ Total Users × 100
Adf=df[df['Group']=='A']
Bdf=df[df['Group']=='B']
print(df['User'].count())
#print(type(df['Converted'].sum()))
#print(type(df['User'].count()))
Conversion_Rate=(df['Converted'].sum() / df['User'].count() * 100).round()
Conversion_RateA=(Adf['Converted'].sum() / Adf['User'].count() * 100).round()
Conversion_RateB=(Bdf['Converted'].sum() / Bdf['User'].count() * 100).round()
ab_group=df.groupby('Group').agg(
        Users=('User','count'),
        Conversions=('Converted','sum'),        
            )
ab_group['Conversion_Rate']=[Conversion_RateA,Conversion_RateB]
print(ab_group)

###Conversion Lift = (B Conversion Rate − A Conversion Rate) / A Conversion Rate × 100
Conversion_Lift = ((Conversion_RateB - Conversion_RateA) / Conversion_RateA * 100).round(2)
print(f"CL:{Conversion_Lift}")

###Two-Proportion Z-Test
ab_group['P_Value'] = ab_group['Conversions'] / ab_group['Users']
p_pool=(ab_group['Conversions'].sum() / ab_group['Users'].sum()).round(2)
se=np.sqrt(p_pool*(1-p_pool)*(1/ab_group.loc['A','Users'] + 1/ab_group.loc['B','Users']))
z_score=(ab_group.loc['B','P_Value'] - ab_group.loc['A','P_Value']) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

###CI 
pA = ab_group.loc['A','P_Value']
pB = ab_group.loc['B','P_Value']
NA = ab_group.loc['A','Users']
NB = ab_group.loc['B','Users']
diff = pB - pA
se_unpooled = np.sqrt(pA*(1-pA)/NA + pB*(1-pB)/NB)
lower = diff - 1.96 * se_unpooled
upper = diff + 1.96 * se_unpooled
#print([lower,upper])
#print(p_pool)print(se)print(z_score)print(p_value)print(ab_group)

segment = df.groupby(['Device','Group']).agg(
        Users=('User','count'),
        Conversion=('Converted','sum')
        ).reset_index()
#print(segment)
segment_summary=segment.pivot(index='Device',columns='Group',values=['Users','Conversion'])
segment_summary.columns=['A_User','B_User','A_Conversion','B_Conversion']
segment_summary['A_Rate']=segment_summary['A_Conversion'] / segment_summary['A_User'] * 100
segment_summary['B_Rate']=segment_summary['B_Conversion'] / segment_summary['B_User'] * 100
segment_summary['Diff']=segment_summary['B_Rate'] - segment_summary['A_Rate']
#print(segment_summary[['A_User','B_User','A_Conversion','B_Conversion']])
print(segment_summary[['A_Rate','B_Rate','Diff']])

###For Desktop 
segment_summary['PA_Value'] = segment_summary['A_Conversion'] / segment_summary['A_User']
segment_summary['PB_Value'] = segment_summary['B_Conversion'] / segment_summary['B_User']
#print(segment_summary[['PA_Value','PB_Value']])
xA_desk=segment_summary.loc['Desktop','A_Conversion']
xB_desk=segment_summary.loc['Desktop','B_Conversion']
pA_desk=segment_summary.loc['Desktop','PA_Value']
pB_desk=segment_summary.loc['Desktop','PB_Value']
NA_desk=segment_summary.loc['Desktop','A_User']
NB_desk=segment_summary.loc['Desktop','B_User']
p_pool_desk= (xA_desk + xB_desk) / (NA_desk + NB_desk)
se_desk = np.sqrt([p_pool_desk*(1- p_pool_desk)*(1/NA_desk + 1/NB_desk)])                                         
z_score_desk = (pB_desk - pA_desk) / se_desk
p_desk = 2 * (1 - stats.norm.cdf(abs(z_score_desk)))
#print(f"z-statics : {z_score_desk}")
#print(f"p-value : {p_desk}")
###For Mobile
xA_mob=segment_summary.loc['Mobile','A_Conversion']
xB_mob=segment_summary.loc['Mobile','B_Conversion']
pA_mob=segment_summary.loc['Mobile','PA_Value']
pB_mob=segment_summary.loc['Mobile','PB_Value']
NA_mob=segment_summary.loc['Mobile','A_User']
NB_mob=segment_summary.loc['Mobile','B_User']
p_pool_mob= (xA_mob + xB_mob) / (NA_mob + NB_mob)
se_mob = np.sqrt([p_pool_mob*(1- p_pool_mob)*(1/NA_mob + 1/NB_mob)])
z_score_mob = (pB_mob - pA_mob) / se_mob
p_mob = 2 * (1 - stats.norm.cdf(abs(z_score_mob)))
print(f"z-statics : {z_score_mob}")
print(f"p-value : {p_mob}")
###For Tabletpp                                           
xA_tab=segment_summary.loc['Tablet','A_Conversion']     
xB_tab=segment_summary.loc['Tablet','B_Conversion']     
pA_tab=segment_summary.loc['Tablet','PA_Value']         
pB_tab=segment_summary.loc['Tablet','PB_Value']         
NA_tab=segment_summary.loc['Tablet','A_User']           
NB_tab=segment_summary.loc['Tablet','B_User']
p_pool_tab= (xA_tab + xB_tab) / (NA_tab + NB_tab)
se_tab = np.sqrt([p_pool_tab*(1- p_pool_tab)*(1/NA_tab + 1/NB_tab)])
z_score_tab = (pB_tab - pA_tab) / se_tab
p_tab = 2 * (1 - stats.norm.cdf(abs(z_score_tab)))
print(f"z-statics : {z_score_tab}")                     
print(f"p-value : {p_tab}")

total_users=df['User'].count()

fig, axes = plt.subplots(2, 2, figsize=(28, 16))
fig.suptitle("A/B Testing & Conversion Experiment Analysis",
                          fontsize=20,
                          fontweight="bold")
card_w, card_h = 0.17, 0.08
kpi_x = [0.10, 0.30, 0.50, 0.70, 0.90]
kpi_y = 0.90
accents = ["#6366f1", "#0ea5e9", "#10b981", "#f59e0b", "#ef4444"]
for cx, accent in zip(kpi_x, accents):
    x0, y0 = cx - card_w / 2, kpi_y - card_h / 2
    fig.patches.append(FancyBboxPatch(
        (x0 + 0.002, y0 - 0.004), card_w, card_h,
        boxstyle="round,pad=0.01,rounding_size=0.02",
        edgecolor="none", facecolor="#e5e7eb",
        transform=fig.transFigure, zorder=1))

def add_kpi_text(fig, x,label, value, delta=None, y=kpi_y, fontsize=30):
    left = x - card_w / 2 + 0.022
    fig.text(left, y + 0.022, label.upper(),
             ha="left", va="center",
             color="#6b7280", fontweight="bold",
             fontsize=13, zorder=4)
    fig.text(left, y - 0.006, f"{value}",
             ha="left", va="center",
             color="#111827", fontweight="bold",
             fontsize=fontsize, zorder=4)
    if delta is not None:
        up = delta >= 0
        fig.text(left, y - 0.032, f"{'▲' if up else '▼'} {abs(delta)}%",
        ha="left", va="center",
        color="#10b981" if up else "#ef4444",
        fontweight="bold", fontsize=13, zorder=4)
add_kpi_text(fig, 0.10, "Total Users", f"{total_users}")
add_kpi_text(fig, 0.30, "Control Conversion (A) ", f"{Conversion_RateA}")
add_kpi_text(fig, 0.50, "Treatment Conversion (B) ", f"{Conversion_RateB}", delta=21.4)
add_kpi_text(fig, 0.70, "Conversion Lift ", f"{Conversion_Lift}")
add_kpi_text(fig, 0.90, "P Value", f"{p_value}")

axes[0, 0].bar(
        ab_group.index,
        ab_group['Conversion_Rate']
            )
axes[0, 0].set_title("PCA Explained Variancea")
axes[0, 0].set_xlabel("PCA")
axes[0, 0].set_ylabel("Explained Variance (%)")
for i, value in enumerate(ab_group['Conversion_Rate']):
    axes[0, 0].text(i, value + 0.1, f"{value:.1f}%", ha="center")


x = np.arange(len(segment_summary.index))
width = 0.35

bars_a = axes[0, 1].bar(x - width/2, segment_summary['A_Rate'], width, label='Group A')
bars_b = axes[0, 1].bar(x + width/2, segment_summary['B_Rate'], width, label='Group B')

axes[0, 1].set_title("Conversion Rate by Device")
axes[0, 1].set_xlabel("Device")
axes[0, 1].set_ylabel("Conversion Rate (%)")
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(segment_summary.index)
axes[0, 1].legend()
results = pd.DataFrame({
        "Test": ["Overall", "Mobile", "Desktop", "Tablet"],
            "p-value": [0.000176, 0.000207, 0.058895, 0.832939],
            })
results["Significant?"] = results["p-value"].apply(lambda p: "Yes" if p < 0.05 else "No")


ax = axes[1, 0]
ax.axis("off")
table = ax.table(
        cellText=[[t, f"{p:.6f}", s] for t, p, s in results.itertuples(index=False)],
        colLabels=["Test", "p-value", "Significant?"],
        cellLoc="center",
        bbox=[0, 0.05, 1, 0.85],   # [left, bottom, width, height] in axes coords
                        )
table.auto_set_font_size(False)
table.set_fontsize(13)
for row, p in enumerate(results["p-value"], start=1):
        table[row, 2].set_facecolor("#d4edda" if p < 0.05 else "#f8d7da")

for col in range(3):
    cell = table[0, col]
    cell.set_facecolor("#40466e")
    cell.set_text_props(color="white", weight="bold")
    ax.set_title("Significance Tests (α = 0.05)")
ax.set_title("Significance Tests (α = 0.05)")

import textwrap
ax = axes[1, 1]
ax.axis("off")
ax.set_title("Key Insights", fontweight="bold")

insights = [
    ("1. Version B wins overall",
     "B increased conversion from 8.70% to 10.95%."),
    ("2. Mobile is the strongest opportunity",
     "Mobile conversion improved by 3.14 percentage points and the difference is statistically significant."),
    ("3. Desktop needs more evidence",
     "Desktop performed better numerically, but the difference was not statistically significant."),
    ("4. Tablet is not a confirmed problem",
     "Tablet conversion was slightly lower under B, but the difference was not statistically significant."),
]

y = 0.95
for title, body in insights:
    ax.text(0.02, y, title, fontsize=12, fontweight="bold",
            va="top", transform=ax.transAxes)
    ax.text(0.02, y - 0.07, textwrap.fill(body, width=55), fontsize=10.5,
            va="top", color="#333333", transform=ax.transAxes)
    y -= 0.25

plt.tight_layout(rect=[0, 0, 1, 0.84])
plt.show()
