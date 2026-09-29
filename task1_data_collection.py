import json
import urllib.request

def fetch_trending_data():
    # We will fetch public data from a reliable test/public API endpoint
    # (Using a standard public API for demonstration)
    url = "https://jsonplaceholder.typicode.com/posts"
    
    print("Fetching live data from the internet...")
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
        # Let's take just the first 10 items to keep our mini-project simple
        trending_items = data[:10]
        
        # Save the raw data into a local file
        file_name = "raw_data.json"
        with open(file_name, "w") as f:
            json.dump(trending_items, f, indent=4)
            
        print(f"Success! Raw data saved to {file_name}")
        
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    fetch_trending_data()