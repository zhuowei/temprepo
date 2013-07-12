import re
import sys

try:
    import readline  # if available, used by raw_input()
except:
    pass

# A corrupter of swords

snippets = []

def loadCorpus():
	newCharacterRe = re.compile(r"^  [A-Z]+\.")
	with open("pg1123.txt", "r") as infile:
		snippet = ""
		hasHitPlay = False
		for aline in infile:
			line = aline[0:len(aline) - 1]
			if not hasHitPlay:
				if line.find("ACT I") >= 0:
					hasHitPlay = True
				else:
					continue
			newCharacter = re.match(newCharacterRe, line)
			if newCharacter:
				if snippet != "":
					snippets.append(snippet)
					snippet = ""
			line = re.sub(newCharacterRe, "", line).strip()
			if len(line) < 1: continue
			snippet += line + "\n"

#	for a in snippets:
#		print a

def getResponse(needle):
	responses = []
	directresponses = []
	needleparts = needle.split(" ")
	for a in range(0, len(snippets)):
		snippet = snippets[a].lower()
		if snippet.find(needle) >= 0:
			directresponses.append(snippets[a+1])
			continue
		for ni in range(0, len(needleparts)):
			mneedleparts = needleparts[ni:]
			canfindnum = 0
			needlepoint = ""
			for needlepart in mneedleparts:
				if needlepoint == "":
					needlepoint = needlepart + " "
				else:
					needlepoint = needlepoint + needlepart + " "
				if snippet.find(needlepoint) >= 0:
					canfindnum = canfindnum + 1
			if canfindnum >= 2:
				responses.append((snippets[a+1], canfindnum))
				continue
	responses.sort(responseSorter)
	return (responses, directresponses)

def responseSorter(item1, item2):
	if item1[1] == item2[1]:
		return 0
	elif item1[1] > item2[1]:
		return -1
	else:
		return 1



def startMeUp():
	loadCorpus()
	while True:
		newquestion = raw_input(">")
		responses, directresponses = getResponse(newquestion.lower().replace("\n", "").strip())
		if len(directresponses) > 0:
			print directresponses[0]
		elif len(responses) > 0:
			print responses[0][0]


startMeUp()
