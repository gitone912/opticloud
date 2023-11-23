import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import ast

def preprocess_cost_data(file_path):
    df = pd.read_csv(file_path)

    # Convert 'TimePeriod' column to datetime objects
    df['TimePeriod'] = df['TimePeriod'].apply(ast.literal_eval)  
    df['Start'] = pd.to_datetime(df['TimePeriod'].apply(lambda x: x['Start']))
    df['End'] = pd.to_datetime(df['TimePeriod'].apply(lambda x: x['End']))

    # Extract 'Amount' value from 'BlendedCost' dictionary
    df['BlendedCost'] = df['BlendedCost'].apply(lambda x: ast.literal_eval(x)['Amount'])

    return df

def create_linear_regression_pipeline(features, target):
    numerical_features = ['Start', 'End']
    categorical_features = ['Service', 'Resource Type']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    return pipeline

def train_linear_regression_model(pipeline, X_train, y_train):
    pipeline.fit(X_train, y_train)
    return pipeline

def predict_blended_cost(pipeline, user_input_features):
    user_predictions = pipeline.predict(user_input_features)
    return user_predictions[0]

# Assuming your data is in a DataFrame named df
# df = preprocess_cost_data('data/cost_explorer_data.csv')

# # Define features and target variable
# features = ['Service', 'Resource Type', 'Start', 'End']
# target = 'BlendedCost'

# # Create pipeline and train the model
# pipeline = create_linear_regression_pipeline(features, target)
# X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
# trained_pipeline = train_linear_regression_model(pipeline, X_train, y_train)

# # Make predictions on user input
# user_input = {
#     'Service': 'EC2',
#     'Resource Type': 'EBS:VolumeUsage.gp2',
#     'Start': pd.to_datetime('2023-11-23T12:00:00'),  # Replace with user input
#     'End': pd.to_datetime('2023-12-23T13:00:00')  # Replace with user input
# }

# user_input_df = pd.DataFrame([user_input])
# user_input_features = user_input_df[features]

# user_predictions = predict_blended_cost(trained_pipeline, user_input_features)

# print(f'Predicted BlendedCost: {round(user_predictions/1000000000)} USD')
