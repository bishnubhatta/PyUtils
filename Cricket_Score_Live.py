from pycricbuzz import Cricbuzz
c = Cricbuzz()
matches = c.matches()
print matches
for match in matches:
    if(match['mchdesc'] == 'BAN vs IND'):
		print c.livescore(match['id'])["matchinfo"]["status"]
		print "Current Score: " + c.livescore(match['id'])["batting"]["score"][0]["runs"] + " for " + \
			  c.livescore(match['id'])["batting"]["score"][0]["wickets"] + " wickets in " + \
			  c.livescore(match['id'])["batting"]["score"][0]["overs"] + " Overs"
		print c.livescore(match['id'])["batting"]["batsman"][0]["name"] + " is batting at :" + \
			  c.livescore(match['id'])["batting"]["batsman"][0]["runs"]
		print c.livescore(match['id'])["batting"]["batsman"][1]["name"] + " is batting at :" + \
			  c.livescore(match['id'])["batting"]["batsman"][1]["runs"]
		#print c.livescore(match['id'])