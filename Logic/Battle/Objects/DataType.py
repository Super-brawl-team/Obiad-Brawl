from enum import Enum
from typing import Type, Dict
from Logic.Battle.Objects.DataTable import DataTable
from Logic.Battle.Objects.LogicData import LogicData
from Logic.Battle.Objects.Row import Row
# Enum definition in Python
class DataType(Enum):
    Projectile = 6
    AllianceBadge = 8
    Location = 15
    Character = 16
    AreaEffect = 17
    Item = 18
    Skill = 20
    Card = 23
    Tile = 27
    PlayerThumbnail = 28
    Skin = 29


# Example Data classes (these would be defined in your actual codebase)
class ProjectileData:
    pass


class AllianceBadgeData:
    pass


class LocationData:
    pass


class CharacterData:
    pass


class AreaEffectData:
    pass


class ItemData:
    pass


class SkillData:
    pass


class CardData:
    pass


class TileData:
    pass


class PlayerThumbnailData:
    pass


class SkinData:
    pass


# DataTables class in Python
class DataTables:
    DataTypes: Dict[DataType, Type] = {
        DataType.Projectile: ProjectileData,
        DataType.AllianceBadge: AllianceBadgeData,
        DataType.Location: LocationData,
        DataType.Character: CharacterData,
        DataType.AreaEffect: AreaEffectData,
        DataType.Item: ItemData,
        DataType.Skill: SkillData,
        DataType.Card: CardData,
        DataType.Tile: TileData,
        DataType.PlayerThumbnail: PlayerThumbnailData,
        DataType.Skin: SkinData,
    }

    Types: Dict[Type, DataType]

    # Static method to initialize Types dictionary
    @staticmethod
    def initialize_types():
        DataTables.Types = {v: k for k, v in DataTables.DataTypes.items()}

    @staticmethod
    def create(file: DataType, row: 'Row', data_table: 'DataTable') -> 'LogicData':
        """
        Creates and returns an instance of LogicData based on DataType
        """
        if file in DataTables.DataTypes:
            return DataTables.DataTypes[file](row, data_table)
        return None



