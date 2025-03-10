
import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import PDFSearchTool, SerperDevTool
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Define event details
today_date = "03-10-2025"
teams = "Oakland vs Robert Morris"
sport = "Mens NCCAB"
event_date = "March 10th 2025"

# Create base folder for today's date
if not os.path.exists(today_date):
    os.makedirs(today_date)

# Create event-specific folder (without repeating the date)
event_folder_name = f"{teams} {sport}"
event_folder = os.path.join(today_date, event_folder_name)

if not os.path.exists(event_folder):
    os.makedirs(event_folder)

serper_api_key = os.getenv("SERPER_API_KEY")
os.environ["SERPER_API_KEY"] = serper_api_key

webSearch = SerperDevTool()
llm = LLM(model="gpt-4o")

researcher = Agent(
    role="Senior sports betting researcher",
    goal="""Uncover useful infromation that can be used to help predict 
    the outcome of a sporting event find any and all useful information.
    Return only detailed information and do not be vague in your responses.""",
    backstory="Driven by a passion for sports and betting, you do unmatched research on upcoming games.",
    tools=[webSearch],
    llm=llm
)

# Define tasks with correct file paths
lines_odds = Task(
    description = f"""
        Identify the current line and odds for the event.
        Is there a consensus line or do multiple books have different lines.
        Look for multiple different sportsbooks lines.
        No need to give your opinion or analysis of it but do give a consensus line.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="Bullet point analysis of line and odds for the event.",
    agent=researcher,
    output_file=os.path.join(event_folder, "lines_odds.txt")
)

lines_movement = Task(
    description =f"""
        Identify how the lines have moved since opening.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="Bullet point analysis of line and odds movement.",
    agent=researcher,
    output_file=os.path.join(event_folder, "lines_movement.txt")
)


large_money = Task(
    description = f"""
        Find if any large money has been placed on either team. If any books have took large wagers on either team. Be specific with the example you cite if there are any.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of any large money bets that have been placed on either team.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "large_money.txt")
)

public_money = Task(
    description = f"""
        Find if the public money is heavily favored for one side. Give percentages of what the breakdown is if possible.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of what percentage the public is favoring over the other team.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "public_money.txt")
)


social_media_sentiment = Task(
    description = f"""
        Check social media and see how the public is feeling the game will go. Any viral tweets or posts about the upcoming game. Share the trending tweets if you find any.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the publlic sentiment.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "social_media_sentiment.txt")
)

key_injuries = Task(
    description = f"""
        Is either team missing any key players. Find what players are injured. 
        Also if possible try and find if it is a new injury or one that they are just returning from or have been playing through the injury for awhile.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the health status for each team.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "key_injuries.txt")
)

head_to_head = Task(
    description = f"""
        Find in the past how have these teams matched up.
        Give the past score results also.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the past outcomes and analysis of those games between the teams.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "head_to_head.txt")
)

trending = Task(
    description = f"""
        Look and see how both teams are trending. Is either team on a winning or losing streak. Have they been doing anything exceptional or very poorly over that stretch.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of how the teams have been trending.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "trending.txt")
)


patterns_in_performance = Task(
    description = f"""
        Find any patterns in these teams performances. Are they scoring a certain amount of points. Do they win games at a certain percentage when they score a certain amount of points.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the key findings for patterns in the teams performances.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "patterns_in_performance.txt")
)

rivalry = Task(
    description = f"""
        Is this a fierce rivalry. Do the teams dislike each other. Any fights or ejections in the past.
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the rivalry if any between these two teams.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "rivalry.txt")
)

motivation = Task(
    description = f"""
        Find if there is any extra added motivation. Like a player or coach facing a former team. Or playing for a conference championship. 
        The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the list of any added motivations if any.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "motivation.txt")
)


special_night = Task(
    description = f"""
        Find if the game has anything special going on. Like is it a penn state whiteout game or dollar beer night. Is it senior night or a coaches last game or is college gameday there.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of if there is anything special in particular for the game.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "special_night.txt")
)


officials = Task(
    description = f"""
        Find who the officials are for the game and any statistics that can be found on them like how many fouls they call per game or how many points are scored in their games.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the referees officiating the game 
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "officials.txt")
)

advanced_analytics = Task(
    description = f"""
        Find if there is any advanced analytics that could make an impact in the game.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the advanced stats for the game.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "advanced_analytics.txt")
)


