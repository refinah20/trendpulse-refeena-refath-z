from datetime import datetime
import json
import os
import time
import requests

# Define categories and their matching keywords (case-insensitive)
CATEGORIES = {
    "technology": [
        "AI",
        "software",
        "tech",
        "code",
        "computer",
        "data",
        "cloud",
        "API",
        "GPU",
        "LLM",
    ],
    "worldnews": [
        "war",
        "government",
        "country",
        "president",
        "election",
        "climate",
        "attack",
        "global",
    ],
    "sports": [
        "NFL",
        "NBA",
        "FIFA",
        "sport",
        "game",
        "team",
        "player",
        "league",
        "championship",
    ],
    "science": [
        "research",
        "study",
        "space",
        "physics",
        "biology",
        "discovery",
        "NASA",
        "genome",
    ],
    "entertainment": [
        "movie",
        "film",
        "music",
        "Netflix",
        "game",
        "book",
        "show",
        "award",
        "streaming",
    ],
}


def collect_trending_data():
  # Required header for HackerNews API requests
  headers = {"User-Agent": "TrendPulse/1.0"}
  top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

  print("Fetching top story IDs from Hacker News...")
  try:
    response = requests.get(top_stories_url, headers=headers)
    response.raise_for_status()
    story_ids = response.json()[:500]  # Fetch the first 500 story IDs
  except Exception as e:
    print(f"Failed to fetch top stories: {e}")
    return

  collected_stories = []
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  date_str = datetime.now().strftime("%Y%m%d")

  # Loop through each category and scan stories for keywords
  for category, keywords in CATEGORIES.items():
    print(f"Searching stories for category: {category}...")
    category_count = 0

    for story_id in story_ids:
      # Collect up to 25 stories per category
      if category_count >= 25:
        break

      story_url = (
          f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
      )

      try:
        story_res = requests.get(story_url, headers=headers)
        if story_res.status_code != 200:
          continue
        story_data = story_res.json()

        # Skip if story data is invalid or doesn't have a title
        if not story_data or "title" not in story_data:
          continue

        title = story_data.get("title", "")
        title_lower = title.lower()

        # Check if title matches any keyword for this category
        matched = False
        for kw in keywords:
          if kw.lower() in title_lower:
            matched = True
            break

        if matched:
          # Extract the 7 required fields
          formatted_story = {
              "post_id": story_data.get("id"),
              "title": title,
              "category": category,
              "score": story_data.get("score", 0),
              "num_comments": story_data.get("descendants", 0),
              "author": story_data.get("by", "unknown"),
              "collected_at": current_time,
          }
          collected_stories.append(formatted_story)
          category_count += 1

      except Exception as e:
        # If a request fails, print a message and move on without crashing
        print(f"Error fetching story ID {story_id}: {e}")
        continue

    # Wait 2 seconds between each category loop (one sleep per category loop)
    time.sleep(2)

  # Create data/ folder if it doesn't exist
  os.makedirs("data", exist_ok=True)
  output_file = f"data/trends_{date_str}.json"

  # Save collected stories to the JSON file
  with open(output_file, "w", encoding="utf-8") as f:
    json.dump(collected_stories, f, indent=4)

  print(
      f"Collected {len(collected_stories)} stories. Saved to {output_file}"
  )


if __name__ == "__main__":
  collect_trending_data()
