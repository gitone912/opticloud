import matplotlib.pyplot as plt
import pandas as pd

def plot_instance_type_distribution(df):
    instance_type_counts = df['InstanceType'].value_counts()
    plt.bar(instance_type_counts.index, instance_type_counts.values)
    plt.xlabel('Instance Type')
    plt.ylabel('Count')
    plt.title('Instance Type Distribution')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/ec2/instance_type_distribution.png')  # Save figure
    plt.close()

def plot_instance_state_distribution(df):
    state_counts = df['State'].value_counts()
    plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Instance State Distribution')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/ec2/instance_state_distribution.png')  # Save figure
    plt.close()

def plot_launch_time_vs_instance_type(df):
    df['LaunchTime'] = pd.to_datetime(df['LaunchTime'])
    plt.scatter(df['LaunchTime'], df['InstanceType'])
    plt.xlabel('Launch Time')
    plt.ylabel('Instance Type')
    plt.title('Launch Time vs. Instance Type')
    plt.xticks(rotation=45)
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/ec2/launch_time_vs_instance_type.png')  # Save figure
    plt.close()

def plot_instance_state_distribution_with_instance_type(df):
    state_instance_type_counts = df.groupby(['State', 'InstanceType']).size().unstack()
    state_instance_type_counts.plot(kind='bar', stacked=True)
    plt.xlabel('Instance Type')
    plt.ylabel('Count')
    plt.title('Instance State Distribution with Instance Type')
    plt.savefig('/Users/pranaymishra/Desktop/MAIT/opticloud/core/static/ec2/instance_state_distribution_with_instance_type.png')  # Save figure
    plt.close()

# Assuming your data is in a DataFrame named df
# df = pd.read_csv('data/ec2_instances_data.csv')

# Plotting
# plot_instance_type_distribution(df)
# plot_instance_state_distribution(df)
# plot_launch_time_vs_instance_type(df)
# plot_instance_state_distribution_with_instance_type(df)
