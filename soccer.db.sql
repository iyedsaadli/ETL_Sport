SELECT venue_name, sum(total_goal_scored) as goals_scored_invenue_season from total_goals_venue GROUP by venue_name ORDER by goals_scored_invenue_season DESC LIMIT 1