import sqlite3
# SQLLITE3 HANDLE ONLY 1 CONNECTION PER TIME .

class Soccer:
    
    def __init__(self):
        self.conn = sqlite3.connect('soccer.db')
        self.cur = self.conn.cursor()
        self.create_table()

    
    def create_table(self):

        # {"database" : "soccer", "tables" : ["match", "season", "venue", "hometeam", "awayteam"]}

        sql_query1 = """ CREATE TABLE IF NOT EXISTS match(matchid VARCHAR(50) PRIMARY KEY, 
                                                        feedMatchId INTEGER, skyId INTEGER,
                                                        competition VARCHAR(50), competitionId SMALLINT, 
                                                        Status VARCHAR(50), period VARCHAR(50), round VARCHAR(50),
                                                        type VARCHAR(30), minute SMALLINT, date TIMESTAMP, lastUpdate TIMESTAMP,
                                                        seasonid SMALLINT,   venueid SMALLINT,
                                                        hometeamid VARCHAR(20), homeskyid SMALLINT, homename VARCHAR(50), 
                                                        homeshortName VARCHAR(30), homeabbreviation CHAR(5),
                                                        homescore SMALLINT, homehalfTimeScore SMALLINT,
                                                        awayteamid VARCHAR(20), awayskyid SMALLINT, awayname VARCHAR(50), 
                                                        awayshortName VARCHAR(30), awayabbreviation CHAR(5),
                                                        awayscore SMALLINT, awayhalfTimeScore SMALLINT, 
                                                        FOREIGN KEY(seasonid) REFERENCES season(seasonid) ON DELETE CASCADE,
                                                        FOREIGN KEY(venueid) REFERENCES venue(id) ON DELETE CASCADE)
                                                        """
        sql_query2 = """CREATE TABLE IF NOT EXISTS season(seasonid SMALLINT PRIMARY KEY, season VARCHAR(30))"""

        sql_query3 = """CREATE TABLE IF NOT EXISTS venue(venueid SMALLINT PRIMARY KEY, name VARCHAR(30), location VARCHAR(30))"""
        
        queries  = [sql_query1, sql_query2, sql_query3]
        
        for query in queries:

            self.cur.execute(query)


    def insert_into_match(self, item):
        
        try:
            
            sql_query  = """INSERT OR IGNORE INTO match VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
            
            self.cur.executemany(sql_query, item)
            
            self.conn.commit()
        
        except Exception as err:
            
            print("\nFailed to insert row into the table match:\n" + str(sql_query))
            
            print(Exception, err)
        

# INSERTION INTO TABLE SEASON
    def insert_into_season(self, item):
        
        try:
            
            sql_query  = """INSERT OR IGNORE INTO season VALUES(?,?)"""
            
            self.cur.executemany(sql_query, item)
            
            self.conn.commit()
        
        except Exception as err:
            
            print("\nFailed to insert row into the table season:\n" + str(sql_query))
            
            print(Exception, err)
        

#INSERTION INTO TABLE VENUE

    def insert_into_venue(self, item):
        
        sql_query  = """INSERT OR IGNORE INTO venue VALUES(?,?,?)"""
        
        try:
            
            self.cur.executemany(sql_query, item)
            
            self.conn.commit()
        
        except Exception as err:
            
            print("\nFailed to insert row into the table season:\n" + str(sql_query))
            
            print(Exception, err)
        


# SELECT DATA FOR TEST

    def select_data(self):

        sql_query = """SELECT * FROM vanue"""

        self.cur.execute(sql_query)

        data = self.cur.fetchall()

        return data

