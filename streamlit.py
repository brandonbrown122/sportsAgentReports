import streamlit as st

def read_text_file(file_path):
    """Utility function to read a text file."""
    with open(file_path, 'r') as file:
        return file.read()

def main():
    st.title("AI Report")

    # Add options for navigation in the sidebar
    nav_options = ["Advanced Analytics","Analyst Picks","Bizzare Stats",
                   "Coaches","Head To Head","Historical Handicapping",
                   "Home/Away Advantage","Injuries","Large Wagers",
                   "Line Movement","Line/Odds","Local News","Motivation",
                   "Officials","Overall Report","Picks","Performance Patterns","Trending Players",
                   "Public Money","Rivalry","Schedule Conflicts",
                   "Social Media Sentiment","Special Night","Trends"
                   ,]
    choice = st.sidebar.radio("Select a Topic", nav_options)

    # Display content based on selected option
    if choice == "Overall Report":
        text_content = read_text_file("final_report.txt")
        st.subheader("Overall Report")
        st.write(text_content)

    elif choice == "Advanced Analytics":
        text_content = read_text_file("advanced_analytics.txt")
        st.subheader("Advanced Analytics")
        st.write(text_content)

    elif choice == "Analyst Picks":
        text_content = read_text_file("top_analysts.txt")
        st.subheader("Analyst Picks")
        st.write(text_content)

    elif choice == "Bizzare Stats":
        text_content = read_text_file("bizzare_stats.txt")
        st.subheader("Bizzare Stats")
        st.write(text_content)

    elif choice == "Coaches":
        text_content = read_text_file("coaching.txt")
        st.subheader("Bizzare Stats")
        st.write(text_content)

    elif choice == "Picks":
        text_content = read_text_file("consensus.txt")
        st.subheader("Picks")
        st.write(text_content)
    
    elif choice == "Head To Head":
        text_content = read_text_file("head_to_head.txt")
        st.subheader("Head To Head")
        st.write(text_content)

    elif choice == "Historical Handicapping":
        text_content = read_text_file("historical_handicapping.txt")
        st.subheader("Historical Handicapping")
        st.write(text_content)

    elif choice == "Home/Away Advantage":
        text_content = read_text_file("home_away_discrepency.txt")
        st.subheader("Home/Away Advantage")
        st.write(text_content)

    elif choice == "Injuries":
        text_content = read_text_file("key_injuries.txt")
        st.subheader("Injuries")
        st.write(text_content)

    elif choice == "Large Wagers":
        text_content = read_text_file("large_money.txt")
        st.subheader("Large Wagers")
        st.write(text_content)

    elif choice == "Line Movement":
        text_content = read_text_file("lines_movement.txt")
        st.subheader("Line Movement")
        st.write(text_content)

    elif choice == "Line/Odds":
        text_content = read_text_file("lines_odds.txt")
        st.subheader("Line/Odds")
        st.write(text_content)

    elif choice == "Local News":
        text_content = read_text_file("local_news.txt")
        st.subheader("Local News")
        st.write(text_content)

    elif choice == "Motivation":
        text_content = read_text_file("motivation.txt")
        st.subheader("Motivation")
        st.write(text_content)

    elif choice == "Officials":
        text_content = read_text_file("officials.txt")
        st.subheader("Officials")
        st.write(text_content)

    elif choice == "Performance Patterns":
        text_content = read_text_file("patterns_in_performance.txt")
        st.subheader("Performance Patterns")
        st.write(text_content)

    elif choice == "Trending Players":
        text_content = read_text_file("players_trending.txt")
        st.subheader("Trending Players")
        st.write(text_content)

    elif choice == "Public Money":
        text_content = read_text_file("public_money.txt")
        st.subheader("Public Money")
        st.write(text_content)

    elif choice == "Rivalry":
        text_content = read_text_file("rivalry.txt")
        st.subheader("Rivalry")
        st.write(text_content)

    elif choice == "Schedule Conflicts":
        text_content = read_text_file("schedule_conflict.txt")
        st.subheader("Schedule Conflicts")
        st.write(text_content)

    elif choice == "Social Media Sentiment":
        text_content = read_text_file("social_media_sentiment.txt")
        st.subheader("Social Media Sentiment")
        st.write(text_content)

    elif choice == "Special Night":
        text_content = read_text_file("special_night.txt")
        st.subheader("Special Night")
        st.write(text_content)

    elif choice == "Trends":
        text_content = read_text_file("trending.txt")
        st.subheader("Trends")
        st.write(text_content)

if __name__ == "__main__":
    main()
