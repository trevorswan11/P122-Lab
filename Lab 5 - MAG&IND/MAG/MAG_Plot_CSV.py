import pandas as pd
import matplotlib.pyplot as plt

def plot_cleaned_csv(csv_file):
    df = pd.read_csv(csv_file)
    
    if df.shape[1] < 2:
        print("CSV must have at least two columns.")
        return

    col1, col2 = df.iloc[:, 0], df.iloc[:, 1]
    
    col1 = pd.to_numeric(col1, errors='coerce')
    col2 = pd.to_numeric(col2, errors='coerce')
    
    mask = col1.notna() & col2.notna()
    col1_cleaned, col2_cleaned = col1[mask], col2[mask]
    
    plt.figure(figsize=(8, 6))
    plt.plot(col1_cleaned, col2_cleaned, 'bo-', label='Filtered Data')
    plt.xlabel('Column 1')
    plt.ylabel('Column 2')
    plt.title('Plot of Cleaned First Two Columns')
    plt.legend()
    plt.grid()
    plt.show()

plot_cleaned_csv('D5Dataset.csv')

