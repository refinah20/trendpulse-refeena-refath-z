import os
import matplotlib.pyplot as plt
import pandas as pd


def generate_visualizations():
  input_file = "data/trends_analysed.csv"

  # Check if the analysed file exists from Task 3
  if not os.path.exists(input_file):
    print(f"Error: {input_file} not found! Please run Task 3 first.")
    return

  # --- Task 1: Setup ---
  print(f"Loading data from {input_file}...")
  df = pd.read_csv(input_file)

  # Create outputs/ folder if it doesn't exist
  os.makedirs("outputs", exist_ok=True)

  # --- Task 2: Chart 1 — Top 10 Stories by Score (Horizontal Bar Chart) ---
  print("Generating Chart 1: Top 10 Stories by Score...")
  top_10 = df.nlargest(10, "score").sort_values("score", ascending=True)

  # Shorten titles longer than 50 characters for better readability
  shortened_titles = [
      title[:47] + "..." if len(title) > 50 else title
      for title in top_10["title"]
  ]

  fig, ax = plt.subplots(figsize=(10, 6))
  ax.barh(shortened_titles, top_10["score"], color="skyblue", edgecolor="navy")
  ax.set_xlabel("Score (Upvotes)")
  ax.set_title("Top 10 Stories by Score")
  ax.grid(axis="x", linestyle="--", alpha=0.6)
  plt.tight_layout()

  chart1_path = "outputs/chart1_top_stories.png"
  plt.savefig(chart1_path)
  plt.close()  # Close figure to free up memory

  # --- Task 3: Chart 2 — Stories per Category (Bar Chart) ---
  print("Generating Chart 2: Stories per Category...")
  category_counts = df["category"].value_counts()

  fig, ax = plt.subplots(figsize=(8, 5))
  colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
  ax.bar(
      category_counts.index,
      category_counts.values,
      color=colors[: len(category_counts)],
      edgecolor="black",
  )
  ax.set_xlabel("Category")
  ax.set_ylabel("Number of Stories")
  ax.set_title("Stories per Category")
  plt.xticks(rotation=30)
  plt.tight_layout()

  chart2_path = "outputs/chart2_categories.png"
  plt.savefig(chart2_path)
  plt.close()

  # --- Task 4: Chart 3 — Score vs Comments (Scatter Plot) ---
  print("Generating Chart 3: Score vs Comments...")
  fig, ax = plt.subplots(figsize=(8, 5))

  # Split data into popular vs non-popular based on 'is_popular' column
  popular = df[df["is_popular"] == True]
  non_popular = df[df["is_popular"] == False]

  ax.scatter(
      non_popular["score"],
      non_popular["num_comments"],
      color="gray",
      alpha=0.7,
      label="Non-Popular",
      edgecolors="black",
  )
  ax.scatter(
      popular["score"],
      popular["num_comments"],
      color="orange",
      alpha=0.9,
      label="Popular (Above Average)",
      edgecolors="black",
  )

  ax.set_xlabel("Score (Upvotes)")
  ax.set_ylabel("Number of Comments")
  ax.set_title("Score vs Comments Scatter Plot")
  ax.legend()
  ax.grid(True, linestyle="--", alpha=0.5)
  plt.tight_layout()

  chart3_path = "outputs/chart3_scatter.png"
  plt.savefig(chart3_path)
  plt.close()

  # --- Bonus: Combined Dashboard Figure (+3 Marks) ---
  print("Generating Bonus Combined Dashboard...")
  fig = plt.figure(figsize=(18, 10))
  fig.suptitle("TrendPulse Dashboard", fontsize=20, fontweight="bold")

  # Subplot 1: Top Stories (Takes left side or top section)
  ax1 = fig.add_subplot(2, 2, 1)
  ax1.barh(
      shortened_titles, top_10["score"], color="skyblue", edgecolor="navy"
  )
  ax1.set_xlabel("Score")
  ax1.set_title("Top 10 Stories by Score")
  ax1.grid(axis="x", linestyle="--", alpha=0.5)

  # Subplot 2: Categories
  ax2 = fig.add_subplot(2, 2, 2)
  ax2.bar(
      category_counts.index,
      category_counts.values,
      color=colors[: len(category_counts)],
      edgecolor="black",
  )
  ax2.set_xlabel("Category")
  ax2.set_ylabel("Count")
  ax2.set_title("Stories per Category")
  ax2.tick_params(axis="x", rotation=30)

  # Subplot 3: Scatter Plot
  ax3 = fig.add_subplot(2, 2, (3, 4))  # Span across the bottom row
  ax3.scatter(
      non_popular["score"],
      non_popular["num_comments"],
      color="gray",
      alpha=0.7,
      label="Non-Popular",
  )
  ax3.scatter(
      popular["score"],
      popular["num_comments"],
      color="orange",
      alpha=0.9,
      label="Popular",
  )
  ax3.set_xlabel("Score")
  ax3.set_ylabel("Comments")
  ax3.set_title("Score vs Comments Analysis")
  ax3.legend()
  ax3.grid(True, linestyle="--", alpha=0.5)

  plt.tight_layout(rect=[0, 0.03, 1, 0.95])
  dashboard_path = "outputs/dashboard.png"
  plt.savefig(dashboard_path)
  plt.close()

  print(f"\nAll visualizations successfully generated and saved to outputs/")


if __name__ == "__main__":
  generate_visualizations()
