import os
import numpy as np
import pandas as pd

def analyze_trending_data():
    input_file = "data/trends_clean.csv"
    
    # Check if the clean file exists from Task 2
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found! Please run Task 2 first.")
        return
    
    # --- Task 1: Load and Explore ---
    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    print(f"Loaded data: {df.shape}")
    print("First 5 rows:")
    print(df.head())
    
    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()
    print(f"\nAverage score   : {avg_score:.2f}")
    print(f"Average comments: {avg_comments:.2f}")
    
    # --- Task 2: Basic Analysis with NumPy ---
    # Convert score column to a NumPy array for mathematical operations
    scores_array = df["score"].to_numpy()
    
    mean_score = np.mean(scores_array)
    median_score = np.median(scores_array)
    std_score = np.std(scores_array)
    max_score = np.max(scores_array)
    min_score = np.min(scores_array)
    
    # Find category with the most stories
    category_counts = df["category"].value_counts()
    most_common_category = category_counts.idxmax()
    max_category_count = category_counts.max()
    
    # Find story with the most comments
    max_comment_idx = df["num_comments"].idxmax()
    top_commented_story = df.loc[max_comment_idx]
    
    print("\n--- NumPy Stats ---")
    print(f"Mean score   : {mean_score:.2f}")
    print(f"Median score : {median_score:.2f}")
    print(f"Std deviation: {std_score:.2f}")
    print(f"Max score    : {max_score}")
    print(f"Min score    : {min_score}")
    print(f"Most stories in: {most_common_category} ({max_category_count} stories)")
    print(f"Most commented story: \"{top_commented_story['title']}\"  — {top_commented_story['num_comments']} comments")
    
    # --- Task 3: Add New Columns ---
    # 1. engagement: num_comments / (score + 1)
    df["engagement"] = df["num_comments"] / (df["score"] + 1)
    
    # 2. is_popular: True if score > average score, else False
    df["is_popular"] = df["score"] > avg_score
    
    # --- Task 4: Save the Result ---
    os.makedirs("data", exist_ok=True)
    output_file = "data/trends_analysed.csv"
    
    df.to_csv(output_file, index=False)
    print(f"\nSaved to {output_file}")

if __name__ == "__main__":
    analyze_trending_data()
