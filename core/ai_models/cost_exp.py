import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast  # Import the ast module for literal_eval

def preprocess_cost_data(file_path):
    df = pd.read_csv(file_path)

    # Convert 'TimePeriod' column to datetime objects
    df['TimePeriod'] = df['TimePeriod'].apply(ast.literal_eval)  # Convert string to dictionary
    df['Start'] = pd.to_datetime(df['TimePeriod'].apply(lambda x: x['Start']))
    df['End'] = pd.to_datetime(df['TimePeriod'].apply(lambda x: x['End']))

    # Extract 'Amount' value from 'BlendedCost' dictionary
    df['BlendedCost'] = df['BlendedCost'].apply(lambda x: ast.literal_eval(x)['Amount'])

    return df

def plot_blended_cost_over_time(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Start', y='BlendedCost', data=df, label='BlendedCost')
    plt.title('BlendedCost Over Time')
    plt.xlabel('Time')
    plt.ylabel('BlendedCost (USD)')
    plt.legend()
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/cost_exp/blended_cost_over_time.png')  # Save figure
    plt.close()

def plot_service_counts(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Service', data=df, order=df['Service'].value_counts().index)
    plt.title('Service Counts')
    plt.xlabel('Service')
    plt.ylabel('Count')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/cost_exp/service_counts.png')  # Save figure
    plt.close()

def plot_scatter_resource_type_vs_blended_cost(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Service', y='BlendedCost', data=df, hue='Service')
    plt.title('Scatter Plot: Resource Type vs BlendedCost')
    plt.xlabel('Resource Type')
    plt.ylabel('BlendedCost (USD)')
    plt.legend()
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/cost_exp/scatter_resource_type_vs_blended_cost.png')  # Save figure
    plt.close()

def plot_box_plot_blended_cost_distribution_by_service(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Service', y='BlendedCost', data=df)
    plt.title('Box Plot: BlendedCost Distribution by Service')
    plt.xlabel('Service')
    plt.ylabel('BlendedCost (USD)')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/cost_exp/box_plot_blended_cost_distribution_by_service.png')  # Save figure
    plt.close()

def plot_heatmap_blended_cost_correlation(df):
    heatmap_data = df.pivot_table(index='Service', columns='Resource Type', values='BlendedCost', aggfunc='sum')
    numeric_cols = ['BlendedCost', 'Resource Type']
    correlation_matrix = df[numeric_cols].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".2f")
    plt.title('BlendedCost Heatmap')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/cost_exp/blended_cost_heatmap.png')  # Save figure
    plt.close()

# # Assuming your data is in a DataFrame named df
# df = preprocess_cost_data('data/cost_explorer_data.csv')

# # Plotting
# plot_blended_cost_over_time(df)
# plot_service_counts(df)
# plot_scatter_resource_type_vs_blended_cost(df)
# plot_box_plot_blended_cost_distribution_by_service(df)
# plot_heatmap_blended_cost_correlation(df)
