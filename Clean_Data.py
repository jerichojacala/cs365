import pandas as pd

# Paths to the CSV files
file_paths = [
    '/path/to/game_stats_2010.csv',
    '/path/to/game_stats_2011.csv',
    '/path/to/game_stats_2012.csv',
    '/path/to/game_stats_2013.csv',
    '/path/to/game_stats_2014.csv',
    '/path/to/game_stats_2015.csv',
    '/path/to/game_stats_2016.csv',
]

# Load all datasets into a list of dataframes
dataframes = [pd.read_csv(file_path) for file_path in file_paths]

# Combine all DataFrames into one
combined_data = pd.concat(dataframes, ignore_index=True)

# Remove any duplicate rows, if they exist
combined_data.drop_duplicates(inplace=True)

# Assuming the initial inspection found no missing values or inconsistencies in team names and numerical data
# and that the dataset is already in a good shape for analysis. 
# However, you can add additional cleaning steps here if necessary.

# Save the cleaned dataset to a new CSV file
cleaned_data_path = '/path/to/cleaned_game_stats_2010_2016.csv'
combined_data.to_csv(cleaned_data_path, index=False)

print(f"Cleaned dataset saved to {cleaned_data_path}")
