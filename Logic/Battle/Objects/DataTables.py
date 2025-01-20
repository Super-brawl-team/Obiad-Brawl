from enum import Enum
from collections import defaultdict
from Logic.Battle.Objects.GameFiles import Gamefiles
from Logic.Battle.Objects.DataType import DataType
from Logic.Battle.Objects.Table import Table


class Debugger:
    @staticmethod
    def print(message):
        print(message)


class DataTables:
    Gamefiles = {}
    Tables = None

    @staticmethod
    def add_files_to_load():
        DataTables.Gamefiles = {
            DataType.Projectile: "GameAssets/csv_logic/projectiles.csv",
            DataType.AllianceBadge: "GameAssets/csv_logic/alliance_badges.csv",
            DataType.Location: "GameAssets/csv_logic/locations.csv",
            DataType.Character: "GameAssets/csv_logic/characters.csv",
            DataType.AreaEffect: "GameAssets/csv_logic/area_effects.csv",
            DataType.Item: "GameAssets/csv_logic/items.csv",
            DataType.Skill: "GameAssets/csv_logic/skills.csv",
            DataType.Card: "GameAssets/csv_logic/cards.csv",
            DataType.Tile: "GameAssets/csv_logic/tiles.csv",
            DataType.PlayerThumbnail: "GameAssets/csv_logic/player_thumbnails.csv",
            DataType.Skin: "GameAssets/csv_logic/skins.csv",
        }

    @staticmethod
    def load():
        DataTables.add_files_to_load()

        DataTables.Tables = Gamefiles()

        for data_type, file_path in DataTables.Gamefiles.items():
            DataTables.Tables.initialize(Table(file_path), data_type)

        Debugger.print(f"{len(DataTables.Gamefiles)} Data Tables initialized!")

    @staticmethod
    def table_exists(data_type):
        return DataTables.Tables.contains_table(data_type)

    @staticmethod
    def get(data_type):
        return DataTables.Tables.get(data_type)