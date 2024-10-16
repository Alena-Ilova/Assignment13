import seaborn as sns
print(sns.get_dataset_names())
car_crashes = sns.load_dataset('car_crashes')
print(car_crashes)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap of Car Crashes Dataset')
plt.show()


avg_premium_by_alcohol = car_crashes.groupby('alcohol')['ins_premium'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(x='alcohol', y='ins_premium', data=avg_premium_by_alcohol, palette='viridis')
plt.title('Average Insurance Premiums Based on Alcohol Impairment')
plt.xlabel('Percentage of Alcohol-Impaired Drivers')
plt.ylabel('Average Insurance Premium')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='speeding', y='total', data=car_crashes, alpha=0.6)
plt.title('Scatter Plot of Speeding vs. Total Accidents')
plt.xlabel('Percentage of Speeding Drivers')
plt.ylabel('Total Fatal Collisions per Billion Miles')
plt.axhline(y=car_crashes['total'].mean(), color='r', linestyle='--')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x='no_previous', y='ins_losses', data=car_crashes, palette='Set2')
plt.title('Insurance Losses by Previous Accident History')
plt.xlabel('Percentage of Drivers with No Previous Accidents')
plt.ylabel('Insurance Losses per Insured Driver')
plt.xticks(rotation=45)
plt.show()


pair_plot_data = car_crashes[['total', 'speeding', 'alcohol', 'ins_premium', 'ins_losses']]
sns.pairplot(pair_plot_data)
plt.suptitle('Pair Plot of Key Variables in Car Crashes Dataset', y=1.02)
plt.show()