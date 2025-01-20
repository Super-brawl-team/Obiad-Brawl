from Logic.Battle.Objects.Tile import Tile

class TileMap:
    TILE_SIZE = 300

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

        self.spawn_points = []
        self.spawn_points_team1 = []
        self.spawn_points_team2 = []

        idx = 0
        for i in range(height):
            for j in range(width):
                char = data[idx]
                logic_x = self.tile_to_logic(j)
                logic_y = self.tile_to_logic(i)
                tile = Tile(char, logic_x, logic_y)
                self.tiles[i][j] = tile

                if char == '1':
                    self.spawn_points.append(tile)
                    self.spawn_points_team1.append(tile)
                elif char == '2':
                    self.spawn_points.append(tile)
                    self.spawn_points_team2.append(tile)

                idx += 1

    @property
    def logic_width(self):
        return self.tile_to_logic(self.width)

    @property
    def logic_height(self):
        return self.tile_to_logic(self.height)

    def get_tile(self, x, y, is_tile=False):
        if not is_tile:
            x = self.logic_to_tile(x)
            y = self.logic_to_tile(y)

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None

    @staticmethod
    def logic_to_tile(logic_value):
        return logic_value // TileMap.TILE_SIZE

    @staticmethod
    def tile_to_logic(tile):
        return TileMap.TILE_SIZE * tile + TileMap.TILE_SIZE // 2

    def get_tiles(self):
        return self.tiles
