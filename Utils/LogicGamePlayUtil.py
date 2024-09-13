import math
class LogicGameModeUtil:
    def getPlayerCountWithGameMode(gameModeVariation):
        if (gameModeVariation | 4) == 7:
            playerCount = 3
        else:
            playerCount = 6
        
        if gameModeVariation == 6:
            playerCount = 10
            
        if gameModeVariation:
            return playerCount
        else:
            return 10
    
    def getDistanceBetween(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def getClosestLevelBorderCollision(a1, a2, a3, a4, a5, a6, a7):
        v11 = 95 if a6 else 0
        v12 = a3 - a1
        v13 = v11 + 1
        v14 = a2 - (v11 + 1)
        v15 = -2 - v11
        v16 = a4 - a2
        v17 = a1 - (v11 + 1)
        v18 = v15 + a5[112]
        v19 = -((a4 - a2) * (v18 - v13))
        v20 = v14 * v12 - v17 * (a4 - a2)
        v21 = v20 / v19
        if 0 <= v21 <= 1:
            v22 = v20 / v19
            if v22 >= 0:
                v23 = 4
                if v22 <= 1:
                    a7[1] = int(a2 + v21 * v16)
                    a7[0] = int(a1 + v21 * v12)
                    return v23
        v24 = v15 + a5[116]
        v25 = (v24 - v13) * v12
        v21 = -(v17 * (v24 - v13)) / v25
        if 0 <= v21 <= 1:
            v26 = v20 / v25
            if v26 >= 0:
               v23 = 2
               if v26 <= 1:
                a7[1] = int(a2 + v21 * v16)
                a7[0] = int(a1 + v21 * v12)
                return v23
        v27 = -(v16 * (v13 - v18))
        v21 = ((a2 - v24) * (v13 - v18)) / v27
        v28 = (a2 - v24) * v12 - (a1 - v18) * v16
        if 0 <= v21 <= 1:
         v29 = v28 / v27
         if v29 >= 0:
            v23 = 1
            if v29 <= 1:
                a7[1] = int(a2 + v21 * v16)
                a7[0] = int(a1 + v21 * v12)
                return v23
        v30 = v13 - v24
        v31 = (a1 - v18) * v30
        v32 = v30 * v12
        v21 = -v31 / v32
        if 0 <= v21 <= 1:
         v34 = v28 / v32
         if v34 >= 0:
            v23 = 3
            if v34 <= 1:
                a7[1] = int(a2 + v21 * v16)
                a7[0] = int(a1 + v21 * v12)
                return v23
        return 0
    def getKillerIndexToSpectate(a1, a2):
     v2 = a2[2]
     if v2 < 1:
        return -1
     v3 = 0
     v4 = a1[160]
     while True:
        v5 = 0
        while True:
            v6 = a2[v5]
            if v6:
                if v6[8] == v4:
                    break
            if v2 == v5 + 1:
                break
        if v6[48]:
            return v4
        v4 = v6[160]
        if v3 + 1 != v2:
            v3 += 1
            continue
        break
     i = a2[0]
     while True:
        v9 = i[0]
        v10 = v9 == 0
        if v9:
            v10 = v9[12] == a1[12]
        if not v10 and v9[48]:
            break
        v2 -= 1
        if not v2:
            return -1
        i += 1
     return v9[8]



