import sqlite3
import json
import time
import random
from Files.CsvLogic.Locations import Locations
import datetime 
from Files.CsvLogic.Cards import Cards
import copy
from datetime import datetime, timedelta
class DataBase:

    def __init__(self, player):
        self.player = player
        self.connection = sqlite3.connect('Database/database.db')
        self.cursor = self.connection.cursor()
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
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Battles (
            id INTEGER PRIMARY KEY,
            data TEXT
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Matchmaking (
            id INTEGER PRIMARY KEY,
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
            "coinsdoubler": self.player.coinsdoubler,
            "coinsbooster": self.player.coinsbooster,
            "trophies": self.player.trophies,
            "highest_trophies": self.player.trophies,
            "profile_icon": 0,
            "teamID": 0,
            "unlocked_brawlers": self.player.unlocked_brawlers,
            "friends": {},
            "last_connection_time": 0,
            "player_status": 0,
            "tutorialState": 0,
            "region": self.player.region,
            "control_mode": self.player.control_mode,
            "has_battle_hints": False,
            "battleID": 0
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
        self.cursor.execute("SELECT MAX(room_id) FROM Gamerooms")
        max_id = self.cursor.fetchone()[0]
        
        if max_id is None:  
            self.player.room_id = 1
        else:
            self.player.room_id = max_id + 1

    def createGameroom(self, roomType, chatData):
        
        data = {
            "room_id": self.player.teamID,
            "info": {
                "room_type": roomType,
                "practice": False,
                "map_id": self.player.map_id,
                "player_count": 1,
                "advertiseToBand": False,
                "alreadyAdvertisedToBand": False,
                "advertisedClub": [0, 0],
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

        self.cursor.execute("INSERT INTO Gamerooms (room_id, data) VALUES (?, ?)", (self.player.teamID, json.dumps(data)))
        
        chatQuery = "INSERT INTO GameroomChats (room_id, data) VALUES (?, ?)"
        self.executeQuery(chatQuery, [self.player.teamID, json.dumps(chatData)])
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
     self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (self.player.teamID,))
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
     self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (self.player.teamID,))
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
        self.cursor.execute("SELECT data FROM Gamerooms WHERE room_id = ?", (self.player.teamID,))
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

        if data:
            gameroomData = json.loads(data[0])
            if str(lowId) in gameroomData["info"]["players"]:
                del gameroomData["info"]["players"][str(lowId)]
                gameroomData["info"]["player_count"] -= 1

                if gameroomData["info"]["player_count"] == 0:
                    self.removeGameroom(roomId)  # udpate bc i suck
                else:
                    updateQuery = "UPDATE Gamerooms SET data = ? WHERE room_id = ?"
                    self.executeQuery(updateQuery, [json.dumps(gameroomData), roomId])
            else:
                print(f"Player with LowID {lowId} not found in RoomID {roomId}.")
        else:
            print(f"Room with ID {roomId} not found.")

        self.replaceOtherValue('teamID', 0, token)
        
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
                "promotedTeam": self.player.teamID,
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
        
    def restartClubOnlineMembers(self):
        query = "SELECT club_id, data FROM Clubs"
        allClubs = self.fetchAll(query)
        for clubId, clubJson in allClubs:
            clubInfo = json.loads(clubJson)
            clubInfo["info"]["onlineMembers"] = 0
            updateQuery = "UPDATE CLubs SET data = ? WHERE club_id = ?"
            self.executeQuery(updateQuery, [json.dumps(clubInfo), clubId])

    def countClubs(self, minMembers, maxMembers, clubType, maxListLength):
     query = "SELECT club_id, data FROM Clubs"
     allClubs = self.fetchAll(query)
     clubList = []
     clubData = []

     for clubId, clubJson in allClubs:
        clubInfo = json.loads(clubJson)
        totalMembers = len(clubInfo["info"]["memberCount"])
        if minMembers <= totalMembers < maxMembers and clubInfo["info"]["clubType"] <= clubType:
            clubList.append(clubId)
            clubData.append(clubInfo)
            if len(clubList) == maxListLength:
                break

     return [clubList, clubData]
 
    def getClubId(self):
        self.cursor.execute("SELECT MAX(club_id) FROM Clubs")
        max_id = self.cursor.fetchone()[0]
        
        if max_id is None:  
            self.player.club_id = 1
        else:
            self.player.club_id = max_id + 1


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
    
    def restartClubOnlineMembers(self):
        query = "SELECT club_id, data FROM Clubs"
        allClubs = self.fetchAll(query)
        for clubId, clubJson in allClubs:
            clubInfo = json.loads(clubJson)
            clubInfo["info"]["onlineMembers"] = 0
            updateQuery = "UPDATE CLubs SET data = ? WHERE club_id = ?"
            self.executeQuery(updateQuery, [json.dumps(clubInfo), clubId])
            
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
                clubData["info"]["onlineMembers"] += 1
                updateQuery = "UPDATE CLubs SET data = ? WHERE club_id = ?"
                self.executeQuery(updateQuery, [json.dumps(clubData), clubId])
            elif action == 2:
                clubData["info"]["memberCount"].remove(playerToken)
                clubData["info"]["onlineMembers"] -= 1
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
            
    def incrementClubTrophies(self, clubId, factor):
        query = "SELECT data FROM Clubs WHERE club_id = ?"
        data = self.fetchOne(query, [clubId])
        if data:
            clubData = json.loads(data[0])
            clubData["info"]["trhophies"] += factor
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
        now = datetime.now()
        is_weekend = now.weekday() in (5, 6)
        refresh_hours = {
            "0": 2,
            "1": 14,
            "2": 8,
            "3": 2
        }

        # --- Handle state 1 (active events)
        self.cursor.execute("SELECT data FROM Events WHERE state = 1")
        row = self.cursor.fetchone()
        if row:
            state1 = json.loads(row[0])
            events1 = state1["info"]["events"]

            if "3" in events1 and not is_weekend:
                event3 = events1.pop("3")

                self.cursor.execute("SELECT data FROM Events WHERE state = 2")
                row2 = self.cursor.fetchone()
                state2 = json.loads(row2[0]) if row2 else {"info": {"events": {}}}
                state2["info"]["events"]["3"] = event3
                self.cursor.execute("UPDATE Events SET data = ? WHERE state = 2", [json.dumps(state2)])

            for key, data in events1.items():
                if key in refresh_hours:
                    if "TimeStamp" in data and now.timestamp() >= data["TimeStamp"]:
                        next_time = now + timedelta(hours=refresh_hours[key])
                        data["TimeStamp"] = int(next_time.timestamp())
                        data["ID"] = random.choice(Locations().GetLocations())


            self.cursor.execute("UPDATE Events SET data = ? WHERE state = 1", [json.dumps(state1)])

        # --- Handle state 2 (comming soon)
        self.cursor.execute("SELECT data FROM Events WHERE state = 2")
        row2 = self.cursor.fetchone()
        if row2:
            state2 = json.loads(row2[0])
            events2 = state2["info"]["events"]

            if is_weekend and "3" in events2:
                event3 = events2.pop("3")

                self.cursor.execute("SELECT data FROM Events WHERE state = 1")
                row1 = self.cursor.fetchone()
                state1 = json.loads(row1[0]) if row1 else {"info": {"events": {}}}
                state1["info"]["events"]["3"] = event3
                self.cursor.execute("UPDATE Events SET data = ? WHERE state = 1", [json.dumps(state1)])
                self.cursor.execute("UPDATE Events SET data = ? WHERE state = 2", [json.dumps(state2)])

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
                "promotedTeam": self.player.teamID,
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
            
    def createMatchmakingData(self):
        self.cursor.execute("SELECT COUNT(*) FROM Matchmaking WHERE id = ?", (self.player.battleID,))
        count = self.cursor.fetchone()[0]
        if count > 0:
            raise ValueError(f"match with id {self.player.battleID} already exists.")
        data = {"battleTicks": 0, "maximumPlayers": 2, "startedTime": time.time(), "displayTime": 20, "mapID": self.player.map_id, "players": [self.player.low_id]}
        self.cursor.execute("INSERT INTO Matchmaking (id, data) VALUES (?, ?)", (self.player.battleID, json.dumps(data)))
        #self.createOffer(self.player.token)
        self.connection.commit()
    def updateMatchmake(self, id, battle):

            updateQuery = "UPDATE Matchmaking SET data = ? WHERE id = ?"
            self.executeQuery(updateQuery, [json.dumps(battle), id])
    def loadMatchmakingData(self, battleID):
        placeholders = ",".join(["?"] * len(battleID))
        query = f"SELECT data FROM Matchmaking WHERE id IN ({placeholders})"
        self.cursor.execute(query, battleID) 
        results = self.cursor.fetchall()
        return [json.loads(row[0]) for row in results]
    def createBattle(self):
        self.cursor.execute("SELECT COUNT(*) FROM Battles WHERE id = ?", (self.player.battleID,))
        count = self.cursor.fetchone()[0]
        if count > 0:
            raise ValueError(f"battle with id {self.player.battleID} already exists.")
        destructibleTiles = {}
        defaultX = [1950, 2550, 3150, 1950, 2550, 3150]
        defaultAngle = [270, 270, 270, 90, 90, 90]
        defaultY = [9750, 9750, 9750, 150, 150 ,150]
        csvid = [self.player.brawler_id]
        BrawlersList = Cards().getBrawlers()
        for x in range(5):
            
            csvid.append(random.choice(BrawlersList))
        csvid.append(10)
        ultiArray = {str(i): copy.deepcopy({"unknown": True, "hasUlti": True, "ultiCharge": 1000}) for i in range(1, 7)}
        killArray = {str(i): copy.deepcopy({"score": 0, "entry": {}}) for i in range(1, 7)}
        objectInfos = {"x": 0, "y": 0, "index": 0, "z": 0, "visibilty": 10}
        heroes = {str(i): copy.deepcopy({"objectInfos": {"x": defaultX[i-1], "y": defaultY[i-1], "index": i-1 if i<=3 else i+15, "z": 0, "visibility": 10}, "teamRotation": defaultAngle[i-1], "ennemyRotation": defaultAngle[i-1], "state": 0, "slowed": False, "unknown": False, "playingAnAnimation": True, "playedAnimation": 63, "rotationRelated": False, "stunned": False, "unknown2": False, "isPoisonned": False, "unknown3": 0, "unknown4": 0, "currentHP": 800, "maximumHP": 800, "itemsAmount": 1, "unknown5": 0, "unknown6": 0, "unknown7": False, "hasImmunityShield": False, "rotationRelated2": False, "hasRage": False, "ultiAiming": False, "activedUlti": False, "invisible": False, "notFullyVisible": False, "unknown8": 0, "unknown9": True, "unknown10": 0, "damagesArray": {}, "skillsArray": {"Weapon": {"activeTicks": 0, "unknown": False, "unknown1": 0, "ammos": 3000}, "Ulti": {"activeTicks": 0, "unknown": False, "unknown1": 0, "ammos": 3000}}}) for i in range(1, 7)}
        projectiles = {str(i): copy.deepcopy({"objectInfos": objectInfos, "state": 0, "path": 992, "unknown": False}) for i in range(0)}
        characters = {str(i): copy.deepcopy({"objectInfos": objectInfos}) for i in range(0)}
        items = {str(i): copy.deepcopy({"objectInfos": {"x": 2550, "y": 4950, "index": i+102, "z": 0, "visibility": 10}}) for i in range(1, 2)}
        areaEffects = {str(i): copy.deepcopy({"objectInfos": objectInfos}) for i in range(0)}
        gameObjectsArray = {"count": 7, "csvIDArray": {str(i): copy.deepcopy({"classID": 16 if i < 7 else 18, "instanceID": csvid[i-1]}) for i in range(1, 8)}, "indexArray": {str(i): copy.deepcopy({"classID": 2  if i < 7 else 4, "instanceID": i-1 if i < 7 else i-7}) for i in range(1, 8)}, "gameObjects": {"heroes": heroes, "projectiles": projectiles, "areaEffects": areaEffects, "characters": characters, "items": items}}
        data = {"globalID": 2000000, "fadeCounter": 0, "isGameOver": False, "unknownBoolean": True, "unkMapSize": 0, "unkMapSize2": 0, "tileMapWidth": 0, "tileMapHeight": 0, "destructibleTiles": destructibleTiles, "ultiArray": ultiArray, "progressionSelf": 0, "progressionRival": 0, "killArray": killArray, "gameObjects": gameObjectsArray}
        self.cursor.execute("INSERT INTO Battles (id, data) VALUES (?, ?)", (self.player.battleID, json.dumps(data)))
        #self.createOffer(self.player.token)
        self.connection.commit()
    def getBattleInfo(self, id_list):
        placeholders = ",".join(["?"] * len(id_list))
        query = f"SELECT data FROM Battles WHERE id IN ({placeholders})"
        self.cursor.execute(query, id_list)
        results = self.cursor.fetchall()
        return [json.loads(row[0]) for row in results]
    def clearMatchmake(self, id):
        deleteQuery = "DELETE FROM Matchmaking WHERE id = ?"
        self.executeQuery(deleteQuery, [id])
    def clearBattle(self, id):
        deleteQuery = "DELETE FROM Battles WHERE id = ?"
        self.executeQuery(deleteQuery, [id])
    def updateBattle(self, id, battle):

            updateQuery = "UPDATE Battles SET data = ? WHERE id = ?"
            self.executeQuery(updateQuery, [json.dumps(battle), id])
    def createBattleID(self):
        self.cursor.execute("SELECT MAX(id) FROM Matchmaking")
        max_id = self.cursor.fetchone()[0]
        
        if max_id is None:  
            self.player.battleID = 1
        else:
            self.player.battleID = max_id + 1


    def __del__(self):
        self.connection.close()
