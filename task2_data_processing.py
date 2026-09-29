from datetime import datetime
import glob
import os
import pandas as pd


def process_trending_data():
  # Find the latest JSON trends file inside the data/ folder automatically
  json_files = glob.glob("data/trends_*.json")

  if not json_files:
    print(
        "Error: No raw trends JSON file found in data/ folder! Please run Task"
        " 1 first."
    )
    return

  # Grab the most recent file if multiple exist
  input_file = max(json_files, key=os.path.getctime)

  # --- Task 1: Load the JSON File ---
  print(f"Loading data from {input_file}...")
  df = pd.read_json(input_file)
  print(f"Loaded {len(df)} stories from {input_file}")

  # --- Task 2: Clean the Data ---

  # 1. Remove duplicate stories based on post_id
  df = df.drop_duplicates(subset=["post_id"])
  print(f"After removing duplicates: {len(df)}")

  # 2. Drop rows where essential fields (post_id, title, score) are missing
  df = df.dropna(subset=["post_id", "title", "score"])
  print(f"After removing nulls: {len(df)}")

  # 3. Ensure score and num_comments are integers
  df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
  df["num_comments"] = (
      pd.to_numeric(df["num_comments"], errors="coerce").fillna(0).astype(int)
  )

  # 4. Remove stories where the score is less than 5 (low quality)
  df = df[df["score"] >= 5]
  print(f"After removing low scores: {len(df)}")

  # 5. Strip extra spaces from the title column
  df["title"] = df["title"].astype(str).str.strip()

  # --- Task 3: Save as CSV & Print Summary ---
  os.makedirs("data", exist_ok=True)
  output_csv = "data/trends_clean.csv"

  # Save the cleaned dataframe to CSV (without pandas index column)
  df.to_csv(output_csv, index=False)

  print(f"Saved {len(df)} rows to {output_csv}")

  # Print stories per category summary
  print("Stories per category:")
  category_counts = df["category"].value_counts()
  for cat, count in category_counts.items():
    print(f"  {cat:<15} {count}")


if __name__ == "__main__":
  process_trending_data()
