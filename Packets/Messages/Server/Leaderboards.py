from Utils.Writer import Writer











class Leaderboard(Writer):







	def __init__(self, device):



		super().__init__(device)


		self.device = device


		self.id = 24403








	def encode(self):



		self.writeVInt(1)#self.device.LeaderboardInfo)



		self.writeVInt(0)



		if self.device.LeaderboardType == 0:



			self.writeString()



		else:



			self.writeString("FR")




		if self.device.LeaderboardInfo == 0:



			self.writeVInt(2) # Players Count







			self.writeVInt(0) # High ID



			self.writeVInt(0) # Low ID







			self.writeVInt(1)



			self.writeVInt(999999) # Player Trophies







			self.writeVInt(1)







			self.writeString("PrimoDEVHacc")  # Player Name



			self.writeString("Primo Team") # Club Name







			self.writeVInt(500) # Player Level



			self.writeVInt(28)



			self.writeVInt(0)



			self.writeVInt(0)
			
			
			
			self.writeVInt(1) # High ID



			self.writeVInt(1) # Low ID







			self.writeVInt(2)



			self.writeVInt(999999) # Player Trophies







			self.writeVInt(2)







			self.writeString("ExplorateurSss")  # Player Name



			self.writeString("Primo Team") # Club Name







			self.writeVInt(500) # Player Level



			self.writeVInt(28)



			self.writeVInt(0)



			self.writeVInt(0)
			
		elif self.device.LeaderboardInfo == 1:



			self.writeVInt(2) # Players Count







			self.writeVInt(0) # High ID



			self.writeVInt(0) # Low ID







			self.writeVInt(1)



			self.writeVInt(1922) # Player Trophies







			self.writeVInt(1)







			self.writeString("PrimoDEVHacc")  # Player Name



			self.writeString("Primo Team") # Club Name







			self.writeVInt(28) # Player Level



			self.writeVInt(28)



			self.writeVInt(2)



			self.writeVInt(0)
			
			
			self.writeVInt(0) # High ID



			self.writeVInt(1) # Low ID







			self.writeVInt(1)



			self.writeVInt(1576) # Player Trophies







			self.writeVInt(1)







			self.writeString("ExplorateurSss")  # Player Name



			self.writeString("Primo Team") # Club Name







			self.writeVInt(16) # Player Level



			self.writeVInt(28)



			self.writeVInt(12)



			self.writeVInt(0)

		elif self.device.LeaderboardInfo == 2:



			self.writeVInt(1) # Clubs Count







			self.writeVInt(0) # Club High ID



			self.writeVInt(1) # Club Low ID







			self.writeVInt(1)



			self.writeVInt(9999) # Club Trophies



			self.writeVInt(2)







			self.writeString("Primooo") # Club Name



			self.writeVInt(1) # Club Members Count







			self.writeVInt(8) # Club Badge



			self.writeVInt(19) # Club Name Color



	  



		self.writeVInt(0)



		self.writeVInt(0)



		self.writeVInt(0)



		self.writeVInt(0)



		



		self.writeString("FR")



		print("[INFO] Message LeaderboardMessage has been sent.")

