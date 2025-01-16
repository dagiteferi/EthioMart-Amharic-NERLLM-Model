import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import re 


# Caculate percentage of missing values in dataframe
def caculate_missing_percentage(dataframe):
    # Determine the total numer of element in dataframe
    total_elements = np.prod(dataframe.shape)
    
    # Calculate the total number of missing values in each column
    missing_values = dataframe.isna().sum()
    
    # Sum of the total numer of missing values 
    total_missing = missing_values.sum()

    # Compute the percentage of missing values 
    percentage_missing = (total_missing / total_elements) * 100 

    # Print the result, rounded to two decimal 
    print(f"The dataset has {round(percentage_missing, 2)}% missing values.")

# Check missing values
def check_missing_values(df):
    """check missing values in the dataset."""
    missing_values = df.isnull().sum()
    missing_percentage = 100 * df.isnull().sum() / len(df)
    column_data_types = df.dtypes
    missing_table = pd.concat([missing_values, missing_percentage, column_data_types], axis=1,
                              keys=['Missing Values', '% of Total Values', 'Data Types'])
    return missing_table.sort_values('% of Total Values', ascending=False).round(2)

def outlier_box_plots(df):
    for column in df:
        plt.figure(figsize=(10,6))
        sns.boxplot(x=df[column])
        plt.title(f"Box plot of {column}")
        plt.show()

# Define a function to remove emojis
def remove_emojis(text):
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251" 
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

# Define a function to remove English words
def remove_english_words(text):
    english_pattern = re.compile(r'\b[a-zA-Z]+\b')
    return english_pattern.sub('', text)