home_away_discrepency = Task(
    description = f"""
        Find if there are any big advantages or disadvantages for a team playing at home or on the road and what are those advantages or disadvantages.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the key things for home and away discrepency.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "home_away_discrepency.txt")
)

coaching = Task(
    description = f"""
        Find if one team has a big coaching advantage. Like a hall of fame coach vs a new coach. Or if the coaches have very different styles. What are the coaches styles.
        Has one coach historically had an advantage over the other.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis about the head coaches and their styles.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "coaching.txt")
)

players_trending = Task(
    description = f"""
        Find if there are any players playing really well or struggling going into the game. If possible give statistics.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of the trending players.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "players_trending.txt")
)

local_news = Task(
    description = f"""
        Find if there is any notable local news about the game. A player was arrested or in trouble for example.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis local news about the game.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "local_news.txt")
)

top_analysts = Task(
    description = f"""
        Find out what the top analysts are predicting for the output of the game. Find how the analstys are predicting the game. Give their predictions and who is predicting it.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of analysts predictions""",
    agent=researcher,
    output_file=os.path.join(event_folder, "top_analysts.txt")
)

bizzare_stats = Task(
    description = f"""
        Find if there are any mindblowing or bizzare stats for the game. Either just crazy normal game stats or sports betting stats. Any stats that woiudl
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of wild or bizzare stats for the game.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "bizzare_stats.txt")
)

historical_handicapping = Task(
    description = f"""
        Find if historically there are any trends in the odds. For example if it was an nfl game and the spread was 20. 
        You could look how often a 20 point favorite covers the spread.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis historical handicapping and trends.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "historical_handicapping.txt")
)


schedule_conflict = Task(
    description = f"""
        Find if there is any scheduling conflict. Like a team is playing back to back days and
          they are away games. Or if a team had to travel multiple time zones.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis any schedule conflicts.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "schedule_conflict.txt")
)

prop_bets = Task(
    description = f"""
        Find any prop bets that are being talked about or being bet on by the public.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of popular prop bets.
""",
    agent=researcher,
    output_file=os.path.join(event_folder, "prop_bets.txt")
)

startingLineup = Task(
    description = f"""
        Find who the likely starting lineups will be for both teams.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""List of who is starting for both teams.
""",
    agent=researcher,
    context=[key_injuries],
    output_file=os.path.join(event_folder, "startingLineup.txt")
)

picks = Task(
    description = f"""
        Find what bet you recommend someone should make for the event.
            The sporting event we need research for is {teams} + {sport} + {event_date}
    """,
    expected_output="""Bullet point analysis of popular prop bets.
""",
context=[
        lines_odds,lines_movement,large_money,
               public_money,social_media_sentiment,key_injuries,
               head_to_head,trending,patterns_in_performance,
               rivalry,motivation,special_night,officials,advanced_analytics,
               home_away_discrepency,coaching,players_trending,local_news,
               top_analysts,bizzare_stats,historical_handicapping,schedule_conflict,
               prop_bets,startingLineup
    ],
    agent=researcher,
    output_file=os.path.join(event_folder, "picks.txt")
)


compile_report = Task(
    description=f"""Compile all research findings into a comprehensive report. Be sure the end of the report includes at least one bet to make that you recommend based on the research. Include all of the data that 
    you gathered in other tasks. Use all context.""",
    expected_output="A complete report containing all research components formatted with clear section headers",
    agent=researcher,
    context=[
        lines_odds,lines_movement,large_money,
               public_money,social_media_sentiment,key_injuries,
               head_to_head,trending,patterns_in_performance,
               rivalry,motivation,special_night,officials,advanced_analytics,
               home_away_discrepency,coaching,players_trending,local_news,
               top_analysts,bizzare_stats,historical_handicapping,schedule_conflict,
               picks
    ],
    output_file=os.path.join(event_folder, "final_report.txt")
)








def main():
    crew = Crew(
        agents=[researcher],
        tasks=[lines_odds,lines_movement,large_money,
               public_money,social_media_sentiment,key_injuries,
               head_to_head,trending,patterns_in_performance,
               rivalry,motivation,special_night,officials,advanced_analytics,
               home_away_discrepency,coaching,players_trending,local_news,
               top_analysts,bizzare_stats,historical_handicapping,schedule_conflict,
               picks,compile_report],       
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={
        'teams': teams,
        'sport': sport,
        'date': event_date
    })

    print(result)

if __name__ == "__main__":
    main()
