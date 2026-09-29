import json
import os
import matplotlib.pyplot as plt

def visualize_data():
    input_file = "clean_data.json"
    output_image = "trend_chart.png"
    
    # Check if the clean data file exists first
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found! Please run Task 2 first.")
        return
        
    print("Generating chart from data...")
    with open(input_file, "r") as f:
        data = json.load(f)
        
    if not data:
        print("No data to visualize.")
        return
        
    # Extract labels (Item IDs) and values (word counts)
    item_labels = [f"Item {item['id']}" for item in data]
    word_counts = [len(item['summary'].split()) for item in data]
    
    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(item_labels, word_counts, color='skyblue', edgecolor='navy')
    
    # Add titles and labels
    plt.xlabel('Trending Items')
    plt.ylabel('Summary Word Count')
    plt.title('TrendPulse: Word Count Distribution per Trending Item')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the chart as an image file
    plt.savefig(output_image)
    print(f"Success! Chart saved as {output_image}.")
    
    # Optional: Show the chart on your screen
    # plt.show()

if __name__ == "__main__":
    visualize_data()