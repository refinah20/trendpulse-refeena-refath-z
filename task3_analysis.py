import json
import os

def analyze_data():
    input_file = "clean_data.json"
    output_file = "analysis_report.json"
    
    # Check if the clean data file exists first
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found! Please run Task 2 first.")
        return
    
    print("Analyzing clean data...")
    with open(input_file, "r") as f:
        data = json.load(f)
        
    total_items = len(data)
    if total_items == 0:
        print("No data to analyze.")
        return
        
    # Perform some basic analysis
    title_lengths = [len(item["title"]) for item in data]
    avg_title_length = sum(title_lengths) / total_items
    
    summary_lengths = [len(item["summary"].split()) for item in data]
    avg_word_count = sum(summary_lengths) / total_items
    
    # Create an analysis report dictionary
    report = {
        "total_items_analyzed": total_items,
        "average_title_length_chars": round(avg_title_length, 2),
        "average_summary_word_count": round(avg_word_count, 2)
    }
    
    # Save the report to a file
    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)
        
    print(f"Success! Analysis report saved to {output_file}.")
    print("Report Summary:")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    analyze_data()