
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


Environments
PyCharm Python IDE and postgreSQL analytics databases.



API Documentation
Endpoints
