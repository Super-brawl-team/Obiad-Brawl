import sqlite3
import json
import time
import random
from Files.CsvLogic.Locations import Locations
import datetime 
from datetime import datetime, timedelta
class DataBase:

    def __init__(self, player):
        self.player = player
        self.connection = sqlite3.connect('Database/database.db')
        self.cursor = self.connection.cursor()
        self._initialize_tables()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Players (
                token TEXT PRIMARY KEY,
                data TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Gamerooms (
                room_id INTEGER PRIMARY KEY,
                data TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clubs (
                club_id INTEGER PRIMARY KEY,
                data TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ClubChats (
                club_id INTEGER PRIMARY KEY,
                data TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS GameroomChats (
                room_id INTEGER PRIMARY KEY,
                data TEXT
            )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Events (
            state INTEGER PRIMARY KEY,
            data TEXT
        )
        ''')
        self.connection.commit()
    def is_token_in_table(self, token):
        self.cursor.execute("SELECT 1 FROM Players WHERE token = ?", (token,))
        result = self.cursor.fetchone()
        return result is not None
    def loadAccount(self):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (self.player.token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            for key, value in playerData.items():
                setattr(self.player, key, value)
    

 
    def getPlayerId(self):
        self.cursor.execute("SELECT COUNT(*) FROM Players")
        self.player.low_id = self.cursor.fetchone()[0] + 1

    def createAccount(self):
        self.cursor.execute("SELECT COUNT(*) FROM Players WHERE token = ?", (self.player.token,))
        count = self.cursor.fetchone()[0]
        if count > 0:
            raise ValueError(f"Account with token {self.player.token} already exists.")
        data = {
            "name": self.player.name,
            "low_id": self.player.low_id,
            "club_id": 0,
            "club_role": 0,
            "player_experience": self.player.player_experience,
            "solo_wins": self.player.solo_wins,
            "duo_wins": self.player.duo_wins,
            "three_vs_three_wins": self.player.ThreeVSThree_wins,
            "gems": self.player.gems,
            "gold": self.player.gold,
            "elexir": self.player.elexir,
            "chips": self.player.chips,
            "coins_reward": 0,
            "coins_doubler": self.player.tokensdoubler,
            "coins_booster": self.player.coinsbooster,
            "trophies": self.player.trophies,
            "highest_trophies": self.player.trophies,
            "profile_icon": 0,
            "big_boxes": self.player.big_boxes,
            "room_id": 0,
            "unlocked_brawlers": self.player.unlocked_brawlers,
            "friends": {},
            "last_connection_time": 0,
            "player_status": 0,
            "tutorialState": 0,
            "region": self.player.region
        }

        self.cursor.execute("INSERT INTO Players (token, data) VALUES (?, ?)", (self.player.token, json.dumps(data)))
        #self.createOffer(self.player.token)
        self.connection.commit()

    def getAllPlayers(self):
        self.cursor.execute("SELECT data FROM Players")
        results = self.cursor.fetchall()
        return [json.loads(row[0]) for row in results]
    
    def getSpecifiedPlayers(self, tokens):
     players = ",".join(["?"] * len(tokens))
     query = f"SELECT data FROM Players WHERE token IN ({players})"
     self.cursor.execute(query, tokens)
     results = self.cursor.fetchall()
     return [json.loads(row[0]) for row in results]

    def getTokenByLowId(self, low_id):
     self.cursor.execute("SELECT token, data FROM Players")
     results = self.cursor.fetchall()
     for token, data in results:
        player_data = json.loads(data)
        if player_data.get('low_id') == low_id:
            return token 
     return None 
    def getSpecifiedValue(self, value_name):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (self.player.token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            return playerData.get(value_name)

    def replaceValue(self, value_name, new_value):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (self.player.token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            playerData[value_name] = new_value
            self.cursor.execute("UPDATE Players SET data = ? WHERE token = ?", (json.dumps(playerData), self.player.token))
            self.connection.commit()
    def replaceOtherValue(self, value_name, new_value, token):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            playerData[value_name] = new_value
            self.cursor.execute("UPDATE Players SET data = ? WHERE token = ?", (json.dumps(playerData), token))
            self.connection.commit()

    def appendElementToArray(self, value_name, element):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (self.player.token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            if value_name in playerData and isinstance(playerData[value_name], list):
                playerData[value_name].append(element)
            else:
                playerData[value_name] = [element]
            self.cursor.execute("UPDATE Players SET data = ? WHERE token = ?", (json.dumps(playerData), self.player.token))
            self.connection.commit()
            
    def getRoomId(self):
        self.cursor.execute("SELECT COUNT(*) FROM Gamerooms")
        self.player.room_id = self.cursor.fetchone()[0] + 1

    def createGameroom(self, roomType, chatData):
        
        data = {
            "room_id": self.player.room_id,
            "info": {
                "room_type": roomType,
                "map_id": self.player.map_id,
                "player_count": 1,
                "advertiseToBand": False,
                "alreadyAdvertisedToBand": False,
                "players": {
                 self.player.low_id: {
                    "host": True,
                    "low_id": self.player.low_id,
                    "name": self.player.name,
                    "team": self.player.team,
                    "ready": self.player.isReady,
                    "status": 3,
                    "brawler_id": self.player.brawler_id,
                    "skin_id": self.player.skin_id
                 }
                }
            }
        }

        self.cursor.execute("INSERT INTO Gamerooms (room_id, data) VALUES (?, ?)", (self.player.room_id, json.dumps(data)))
        
        chatQuery = "INSERT INTO GameroomChats (room_id, data) VALUES (?, ?)"
        self.executeQuery(chatQuery, [self.player.room_id, json.dumps(chatData)])
        self.connection.commit()
    
    def joinGameroom(self, room_id):
     self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (room_id,))
     result = self.cursor.fetchone()
     if not result:
        return False

     data = json.loads(result[0])

     data["info"]["player_count"] += 1
     data["info"]["players"][self.player.low_id] = { 
        "host": False,
        "low_id": self.player.low_id,
        "name": self.player.name,
        "team": self.player.team,
        "ready": self.player.isReady,
        "status": self.player.player_status,
        "brawler_id": self.player.brawler_id,
        "skin_id": self.player.skin_id
    }

     self.cursor.execute("UPDATE Gamerooms SET data = ? WHERE room_id = ?", (json.dumps(data), room_id))
     self.connection.commit()
     return True

    def loadGameroom(self):
     self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (self.player.room_id,))
     result = self.cursor.fetchone()
     if result:
        gameroomData = json.loads(result[0])
        return gameroomData.get("info", {})
     else:
        self.replaceValue('room_id', 0)
        return {} 

    def executeQuery(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchOne(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchAll(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def getPlayerInfo(self, lowId):
     self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (self.player.room_id,))
     result = self.cursor.fetchone()
     if result:
        gameroomData = json.loads(result[0])
        self.playerInfo = gameroomData["info"]["players"][str(lowId)]
        return self.playerInfo
     else:
        
        return None

    def updateGameroomPlayerInfo(self, lowId, roomId, playerInfo):
        query = "SELECT data FROM Gamerooms WHERE room_id = ?"
        data = self.fetchOne(query, [roomId])
        if data:
            gameroomData = json.loads(data[0])
            gameroomData["info"]["players"][str(lowId)] = playerInfo
            updateQuery = "UPDATE Gamerooms SET data = ? WHERE room_id = ?"
            self.executeQuery(updateQuery, [json.dumps(gameroomData), roomId])

    def updateGameroomInfo(self, value, roomId, index):
        query = "SELECT data FROM Gamerooms WHERE room_id = ?"
        data = self.fetchOne(query, [roomId])
        if data:
            gameroomData = json.loads(data[0])
            gameroomData["info"][index] = value
            updateQuery = "UPDATE Gamerooms SET data = ? WHERE room_id = ?"
            self.executeQuery(updateQuery, [json.dumps(gameroomData), roomId])
    def getGameroomInfo(self, index):
        self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (self.player.room_id,))
        result = self.cursor.fetchone()
        if result:
          gameroomData = json.loads(result[0])
          self.gameroomInfo = gameroomData[index]
          return self.gameroomInfo
        else:
        
          return None

    def removeGameroomPlayer(self, lowId, roomId, token):
     query = "SELECT data FROM Gamerooms WHERE room_id = ?"
     data = self.fetchOne(query, [roomId])
     #gameroomInfo = self.getGameroomInfo("info")
     if data:
        gameroomData = json.loads(data[0])
        if str(lowId) in gameroomData["info"]["players"]:
            del gameroomData["info"]["players"][str(lowId)] 
            gameroomData["info"]["player_count"] -= 1
            updateQuery = "UPDATE Gamerooms SET data = ? WHERE room_id = ?"
            self.executeQuery(updateQuery, [json.dumps(gameroomData), roomId])
            if gameroomData["info"]["player_count"] == 0:
               self.removeGameroom(roomId)
            else:
               updateQuery = "UPDATE Gamerooms SET data = ? WHERE room_id = ?"
               self.executeQuery(updateQuery, [json.dumps(gameroomData), roomId])
            
        else:
            print(f"Player with LowID {lowId} not found in RoomID {roomId}.")
        
     else:
        print(f"Room with ID {roomId} not found.")
     self.replaceOtherValue('room_id', 0, token)

    def removeGameroom(self, lowId):
     deleteQuery = "DELETE FROM Gamerooms WHERE room_id = ?"
     self.executeQuery(deleteQuery, [lowId])
     deleteQuery = "DELETE FROM GameroomChats WHERE room_id = ?"
     self.executeQuery(deleteQuery, [lowId])
     
    def loadRoomMessages(self, roomId):
        query = "SELECT data FROM GameroomChats WHERE room_id = ?"
        data = self.fetchOne(query, [roomId])
        if data:
            return json.loads(data[0])
        return None
    
    def getNextGameroomKey(self, roomId):
        query = "SELECT data FROM GameroomChats WHERE room_id = ?"
        data = self.fetchOne(query, [roomId])
        nextKey = 0
        if data:
            chatData = json.loads(data[0])
            messages = chatData["info"]["messages"]
            nextKey = str(max(map(int, messages.keys())) + 1 if messages else 0)
            try:
               return int(nextKey)
            except:
               return 0
        return 0

    def addGameroomMsg(self, roomId, eventType, playerId, playerName, msg, event, targetID = 0, targetName = ""):
        query = "SELECT data FROM GameroomChats WHERE room_id = ?"
        data = self.fetchOne(query, [roomId])
        if data:
            chatData = json.loads(data[0])
            messages = chatData["info"]["messages"]
            nextKey = str(max(map(int, messages.keys())) + 1 if messages else 0)
            messages[nextKey] = {
                "EventType": eventType,
                "Event": event,
                "Tick": int(nextKey)+1,
                "PlayerID": playerId,
                "PlayerName": playerName,
                "Message": msg,
                "promotedTeam": self.player.room_id,
                "TimeStamp": time.time(),
                "targetID": targetID,
                "targetName": targetName
            }
            updateQuery = "UPDATE GameroomChats SET data = ? WHERE room_id = ?"
            self.executeQuery(updateQuery, [json.dumps(chatData), roomId])

    def createClub(self, clubId, clubData, chatData):
        clubQuery = "INSERT INTO Clubs (club_id, data) VALUES (?, ?)"
        chatQuery = "INSERT INTO ClubChats (club_id, data) VALUES (?, ?)"
        self.executeQuery(clubQuery, [clubId, json.dumps(clubData)])
        self.executeQuery(chatQuery, [clubId, json.dumps(chatData)])

    def countClubs(self, minMembers, maxMembers, clubType, maxListLength):
     query = "SELECT club_id, data FROM Clubs"
     allClubs = self.fetchAll(query)
     clubList = []
     clubData = []

     for clubId, clubJson in allClubs:
        clubInfo = json.loads(clubJson)
        totalMembers = len(clubInfo["info"]["memberCount"])  # Access "memberCount" directly
        if minMembers <= totalMembers < maxMembers and clubInfo["info"]["clubType"] <= clubType:
            clubList.append(clubId)
            clubData.append(clubInfo)
            if len(clubList) == maxListLength:
                break

     return [clubList, clubData]
 
    def getClubId(self):
        self.cursor.execute("SELECT COUNT(*) FROM Clubs")
        self.player.club_id = self.cursor.fetchone()[0] + 1


    def loadClub(self, clubId):
        query = "SELECT data FROM Clubs WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        if data:
            return json.loads(data[0])
        return None
    
    def getMemberData(self, token):
        query = "SELECT data FROM Players WHERE token = ?"
        data = self.fetchOne(query, [token])
        if data:
            return json.loads(data[0])
        return None

    def addMember(self, clubId, playerToken, action):
        query = "SELECT data FROM Clubs WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        if data:
            clubData = json.loads(data[0])
            if action == 0:
                deleteQuery = "DELETE FROM Clubs WHERE club_id = ?"
                self.executeQuery(deleteQuery, [clubId])
            elif action == 1:
                clubData["info"]["memberCount"].append(playerToken)
                updateQuery = "UPDATE CLubs SET data = ? WHERE club_id = ?"
                self.executeQuery(updateQuery, [json.dumps(clubData), clubId])
            elif action == 2:
                clubData["info"]["memberCount"].remove(playerToken)
                updateQuery = "UPDATE Clubs SET data = ? WHERE club_id = ?"
                self.executeQuery(updateQuery, [json.dumps(clubData), clubId])

    def replaceClubValue(self, clubId, description, badgeId, clubType, trophiesNeeded):
        query = "SELECT data FROM Clubs WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        if data:
            clubData = json.loads(data[0])
            clubData["info"]["description"] = description
            clubData["info"]["clubBadge"] = badgeId
            clubData["info"]["clubType"] = clubType
            clubData["info"]["requiredTrophies"] = trophiesNeeded
            updateQuery = "UPDATE CLubs SET data = ? WHERE club_id = ?"
            self.executeQuery(updateQuery, [json.dumps(clubData), clubId])
            
    def loadClubMessages(self, clubId):
        query = "SELECT data FROM ClubChats WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        if data:
            return json.loads(data[0])
        return None
    
    def loadEvents(self, state):
        query = "SELECT data FROM Events WHERE state = ?"
        data = self.fetchOne(query, [state])
        if data:
            return json.loads(data[0])
        return None
    
    def loadPlayerOffers(self, token):
        query = "SELECT data FROM PlayerOffers WHERE PlayerToken = ?"
        data = self.fetchOne(query, [token])
        if data:
            return json.loads(data[0])
        return None
    
    def rerollEvents(self):
        
        self.cursor.execute("SELECT state, data FROM Events WHERE state = ?", [1])
        results = self.cursor.fetchall()
        for state, row in results:
            event = json.loads(row)
            updatedData = json.dumps(event)
        updateQuery = "UPDATE Events SET data = ? WHERE state = ?"
        self.cursor.execute(updateQuery, [updatedData, 2])
        for state, row in results:
            event = json.loads(row)
            
            eventData = event["info"]["events"]

            now = datetime.now()
            tomorrow = now + timedelta(days=1)
            timestamp = int(tomorrow.replace(hour=10, minute=0, second=0, microsecond=0).timestamp())
            for key, data in eventData.items():
                data["TimeStamp"] = timestamp
                if int(key) == 0:
                    gamemodes = Locations.getAllLocationsWithGamemode("CoinRush")
                elif int(key) == 1:
                    gamemodes = Locations.getAllLocationsWithGamemode("BattleRoyale")
                elif int(key) == 2:
                    gamemodes = Locations.getAllLocationsWithException(["CoinRush", "BattleRoyale", "Survival", "BossFight", "BattleRoyaleTeam"])
                elif int(key) == 3:
                    gamemodes = Locations.getAllLocationsWithException(["Survival", "BossFight"])
                else:
                    gamemodes = Locations.getAllLocationsWithGamemode("BattleRoyaleTeam")
                data["ID"] = random.choice(gamemodes)

        # Convert the modified event back to JSON and update in DB
            updatedData = json.dumps(event)
            updateQuery = "UPDATE Events SET data = ? WHERE state = ?"
            self.cursor.execute(updateQuery, [updatedData, state])

        self.connection.commit()
    
    def getNextKey(self, clubId):
        query = "SELECT data FROM ClubChats WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        nextKey = 0
        if data:
            chatData = json.loads(data[0])
            messages = chatData["info"]["messages"]
            nextKey = str(max(map(int, messages.keys())) + 1 if messages else 0)
            try:
               return int(nextKey)
            except:
               return 0
        return 0

    def addMsg(self, clubId, eventType, playerId, playerName, role, msg, event, targetID = 0, targetName = ""):
        query = "SELECT data FROM ClubChats WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        if data:
            chatData = json.loads(data[0])
            messages = chatData["info"]["messages"]
            nextKey = str(max(map(int, messages.keys())) + 1 if messages else 0)
            messages[nextKey] = {
                "EventType": eventType,
                "Event": event,
                "Tick": int(nextKey)+1,
                "PlayerID": playerId,
                "PlayerName": playerName,
                "PlayerRole": role,
                "Message": msg,
                "promotedTeam": self.player.room_id,
                "TimeStamp": time.time(),
                "targetID": targetID,
                "targetName": targetName
            }
            updateQuery = "UPDATE ClubChats SET data = ? WHERE club_id = ?"
            self.executeQuery(updateQuery, [json.dumps(chatData), clubId])
            
    def replaceMessageValue(self, tick, value_name, new_value):
        self.cursor.execute("SELECT data FROM ClubChats WHERE club_id = ?", (self.player.club_id,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            playerData["info"]["messages"][str(tick-1)][value_name] = new_value
            self.cursor.execute("UPDATE ClubChats SET data = ? WHERE club_id = ?", (json.dumps(playerData), self.player.club_id))
            self.connection.commit()
            
    


    def __del__(self):
        self.connection.close()
