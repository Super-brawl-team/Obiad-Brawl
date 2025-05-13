from Logic.Player import Player
from Logic.Milestones import Milestones
from Database.DatabaseManager import DataBase
from Utils.Reader import ByteStream
from Files.CsvLogic.playerThumbnails import playerThumbnails
from Files.CsvLogic.Characters import Characters
class LogicSetPlayerThumbnailCommand(ByteStream):
    def __init__(self, device, player, data):
        super().__init__(data)
        self.player = player
        self.device = device

    def decode(self):
        self.readCommandHeader()
        self.selected_icon = self.readDataReference()
        
    def process(self):
        db = DataBase(self.player)
        RequiredExps = Milestones.ProgressStartExp
        if self.selected_icon[1] not in playerThumbnails.getAllThumbnails(self):
            return "kek"
        elif playerThumbnails.getRequiredTrophiesForThumbnail(self, self.selected_icon[1]) >self.player.trophies:
            return "kek"
        elif str(Characters().getCharacterByName(playerThumbnails.getRequiredBrawlerForThumbnail(self, self.selected_icon[1]))) not in self.player.unlocked_brawlers:
            return "kek"
        requiredExpLevelForThumb = playerThumbnails.getRequiredExpForThumbnail(self, self.selected_icon[1])
        requiredExpForThumb = RequiredExps[requiredExpLevelForThumb-1]
        if requiredExpLevelForThumb != 0 and requiredExpForThumb > self.player.player_experience:
            return "kek"
        self.player.profile_icon = self.selected_icon[1]
        db.replaceValue('profile_icon', self.player.profile_icon)
        
        