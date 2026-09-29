import json
import os

def process_data():
    input_file = "raw_data.json"
    output_file = "clean_data.json"
    
    # Check if the raw data file exists first
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found! Please run Task 1 first.")
        return
    
    print("Reading and cleaning raw data...")
    with open(input_file, "r") as f:
        raw_data = json.load(f)
        
    cleaned_data = []
    
    for item in raw_data:
        # Simple cleaning steps:
        # 1. Ensure title is properly capitalized and stripped of extra spaces
        title = item.get("title", "").strip().capitalize()
        
        # 2. Ensure body/content is cleaned up
        body = item.get("body", "").strip().replace("\n", " ")
        
        # 3. Keep only items that actually have a title and body
        if title and body:
            cleaned_item = {
                "id": item.get("id"),
                "title": title,
                "summary": body
            }
            cleaned_data.append(cleaned_item)
            
    # Save the cleaned data to a new file
    with open(output_file, "w") as f:
        json.dump(cleaned_data, f, indent=4)
        
    print(f"Success! Cleaned data saved to {output_file}. Total items kept: {len(cleaned_data)}")

if __name__ == "__main__":
    process_data()