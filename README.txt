InCrowd Sports - Data Engineer Task

This task is based on a common business task within the Data and Insights Team. 

We have a collection of ETL scripts that pull data from third party APIs, clean/re-structure that data, and use it to feed analytics.

Project Spec
We have created an API wrapper for a data source containing stats for major and minor football leagues (docs below)
Using this API, get all matches (excluding the Promotion Play-offs - Semi-finals & Promotion Play-offs - Final rounds) for the Sky Bet Championship in season 2020/2021, using Python
Create a table in a SQL database to hold the match information (including scores)
Write SQL queries to determine 
1) the team with the highest average number of goals per match
2) the most common match score result
3) the venue with the highest number of goals across the season
Produce the end-of-season league table and output it to a CSV file. The CSV file should have the following headings and should be ordered first by Total Number of Points and then by the Total Number of Goals Scored:
Team Name
Total Games Played
Total Number of Points (Win = 3 points, Draw = 1 point, Loss = 0 points)
Total Number of Goals Scored

In a zip file, please send to jobs@incrowdsports.com using https://wetransfer.com/ 
The final league table and stats, as above
Any interim tables 
Your Python code and its output
Your SQL statements

Environments
We use PyCharm as our Python IDE and postgreSQL analytics databases, but please use the environments in which you are most comfortable working. 

Please get in touch if you have any questions or need clarification. Asking for help is an important part of how we work together so don’t be afraid to ask if you need to.

Please do not spend more than 4 hours on this task.




API Documentation
Endpoints
All fixture information for League ID 1: https://feeds.incrowdsports.com/provider/opta/football/v1/matches?compId=8&season=2020
All fixture information for League ID 2: https://feeds.incrowdsports.com/provider/opta/football/v1/matches?compId=9&season=2020
All fixture information for League ID 3: https://feeds.incrowdsports.com/provider/opta/football/v1/matches?compId=10&season=2020
All fixture information for League ID 4: https://feeds.incrowdsports.com/provider/opta/football/v1/matches?compId=11&season=2020
