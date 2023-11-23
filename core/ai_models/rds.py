import matplotlib.pyplot as plt
import pandas as pd

def plot_engine_distribution(df):
    engine_counts = df['Engine'].value_counts()
    plt.bar(engine_counts.index, engine_counts.values)
    plt.xlabel('Engine')
    plt.ylabel('Count')
    plt.title('Engine Distribution')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/rds_vis/engine_distribution.png')  # Save figure
    plt.close()

def plot_status_distribution(df):
    status_counts = df['DBInstanceStatus'].value_counts()
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('DBInstanceStatus Distribution')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/rds_vis/status_distribution.png')  # Save figure
    plt.close()

def plot_storage_vs_engine(df):
    plt.scatter(df['AllocatedStorage'], df['Engine'])
    plt.xlabel('Allocated Storage')
    plt.ylabel('Engine')
    plt.title('Allocated Storage vs. Engine')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/rds_vis/storage_vs_engine.png')  # Save figure
    plt.close()

def plot_engine_distribution_with_status(df):
    engine_status_counts = df.groupby(['Engine', 'DBInstanceStatus']).size().unstack()
    engine_status_counts.plot(kind='bar', stacked=True)
    plt.xlabel('Engine')
    plt.ylabel('Count')
    plt.title('Engine Distribution with DBInstanceStatus')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/rds_vis/engine_distribution_with_status.png')  # Save figure
    plt.close()

def recommend_engine_instance_and_storage(df, storage_requirement):
    filtered_data = df[df['AllocatedStorage'] >= storage_requirement]

    if filtered_data.empty:
        closest_match = df.iloc[(df['AllocatedStorage'] - storage_requirement).abs().argsort()[:1]]
        recommended_engine = closest_match['Engine'].values[0]
        recommended_instance_type = closest_match['DBInstanceClass'].values[0]
        recommended_storage = closest_match['AllocatedStorage'].values[0]
        return recommended_engine, recommended_instance_type, recommended_storage

    recommended_engine = filtered_data['Engine'].values[0]
    recommended_instance_type = filtered_data['DBInstanceClass'].values[0]
    recommended_storage = filtered_data['AllocatedStorage'].values[0]
    return recommended_engine, recommended_instance_type, recommended_storage

# Assuming your data is in a DataFrame named df
# df = pd.read_csv('data/rds_databases_data.csv')

# # Plotting
# plot_engine_distribution(df)
# plot_status_distribution(df)
# plot_storage_vs_engine(df)
# plot_engine_distribution_with_status(df)

# # Recommendation
# user_storage_requirement = 50
# recommendation = recommend_engine_instance_and_storage(df, user_storage_requirement)
# print(f"Recommended Engine: {recommendation[0]}, Recommended Instance Type: {recommendation[1]}, Recommended Storage: {recommendation[2]} GB")
