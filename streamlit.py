import streamlit as st
import os

def read_text_file(file_path):
    """Utility function to read a text file."""
    with open(file_path, 'r') as file:
        return file.read()

def main():
    st.title("AI Report")

    # 1. Specify or discover your "date folder"
    #    If you only have one date folder (e.g., '03-09-2025'), you can hardcode it:
    date_folder = "03-10-2025"

    # 2. List all subdirectories in your date folder.
    #    Each subdirectory is a "game" (e.g., "Troy vs James Madison Mens NCCAB")
    games = [
        d for d in os.listdir(date_folder) 
        if os.path.isdir(os.path.join(date_folder, d))
    ]
    games.sort()  # Optional: sort them alphabetically

    if not games:
        st.error(f"No game folders found in {date_folder}!")
        return

    # 3. Let the user pick which game folder to view
    selected_game = st.selectbox("Select a Game", games)

    # 4. Define your sidebar navigation options
    nav_options = [
        "Overall Report", "Advanced Analytics", "Analyst Picks", "Bizzare Stats",
        "Coaches", "Head To Head", "Historical Handicapping", "Home/Away Advantage",
        "Injuries", "Large Wagers", "Line Movement", "Line/Odds", "Local News",
        "Motivation", "Officials", "Performance Patterns", "Trending Players",
        "Public Money", "Rivalry", "Schedule Conflicts", "Social Media Sentiment",
        "Special Night", "Trends"
    ]
    choice = st.sidebar.radio("Select a Topic", nav_options)

    # 5. Map each choice to its corresponding filename
    #    Make sure the filenames here match the actual .txt filenames in each game folder
    choice_to_filename = {
        "Overall Report": "final_report.txt",
        "Advanced Analytics": "advanced_analytics.txt",
        "Analyst Picks": "top_analysts.txt",             # ensure "top_analysts.txt" exists
        "Bizzare Stats": "bizzare_stats.txt",
        "Coaches": "coaching.txt",
        "Head To Head": "head_to_head.txt",
        "Historical Handicapping": "historical_handicapping.txt",
        "Home/Away Advantage": "home_away_discrepency.txt",
        "Injuries": "key_injuries.txt",
        "Large Wagers": "large_money.txt",
        "Line Movement": "lines_movement.txt",
        "Line/Odds": "lines_odds.txt",
        "Local News": "local_news.txt",
        "Motivation": "motivation.txt",
        "Officials": "officials.txt",
        "Performance Patterns": "patterns_in_performance.txt",
        "Trending Players": "players_trending.txt",
        "Public Money": "public_money.txt",
        "Rivalry": "rivalry.txt",
        "Schedule Conflicts": "schedule_conflict.txt",
        "Social Media Sentiment": "social_media_sentiment.txt",
        "Special Night": "special_night.txt",
        "Trends": "trending.txt",
        "Picks": "picks.txt",  # If you ever need the "Picks" option
    }

    # 6. Read the file from the selected game's folder
    selected_filename = choice_to_filename.get(choice)
    if not selected_filename:
        st.error(f"No filename mapped for '{choice}'!")
        return

    file_path = os.path.join(date_folder, selected_game, selected_filename)

    # 7. Check if the file exists
    if os.path.exists(file_path):
        text_content = read_text_file(file_path)
        st.subheader(choice)
        st.write(text_content)
    else:
        st.warning(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
