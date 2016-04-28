from django.shortcuts import render, redirect
from django.views.generic import View
from threading import Timer

# Create your views here.
# Declare Global variables

log = []
inventory = []
didDie = []
story = {
		'log' : log,
		'inventory' : inventory
		}




def postDirector(request):
	request.session['action'] = request.POST['action']
	if request.session['location'] == 'Palace Chambers':
		return redirect('startPost')
	elif request.session['location'] == 'North of Mountains':
		return redirect('mountainsPost')
	elif request.session['location'] == 'Cold Room':
		return redirect('ColdRoomPost')
	elif request.session['location'] == 'Prison Hallway':
		return redirect('prisonHallPost')
	elif request.session['location'] == 'Open Room':
		return redirect('openRoomPost')
	elif request.session['location'] == 'Sphinx Lair':
		return redirect('sphinxLairPost')
	elif request.session['location'] == 'Space Room':
		return redirect('spaceRoomPost')
	elif request.session['location'] == 'Cypher Room':
		return redirect('cypherRoomPost')
	elif request.session['location'] == 'Dragons Lair':
		return redirect('dragonsLairPost')
	else:
		return redirect('start')

def newGame(request):
	del log[:]
	del didDie[:]
	del inventory[:]
	request.session['location'] = 'Palace Chambers'
	return redirect('start')


class Start(object):
	# event = []
	location = 'Palace Chambers'
	startPostprivateLog = []
	

class StartGet(Start, View):
	event = []
	def get(self, request):
		del self.event[:]
		del self.startPostprivateLog[:]
		del request.session['inventory'][:]
		if ('dead' in didDie):
			self.event.append('******* YOU HAVE FAILED YOUR PRINCESS. TRY AGAIN *******')
		self.request.session['location'] = self.location
		self.event.append('It is a beautiful day in the Kingdom.')
		self.event.append('The princess sits on her throne ready to lead.')
		self.event.append('There is a banner on the wall.')
		self.event.append('BRAKOOMMMMMMMMM')
		self.event.append('You hear a large crash up above as a winged behemoth swoops down and grabs up the princess.')
		self.event.append('As it flies off it drops a scroll...')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', {'log' : log, 'inventory' : inventory})

class StartPost(StartGet, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if ('Scroll') not in request.session['inventory']:
			scroll = False
		else:
			scroll = True

		if ('Read scroll') not in self.startPostprivateLog:
			scrollRead = False
		else:
			scrollRead = True
		
		if (request.session['action'] == 'pick up scroll' and scroll == True) or (request.session['action'] == 'Pick up scroll' and scroll == True) or (request.session['action'] == 'grab the scroll' and scroll == True) or (request.session['action'] == 'Grab the scroll' and scroll == True) or (request.session['action'] == 'grab scroll' and scroll == True) or (request.session['action'] == 'Grab scroll' and scroll == True):
			self.event.append('Nothing to pick up.')
		elif (request.session['action'] == 'pick up scroll' and scroll == False) or (request.session['action'] == 'Pick up scroll' and scroll == False) or (request.session['action'] == 'grab the scroll' and scroll == False) or (request.session['action'] == 'Grab the scroll' and scroll == False) or (request.session['action'] == 'grab scroll' and scroll == False) or (request.session['action'] == 'Grab scroll' and scroll == False):
			self.event.append('Picked up scroll.')
			scroll = True
			request.session['inventory'] = ['Scroll']
		elif (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			self.event.append('There is a scroll on the ground and a banner on the wall. Also the palace just got a new sun roof.')
		elif (request.session['action'] == 'pick up banner') or (request.session['action'] == 'Pick up banner'):
			self.event.append('You cannot pick up the banner. It is attached to the wall.')
		elif (request.session['action'] == 'read banner') or (request.session['action'] == 'Read banner') or (request.session['action'] == 'read the banner') or (request.session['action'] == 'Read the banner') or (request.session['action'] == 'look at banner') or (request.session['action'] == 'Look at banner'):
			self.event.append('******** Welcome to Medieval Space Adventure. MSA is a game of adventure, peril and cunning. You are about to embark on a journey, the likes of which few have ever imagined. In MSA the courageous adventurer discovers the secrets of his worlds mythical creatures origins. He is cast into a series of puzzles, only the most cunning are to survive. You can interact with the game environment with commands such as "look around", "use western door", "attack \'creature\'", "pick up \'item\'", "read item", etc. You dont need to use the word "the". For example you can say "pick up sword" instead of "pick up THE sword". You also dont need to capitalize and of the words in your commands or add punctuation. MSA was developed by Kerrin Arora during a rainy week in Houston, TX. It was inspired by the 1980s game, ZORK. MSA was written in Python using the Django Framework. For any comments, feel free to email me at kerrin.arora@gmail.com! *********')
		elif (scroll == False and request.session['action'] == 'read scroll') or (scroll == False and request.session['action'] == 'Read scroll'):
			self.event.append('You must first pick up scroll')
		elif (scroll == True and request.session['action'] == 'read scroll') or (scroll == True and request.session['action'] == 'Read scroll'):
			self.event.append('******** Your Princess now belongs in my castle... Bring 2000 gold pieces to the castle North of the mountains for her return *********')
			self.startPostprivateLog.append('Read scroll')
			self.event.append('Would you like to save the Princess? Y/N')
		elif scrollRead == True:
			if (request.session['action'] == 'Y') or (request.session['action'] == 'y') or (request.session['action'] == 'yes') or (request.session['action'] == 'Yes'):
				return redirect('mountains')
			else:
				scrollRead = False
		else:
			self.event.append('Not Understood.')
		print(request.session['inventory'])
		# startPostprivateLog.append(request.session["action"])
		return render(request, 'game/index.html', story)

class Mountains(object):
	event = []
	location = 'North of Mountains'

class MountainsGet(Mountains, View):
	def get(self, request):
		del self.event[:]
		self.request.session['location'] = self.location
		self.event.append('After many days journey, you and a group of men have finally arrived at the castle north of the Mountains.')
		self.event.append('It is an odd castle of a shape never seen before and made of metal.')
		self.event.append('Suddenly the castle seems to come alive!')
		self.event.append('It begins to hover above the ground as lights emit from all sides')
		self.event.append('A strange beam shines down onto the cart of gold. The gold begins to float up toward the light.')
		self.event.append('Do you jump in after it? Y/N')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)

class MountainsPost(Mountains, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if (request.session['action'] == 'y') or (request.session['action'] == 'Y') or (request.session['action'] == 'yes') or (request.session['action'] == 'Yes'):
			self.event.append('You jump in after the gold. Everything goes dark...')
			return redirect('ColdRoom')
		elif (request.session['action'] == 'n') or (request.session['action'] == 'N') or (request.session['action'] == 'no') or (request.session['action'] == 'No'):
			self.event.append('** The Counsil Elders are disappointed with your failure. You are to be executed... **')
			didDie.append('dead')
			return redirect('start')
		else:
			self.event.append('Not Understood.')
		return render(request, 'game/index.html', story)

class ColdRoom(object):
	event = []
	location = 'Cold Room'

class ColdRoomGet(ColdRoom, View):
	def get(self, request):
		del self.event[:]
		self.request.session['location'] = self.location
		self.event.append('You awaken in a prison cell.')
		self.event.append('Three walls are bare metal while the west wall is replaced with bars')
		self.event.append('Just beyond the bars you see an orc sleeping with a key hanging loosly from his side.')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)

class ColdRoomPost(ColdRoom, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if ('Bronze Key' not in request.session['inventory']):
			bronzeKey = False
		else:
			bronzeKey = True
		if (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			self.event.append('The Northern, Eastern, and Southern walls are all bare. The western wall is replaced with steel bars. Through the bars you can see an orc sleeping near by with a key hanging loosly from his pocket.')
		elif (request.session['action'] == 'break bars') or (request.session['action'] == 'Break bars'):
			self.event.append('They are too strong')
		elif (request.session['action'] == 'scream') or (request.session['action'] == 'Scream') or (request.session['action'] == 'yell') or (request.session['action'] == 'Yell'):
			self.event.append('You dont want to wake the guard. He doesnt look friendly')
		elif (request.session['action'] == 'grab key' and bronzeKey == False) or (request.session['action'] == 'Grab key' and bronzeKey == False) or (request.session['action'] == 'reach for key' and bronzeKey == False) or (request.session['action'] == 'Reach for key' and bronzeKey == False) or (request.session['action'] == 'grab the key' and bronzeKey == False) or (request.session['action'] == 'Grab the key' and bronzeKey == False) or (request.session['action'] == 'steal the key' and bronzeKey == False) or (request.session['action'] == 'Steal the key' and bronzeKey == False) or (request.session['action'] == 'steal key' and bronzeKey == False) or (request.session['action'] == 'Steal key' and bronzeKey == False):
			self.event.append('You slowly and quietly squeeze your arm through the bars. Your face is smushed against the cold metal as you twidle at the key. The key holder drops but you catch it just in time!')
			self.bronzeKey = True
			request.session['inventory'].append('Bronze Key')
			self.event.append('Bronze Key was added to your inventory')
		elif (request.session['action'] == 'grab key' and bronzeKey == True) or (request.session['action'] == 'Grab key' and bronzeKey == True) or (request.session['action'] == 'reach for key' and bronzeKey == True) or (request.session['action'] == 'Reach for key' and bronzeKey == True) or (request.session['action'] == 'grab the key' and bronzeKey == True) or (request.session['action'] == 'Grab the key' and bronzeKey == True):
			self.event.append('You already have the key.')
		elif (bronzeKey == True and request.session['action'] == 'use key') or (bronzeKey == True and request.session['action'] == 'Use key') or (bronzeKey == True and request.session['action'] == 'unlock door') or (bronzeKey == True and request.session['action'] == 'Unlock door') or (bronzeKey == True and request.session['action'] == 'unlock cell') or (bronzeKey == True and request.session['action'] == 'Unlock cell') or (bronzeKey == True and request.session['action'] == 'unlock') or (bronzeKey == True and request.session['action'] == 'Unlock') or (bronzeKey == True and request.session['action'] == 'use bronze key') or (bronzeKey == True and request.session['action'] == 'Use bronze key') or (bronzeKey == True and request.session['action'] == 'open door') or (bronzeKey == True and request.session['action'] == 'Open door') or (bronzeKey == True and request.session['action'] == 'open the door') or (bronzeKey == True and request.session['action'] == 'Open the door') or (bronzeKey == True and request.session['action'] == 'unlock cell') or (bronzeKey == True and request.session['action'] == 'Unlock cell') or (bronzeKey == True and request.session['action'] == 'open cell') or (bronzeKey == True and request.session['action'] == 'Open cell') or (bronzeKey == True and request.session['action'] == 'open the cell') or (bronzeKey == True and request.session['action'] == 'Open the cell'):
			self.event.append('The prison door unlocks.')
			return redirect('prisonHall')
		elif (bronzeKey == False and request.session['action'] == 'use key') or (bronzeKey == False and request.session['action'] == 'Use key') or (bronzeKey == False and request.session['action'] == 'unlock door') or (bronzeKey == False and request.session['action'] == 'Unlock door') or (bronzeKey == False and request.session['action'] == 'unlock cell') or (bronzeKey == False and request.session['action'] == 'Unlock cell') or (bronzeKey == False and request.session['action'] == 'unlock') or (bronzeKey == False and request.session['action'] == 'Unlock') or (bronzeKey == False and request.session['action'] == 'use bronze key') or (bronzeKey == False and request.session['action'] == 'Use bronze key'):
			self.event.append('You dont have the key.')
		else:
			self.event.append('Not Understood.')
		print(request.session['inventory'])
		return render(request, 'game/index.html', story)


class PrisonHall(object):
	event = []
	location = 'Prison Hallway'
	hallPostprivateLog = []

class PrisonHallGet(PrisonHall, View):
	def get(self, request):
		del self.event[:]
		del self.hallPostprivateLog[:]
		self.request.session['location'] = self.location
		self.event.append('You slowly creep out of your cell, making sure not to awaken the guard.')
		self.event.append('There is a door to the west and one to the north. The Orc Guard is still asleep.')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)

class PrisonHallPost(PrisonHall, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if ('Sword') not in request.session['inventory']:
			armed = False
		else:
			armed = True
		if ('west Opened') not in self.hallPostprivateLog:
			westOpened = False
		else:
			westOpened = True
		if ('orcDead') not in self.hallPostprivateLog:
			OrcDead = False
		else:
			OrcDead = True
		if (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			self.event.append('There is a door to the west and one to the north. The Orc Guard is still asleep.')
		elif (request.session['action'] == 'open door') or (request.session['action'] == 'Open door') or (request.session['action'] == 'use door') or (request.session['action'] == 'Use door') or (request.session['action'] == 'door') or (request.session['action'] == 'Door'):
			self.event.append('Please specify which door.')
		elif (armed == False and request.session['action'] == 'open west door') or (armed == False and request.session['action'] == 'Open west door') or (armed == False and request.session['action'] == 'use west door') or (armed == False and request.session['action'] == 'Use west door') or (armed == False and request.session['action'] == 'west door') or (armed == False and request.session['action'] == 'West door') or (armed == False and request.session['action'] == 'open western door') or (armed == False and request.session['action'] == 'Open western door') or (armed == False and request.session['action'] == 'use western door') or (armed == False and request.session['action'] == 'Use western door') or (armed == False and request.session['action'] == 'western door') or (armed == False and request.session['action'] == 'Western door'):
			self.event.append('You slowly open the western door, revealing a closet with your sword lying there.')
			self.hallPostprivateLog.append('west Opened')
			westOpened = True
		elif (armed == True and request.session['action'] == 'open west door') or (armed == True and request.session['action'] == 'Open west door') or (armed == True and request.session['action'] == 'use west door') or (armed == True and request.session['action'] == 'Use west door') or (armed == True and request.session['action'] == 'west door') or (armed == True and request.session['action'] == 'West door') or (armed == True and request.session['action'] == 'open western door') or (armed == True and request.session['action'] == 'Open western door') or (armed == True and request.session['action'] == 'use western door') or (armed == True and request.session['action'] == 'Use western door') or (armed == True and request.session['action'] == 'western door') or (armed == True and request.session['action'] == 'Western door'):
			self.event.append('You slowly open the western door, There is nothing in here')
			self.hallPostprivateLog.append('west Opened')
			westOpened = True
			# stuff
		elif (OrcDead == False and request.session['action'] == 'open north door') or (OrcDead == False and request.session['action'] == 'Open north door') or (OrcDead == False and request.session['action'] == 'use north door') or (OrcDead == False and request.session['action'] == 'Use north door') or (OrcDead == False and request.session['action'] == 'north door') or (OrcDead == False and request.session['action'] == 'north Door') or (OrcDead == False and request.session['action'] == 'open northern door') or (OrcDead == False and request.session['action'] == 'Open northern door') or (OrcDead == False and request.session['action'] == 'use northern door') or (OrcDead == False and request.session['action'] == 'Use northern door') or (OrcDead == False and request.session['action'] == 'Northern door') or (OrcDead == False and request.session['action'] == 'northern Door'):
			self.event.append('The rusted hinges scream as you pull the northern door open.')
			self.event.append('The Orc guard wakes up and charges towards you, furiously swinging his club.')
			self.event.append('The blow knocks you back against the wall. Everything goes dark as your body goes limp...')
			didDie.append('dead')
			return redirect('start')
			#did die event
		elif (OrcDead == True and request.session['action'] == 'open north door') or (OrcDead == True and request.session['action'] == 'Open north door') or (OrcDead == True and request.session['action'] == 'use north door') or (OrcDead == True and request.session['action'] == 'Use north door') or (OrcDead == True and request.session['action'] == 'north door') or (OrcDead == True and request.session['action'] == 'north Door') or (OrcDead == True and request.session['action'] == 'open northern door') or (OrcDead == True and request.session['action'] == 'Open northern door') or (OrcDead == True and request.session['action'] == 'use northern door') or (OrcDead == True and request.session['action'] == 'Use northern door') or (OrcDead == True and request.session['action'] == 'Northern door') or (OrcDead == True and request.session['action'] == 'northern Door'):
			self.event.append('The rusted hinges scream as you pull the northern door open.')
			return redirect('openRoom')
		elif (armed == True and request.session['action'] == 'attack guard') or (armed == True and request.session['action'] == 'Attack guard') or (armed == True and request.session['action'] == 'kill guard') or (armed == True and request.session['action'] == 'Kill guard') or (armed == True and request.session['action'] == 'hit guard') or (armed == True and request.session['action'] == 'Hit guard') or (armed == True and request.session['action'] == 'attack orc') or (armed == True and request.session['action'] == 'Attack orc') or (armed == True and request.session['action'] == 'kill orc') or (armed == True and request.session['action'] == 'Kill orc') or (armed == True and request.session['action'] == 'hit orc') or (armed == True and request.session['action'] == 'Hit orc'):
			self.event.append('You expertly slash at the sleeping Orc\'s chest. Blood starts to curdle on the sides of his mouth as his eyes dart around scanning for anything that can help.')
			self.event.append('His body goes limp as his eyes glaze over.')
			self.hallPostprivateLog.append('orcDead')
		elif (armed == False and request.session['action'] == 'attack guard') or (armed == False and request.session['action'] == 'Attack guard') or (armed == False and request.session['action'] == 'kill guard') or (armed == False and request.session['action'] == 'Kill guard') or (armed == False and request.session['action'] == 'hit guard') or (armed == False and request.session['action'] == 'Hit guard') or (armed == False and request.session['action'] == 'attack orc') or (armed == False and request.session['action'] == 'Attack orc') or (armed == False and request.session['action'] == 'kill orc') or (armed == False and request.session['action'] == 'Kill orc') or (armed == False and request.session['action'] == 'hit orc') or (armed == False and request.session['action'] == 'Hit orc'):
			self.event.append('Not having any weapon doesnt deter you as you run up and punch the sleeping Orc with all your might.')
			self.event.append('The Orc falls backward out of his seat.')
			self.event.append('He jumps to his feet and charges at you with all his might.')
			self.event.append('The blow throws you against the wall. Everything goes dark as your body goes limp...')
			didDie.append('dead')
			return redirect('start')
			# enter DEAD event
		elif (westOpened == True and armed == False and request.session['action'] == 'take sword') or (westOpened == True and armed == False and request.session['action'] == 'Take sword') or (westOpened == True and armed == False and request.session['action'] == 'grab sword') or (westOpened == True and armed == False and request.session['action'] == 'Grab sword') or (westOpened == True and armed == False and request.session['action'] == 'pick up sword') or (westOpened == True and armed == False and request.session['action'] == 'Pick up sword'):
			request.session['inventory'].append('Sword')
			self.event.append('Sword has been added to your inventory')
		elif (westOpened == False and request.session['action'] == 'take sword') or (westOpened == False and request.session['action'] == 'Take sword') or (westOpened == False and request.session['action'] == 'grab sword') or (westOpened == False and request.session['action'] == 'Grab sword') or (westOpened == False and request.session['action'] == 'pick up sword') or (westOpened == False and request.session['action'] == 'Pick up sword'):
			self.event.append('There are no weapons around.')
		elif (armed == True and request.session['action'] == 'take sword') or (armed == True and request.session['action'] == 'Take sword') or (armed == True and request.session['action'] == 'grab sword') or (armed == True and request.session['action'] == 'Grab sword') or (armed == True and request.session['action'] == 'pick up sword') or (armed == True and request.session['action'] == 'Pick up sword'):
			self.event.append('Nothing to pick up. Sword is already in inventory.')
		else:
			self.event.append('Not Understood.')
		return render(request, 'game/index.html', story)

class OpenRoom(object):
	event = []
	location = 'Open Room'

class OpenRoomGet(OpenRoom, View):
	def get(self, request):
		del self.event[:]
		self.request.session['location'] = self.location
		self.event.append('You enter a large dark room. light is shining down from magical orbs on the ceiling')
		self.event.append('There is a door on the northern wall as well as the eastern wall.')
		self.event.append('The eastern door has a banner beside it.')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)

class OpenRoomPost(OpenRoom, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if 'Copper Key' not in request.session['inventory']:
			CopperKey = False
		else:
			CopperKey = True
		if (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			self.event.append('There is a door on the northern wall as well as the eastern wall. There is a banner near the eastern door.')
		elif (request.session['action'] == 'read banner') or (request.session['action'] == 'Read banner') or (request.session['action'] == 'look at banner') or (request.session['action'] == 'Look at banner') or (request.session['action'] == 'read the banner') or (request.session['action'] == 'Read the banner'):
			self.event.append('******** To reach the end you cannot rest. You must first pass this cunning test. Tread lightly to those that dare. Beyond this door lies the Sphinx Lair. *********')
		elif (request.session['action'] == 'open door') or (request.session['action'] == 'Open door') or (request.session['action'] == 'use door') or (request.session['action'] == 'Use door') or (request.session['action'] == 'door') or (request.session['action'] == 'Door'):
			self.event.append('Please specify which door.')
		elif (request.session['action'] == 'open east door') or (request.session['action'] == 'Open east door') or (request.session['action'] == 'use east door') or (request.session['action'] == 'Use east door') or (request.session['action'] == 'east door') or (request.session['action'] == 'East door') or (request.session['action'] == 'open eastern door') or (request.session['action'] == 'Open eastern door') or (request.session['action'] == 'use eastern door') or (request.session['action'] == 'Use eastern door') or (request.session['action'] == 'eastern door') or (request.session['action'] == 'Eastern door'):
			self.event.append('You push open the door on the eastern wall.')
			return redirect('sphinxLair')
		elif (CopperKey == False and request.session['action'] == 'open north door') or (CopperKey == False and request.session['action'] == 'Open north door') or (CopperKey == False and request.session['action'] == 'use north door') or (CopperKey == False and request.session['action'] == 'Use north door') or (CopperKey == False and request.session['action'] == 'north door') or (CopperKey == False and request.session['action'] == 'north Door') or (CopperKey == False and request.session['action'] == 'open northern door') or (CopperKey == False and request.session['action'] == 'Open northern door') or (CopperKey == False and request.session['action'] == 'use northern door') or (CopperKey == False and request.session['action'] == 'Use northern door') or (CopperKey == False and request.session['action'] == 'Northern door') or (CopperKey == False and request.session['action'] == 'northern Door'):
			self.event.append('There seems to be a copper lock on this door.')
		elif (CopperKey == True and request.session['action'] == 'open north door') or (CopperKey == True and request.session['action'] == 'Open north door') or (CopperKey == True and request.session['action'] == 'use north door') or (CopperKey == True and request.session['action'] == 'Use north door') or (CopperKey == True and request.session['action'] == 'north door') or (CopperKey == True and request.session['action'] == 'north Door') or (CopperKey == True and request.session['action'] == 'open northern door') or (CopperKey == True and request.session['action'] == 'Open northern door') or (CopperKey == True and request.session['action'] == 'use northern door') or (CopperKey == True and request.session['action'] == 'Use northern door') or (CopperKey == True and request.session['action'] == 'Northern door') or (CopperKey == True and request.session['action'] == 'northern Door') or (CopperKey == True and 'key' in request.session['action']) or (CopperKey == True and 'Key' in request.session['action']):
			self.event.append('Northern Door unlocks')
			return redirect('spaceRoom')
		else:
			self.event.append('Not Understood.')
		return render(request, 'game/index.html', story)

class SphinxLair(object):
	event = []
	location = 'Sphinx Lair'
	attempts = []
	sphinxPostprivateLog = []

class SphinxLairGet(SphinxLair, View):
	def get(self, request):
		self.request.session['location'] = self.location
		del self.event[:]
		del self.sphinxPostprivateLog[:]
		if ('Copper Key' in request.session['inventory']):
			self.event.append('You enter a small room')
			self.event.append('The Sphinx has gone to sleep. His purring is unnerving.')
			self.event.append('There is a door on the eastern wall with nothing in it.')
			self.event.append('There is also the door you walked through on the western wall.')
			self.sphinxPostprivateLog.append('Copper')
		else:
			self.event.append('You enter a small room.')
			self.event.append('There is a creature sitting in front of you, staring back.')
			self.event.append('This creature, standing on all fours is six feet tall with the head of a human and body of a lion.')
			self.event.append('There is a door behind him on the east wall as well as the one that you just walked through on the west wall.')
			self.event.append('* Behold, I am the Sphinx, he says. In order to pass me, you must first answer these riddles, three... *')
			self.event.append('You nod slowly in understanding.')
			self.event.append('* #1: I live in light but die when it shines upon me. What am I?')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)

class SphinxLairPost(SphinxLair, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if ('Copper' in self.sphinxPostprivateLog):
			if (request.session['action'] == 'look around') or (request.session['action'] == "look around"):
				self.event.append('The Sphinx is resting near an open door with nothing in it on the eastern wall.')
				self.event.append('The door behind you on the western wall seems to be your only option.')
			elif ('Copper Key' in request.session['inventory'] and 'west' in request.session['action']) or ('Copper Key' in request.session['inventory'] and 'West' in request.session['action']):
				self.event.append('You exit back towards the Open Room.')
				return redirect('openRoom')
			else:
				self.event.append('There is nothing for you to interact with in this room.')
				self.event.append('The door behind you on the western wall seems to be your only option.')
		else:
			if ('Shadow') not in self.sphinxPostprivateLog:
				questionOne = False
			else:
				questionOne = True
			if ('M') not in self.sphinxPostprivateLog:
				questionTwo = False
			else:
				questionTwo = True
			if ('Needle') not in self.sphinxPostprivateLog:
				questionThree = False
			else:
				questionThree = True
			if (questionThree != True and 'west' in request.session['action']) or questionThree != True and 'West' in request.session['action']:
				self.event.append('The Sphinx roars.')
				self.event.append('* You dare walk away from me? *')
				self.event.append('You begrudgingly stop and turn to face him again.')
			if (questionOne == False and 'shadow' in request.session['action']) or (questionOne == False and 'Shadow' in request.session['action']):
				self.event.append('* The Sphinx nods with a smile on his face. "Very good." *')
				self.event.append('* #2: What comes once in a minute, twice in a moment, but never in a thousand years? *')
				del self.attempts[:]
				self.sphinxPostprivateLog.append('Shadow')
			elif (questionOne == False and 'shadow' not in request.session['action'] and len(self.attempts) == 0) or (questionOne == False and 'Shadow' not in request.session['action'] and len(self.attempts) == 0):
				self.event.append('The sphinx stares back blankly. He is not amused by your incompetance.')
				self.attempts.append('attempt')
			elif (questionOne == False and 'shadow' not in request.session['action'] and len(self.attempts) == 1) or (questionOne == False and 'Shadow' not in request.session['action'] and len(self.attempts) == 1):
				self.event.append('Bored with your repeated foolishness, the Sphinx attacks.  You don\'t have a chance to defend as he rips your head off with his fangs.')
				del self.attempts[:]
				didDie.append('dead')
				return redirect('start')
				# enter DEAD event

			elif (questionOne == True and questionTwo == False and 'letter m' in request.session['action']) or (questionOne == True and questionTwo == False and 'letter M' in request.session['action']) or (questionOne == True and questionTwo == False and request.session['action'] == 'm') or (questionOne == True and questionTwo == False and request.session['action'] == 'M'):
				self.event.append('The Sphinx once again nods. He bares his lion teeth as he smiles toward you.')
				self.event.append('* #3: I have one eye but cannot see. What am I? *')
				self.sphinxPostprivateLog.append('M')

			elif (questionOne == True and questionTwo == False and ' m ' not in request.session['action'] and len(self.attempts) == 0) or (questionOne == True and questionTwo == False and ' M ' not in request.session['action'] and len(self.attempts) == 0):
				self.event.append('The sphinx stares back blankly. He is not amused by your incompetance.')
				self.attempts.append('attempt')
			elif (questionOne == True and questionTwo == False and ' m ' not in request.session['action'] and len(self.attempts) == 1) or (questionOne == True and questionTwo == False and ' M ' not in request.session['action'] and len(self.attempts) == 1):
				self.event.append('Bored with your repeated foolishness, the Sphinx attacks.  You don\'t have a chance to defend as he rips your head off with his fangs.')
				del self.attempts[:]
				didDie.append('dead')
				return redirect('start')
				# enter DEAD event

			elif (questionTwo == True and questionThree == False and 'needle' in request.session['action']) or (questionTwo == True and questionThree == False and 'Needle' in request.session['action']):
				self.event.append('The sphinx lets out a roar before stepping aside.')
				self.event.append('The door behind him opens revealing a Copper Key.')
				self.sphinxPostprivateLog.append('Needle')

			elif (questionTwo == True and questionThree == False and 'needle' not in request.session['action'] and len(self.attempts) == 0) or (questionTwo == True and questionThree == False and 'Needle' not in request.session['action'] and len(self.attempts) == 0):
				self.event.append('The Sphinx stares back blankly. He is not amused by your incompetance.')
				self.attempts.append('attempt')
			elif (questionTwo == True and questionThree == False and 'needle' not in request.session['action'] and len(self.attempts) == 1) or (questionTwo == True and questionThree == False and 'Needle' not in request.session['action'] and len(self.attempts) == 1):
				self.event.append('Bored with your repeated foolishness, the Sphinx attacks.  You don\'t have a chance to defend as he rips your head off with his fangs.')
				del self.attempts[:]
				didDie.append('dead')
				return redirect('start')
				# enter DEAD event

			elif (questionThree == True and request.session['action'] == 'pick up key') or (questionThree == True and request.session['action'] == 'Pick up key') or (questionThree == True and request.session['action'] == 'grab key') or (questionThree == True and request.session['action'] == 'Grab key') or (questionThree == True and request.session['action'] == 'take key') or (questionThree == True and request.session['action'] == 'Take key') or (questionThree == True and request.session['action'] == 'pick up copper key') or (questionThree == True and request.session['action'] == 'Pick up copper key') or (questionThree == True and request.session['action'] == 'grab copper key') or (questionThree == True and request.session['action'] == 'Grab copper key') or (questionThree == True and request.session['action'] == 'take copper key') or (questionThree == True and request.session['action'] == 'Take copper key'):
				if ('Copper Key' not in request.session['inventory']):
					self.event.append('Copper key added to inventory.')
					request.session['inventory'].append('Copper Key')
				else:
					self.event.append('Nothing to pick up.')
			elif ('Copper Key' in request.session['inventory'] and 'west' in request.session['action']) or ('Copper Key' in request.session['inventory'] and 'West' in request.session['action']):
				self.event.append('You exit back towards the Open Room.')
				return redirect('openRoom')
			else:
				self.event.append('Not understood.')
		return render(request, 'game/index.html', story)

class SpaceRoom(object):
	event = []
	location = 'Space Room'

class SpaceRoomGet(SpaceRoom, View):
	def get(self, request):
		del self.event[:]
		self.request.session['location'] = self.location
		self.event.append('As you enter you notice a window in front of you on the northern wall and a door on the western wall.')
		self.event.append('Peering out the window, you see a large blue and green orb slowly getting smaller in the distance.')
		self.event.append('Is that the Earth, you wonder.')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)


class SpaceRoomPost(SpaceRoom, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		if (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			self.event.append('There is a door on the western wall and a window on the northern wall')
			self.event.append('As you stare out the window, you begin to feel so small and alone.')
		elif (request.session['action'] == 'look out window') or (request.session['action'] == 'Look out window') or (request.session['action'] == 'look out the window') or (request.session['action'] == 'Look out the window') or (request.session['action'] == 'look outside') or (request.session['action'] == 'Look outside') or (request.session['action'] == 'use window') or (request.session['action'] == 'Use window'):
			self.event.append('The Earth shrinks in the distance. You wonder how you\'ll ever get the princess home...')
		elif (request.session['action'] == 'open west door') or (request.session['action'] == 'Open west door') or (request.session['action'] == 'use west door') or (request.session['action'] == 'Use west door') or (request.session['action'] == 'west door') or (request.session['action'] == 'West door') or (request.session['action'] == 'open western door') or (request.session['action'] == 'Open western door') or (request.session['action'] == 'use western door') or (request.session['action'] == 'Use western door') or (request.session['action'] == 'western door') or (request.session['action'] == 'Western door'):
			self.event.append('You walk into the next room...')
			return redirect('cypherRoom')
		else:
			self.event.append('Not understood.')
		return render(request, 'game/index.html', story)

class CypherRoom(object):
	event = []
	location = 'Cypher Room'
	attempts = []

class CypherRoomGet(CypherRoom, View):
	def get(self, request):
		del self.event[:]
		del self.attempts[:]
		self.request.session['location'] = self.location
		self.event.append('There is a door on the southern wall. In the middle of the room, on a pedastile 10 jewels with etchings on them')
		self.event.append('You inspect each of the jewels closely.')
		self.event.append('The jewels are arranged with the letters spelling P-O-S-E-N-M-A-S-E-E')
		self.event.append('Below the jewels there is an inscription')
		self.event.append('** You have shown cunning, this is true. Sadly, your life is nearly through. Lest you solve this anagram soon, the floor will open as you fall to your doom. **')
		self.event.append('** Tries, 3 you shall attempt, before your kinsmen are made to lament. **')
		self.event.append('Enter your guess:')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)

class CypherRoomPost(CypherRoom, View):
	def get(self, request):
		self.event.append('> ' + request.session["action"])
		guess = request.session['action'].upper()

		if (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			self.event.append('There is a pedastile in front of you with 10 jewels. You should not focus on anything else.')
		elif (guess == 'OPENSESAME') or (guess == 'OPEN SESAME'):
			self.event.append('The crystals begin to glow. Suddenly the door in front of you slides open.')
			self.event.append('You hear a sinister cackle on the other side.')
			self.event.append('Undeterred, you walk through the door...')
			return redirect('dragonsLair')
		elif (guess != 'OPENSESAME') or (guess != 'OPEN SESAME'):
			self.event.append('That is incorrect.')
			self.attempts.append('wrong')
			if (len(self.attempts)) == 3:
				self.event.append('The floor suddenly creaks open.')
				self.event.append('you are dropped into open space.')
				self.event.append('The breath is sucked from your lungs as your eyes bulge in their sockets.')
				self.event.append('Your body goes cold as your heart bursts in your chest.')
				didDie.append('dead')
				return redirect('start')
				# Death Event
		else:
			self.event.append('Not understood.')
		return render(request, 'game/index.html', story)

class DragonsLair(object):
	event = []
	location = 'Dragons Lair'
	timesAttacked = []
	directHit = []

class DragonsLairGet(DragonsLair, View):
	def get(self, request):
		del self.event[:]
		del self.timesAttacked[:]
		del self.directHit[:]
		self.request.session['location'] = self.location
		self.event.append('You enter a large dark room. with oddly high ceilings')
		self.event.append('Suddenly the room lights up as a huge fireball comes hurdling toward you.')
		self.event.append('You dive out of the way just in time.')
		self.event.append('The fireball burns in the center of the room as a loud cackle is heard in the distance')
		self.event.append('A large winged beast flies into the fireballs light and drops to the ground right in front of you.')
		self.event.append('** "Behold, I am Kur", he says **')
		self.event.append('"What have you done with the princess", you scream trying not to show your fear.')
		self.event.append('** "Such bravery for an Earthling", he says. "You see, magical creaturessss are not from your world. We come from a planet far away and have been stranded on your world for some time. We needed your gold to power our enginessss." **')
		self.event.append('Not quite understanding the beasts ramblings, you yell once more. "Where is the princess?!"')
		self.event.append('He lets out yet another cackle.')
		self.event.append('** I was going to take her as a tassssty treat but when I heard you were aboard I decided it would be best to eat you both togetherrrrr. **')
		self.event.append('Just then you notice in the corner of the room on the southern wall the princess is chained and gagged. She stares back at you in horror.')
		self.event.append('* You must specify if you want to attack Kur\'s various body parts. (Head, chest, arms, legs) *')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)


class DragonsLairPost(DragonsLair, View):
	def get(self, request):
		if (len(self.timesAttacked) < 3):
			vulnerable = False
		else:
			vulnerable = True
		if (len(self.directHit) < 2):
			killed = False
		else:
			killed = True
		# if (vulnerable == True):
			# self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
		self.event.append('> ' + request.session["action"])
		attack = request.session['action'].upper()
		if (request.session['action'] == 'look around' and killed == False) or (request.session['action'] == 'Look around' and killed == False):
			self.event.append('The dragon stares down at you in the center of the room. You see the princess chained to the wall in the corner. You cannot make out if there is anything else around. It is too dark.')
		elif (request.session['action'] == 'look around' and killed == True) or (request.session['action'] == 'Look around' and killed == True):
			self.event.append('Kur lies dead in the center of the large room. The fire in his gut illuminates a lone door on the northern side of the room.')
		elif ('princess' in request.session['action']):
			self.event.append('There is no time to deal with the princess. Kur is ready to attack.')
		elif ('head' in request.session['action'] and vulnerable == False) or ('Head' in request.session['action'] and vulnerable == False):
			self.event.append('Your sword merely scrapes against his scales causing no damage.')
			self.timesAttacked.append('attacked')
			if (len(self.timesAttacked) == 3):
				self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
		elif ('arm' in request.session['action'] and vulnerable == False) or ('Arm' in request.session['action'] and vulnerable == False) or ('arms' in request.session['action'] and vulnerable == False) or ('Arms' in request.session['action'] and vulnerable == False):
			self.event.append('Your sword merely scrapes against his scales causing no damage.')
			self.timesAttacked.append('attacked')
			if (len(self.timesAttacked) == 3):
				self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
		elif ('leg' in request.session['action'] and vulnerable == False) or ('Leg' in request.session['action'] and vulnerable == False) or ('legs' in request.session['action'] and vulnerable == False) or ('Legs' in request.session['action'] and vulnerable == False):
			self.event.append('Your sword merely scrapes against his scales causing no damage.')
			self.timesAttacked.append('attacked')
			if (len(self.timesAttacked) == 3):
				self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
		elif ('chest' in request.session['action'] and vulnerable == False) or ('Chest' in request.session['action'] and vulnerable == False):
			self.event.append('Kur anticipates your attack and covers his chest with his arms.')
			self.timesAttacked.append('attacked')
			if (len(self.timesAttacked) == 3):
				self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
# vulverable actions
		elif ('head' in request.session['action'] and vulnerable == True and killed == False) or ('Head' in request.session['action'] and vulnerable == True and killed == False):
			self.event.append('As you run towards his head for the attack he releases a giant fire ball. Your world is lit aflame as your skin starts to boil...')
			didDie.append('dead')
			return redirect('start')
			# Death Event
		elif ('arm' in request.session['action'] and vulnerable == True and killed == False) or ('Arm' in request.session['action'] and vulnerable == True and killed == False) or ('arms' in request.session['action'] and vulnerable == True and killed == False) or ('Arms' in request.session['action'] and vulnerable == True and killed == False):
			self.event.append('Kur swipes his arm toward you, knocking you to the ground as he releases his fireball...')
			didDie.append('dead')
			return redirect('start')
			# Death Event
		elif ('leg' in request.session['action'] and vulnerable == True and killed == False) or ('Leg' in request.session['action'] and vulnerable == True and killed == False) or ('legs' in request.session['action'] and vulnerable == True and killed == False) or ('Legs' in request.session['action'] and vulnerable == True and killed == False):
			self.event.append('Kur anticipates this attacks and stomps on you. Everything goes black...')
			didDie.append('dead')
			return redirect('start')
			# Death Event
		elif ('chest' in request.session['action'] and vulnerable == True and len(self.directHit) == 0 and killed == False) or ('Chest' in request.session['action'] and vulnerable == True and len(self.directHit) == 0 and killed == False):
			self.event.append('You slash Kur\'s newly undefended chest. He haphazardly releases his fireball in the wrong direction as he stumbles backward. He is hurt.')
			self.directHit.append('hit')
			del self.timesAttacked[:]
		elif ('chest' in request.session['action'] and vulnerable == True and len(self.directHit) == 1 and killed == False) or ('Chest' in request.session['action'] and vulnerable == True and len(self.directHit) == 1 and killed == False):
			self.event.append('You slash Kur\'s newly undefended chest. He haphazardly releases his fireball in the wrong direction as he stumbles backward. He is hurt.')
			self.directHit.append('hit')
			self.event.append('Kur falls to the ground as blood spurts from his chest!')
			self.event.append('You watch as his pupils slowly shink into nothingness.')
			self.event.append('Suddenly you remember...')
			self.event.append('"The Princess!", you exclaim.')
			self.event.append('You run over and break her chains with your sword.')
			self.event.append('BOOMMM!')
			self.event.append('There is a loud pop behind you as Kur\'s chest burns open, illuminating the room.')
			self.event.append('You notice a door on the northern wall that was covered by the darkness before.')
		elif (killed == True and request.session['action'] == 'open north door') or (killed == True and request.session['action'] == 'Open north door') or (killed == True and request.session['action'] == 'use north door') or (killed == True and request.session['action'] == 'Use north door') or (killed == True and request.session['action'] == 'north door') or (killed == True and request.session['action'] == 'north Door') or (killed == True and request.session['action'] == 'open northern door') or (killed == True and request.session['action'] == 'Open northern door') or (killed == True and request.session['action'] == 'use northern door') or (killed == True and request.session['action'] == 'Use northern door') or (killed == True and request.session['action'] == 'Northern door') or (killed == True and request.session['action'] == 'northern Door'):
			self.event.append('You grab the princess\'s arm and drag her toward the door...')
			return redirect('cockpit')
		else:
			self.event.append('Not understood.')
		return render(request, 'game/index.html', story)

class Cockpit(object):
	event = []
	location = 'Cockpit'

class CockpitGet(Cockpit, View):
	def get(self, request):
		del self.event[:]
		self.request.session['location'] = self.location
		self.event.append('You enter a room with a large window pointing towards the darkness outside')
		self.event.append('There is an abandoned consol with buttons and levers.')
		self.event.append('You sit in the throne at the front.')
		self.event.append('This monstrosity you have battled through seems to be moving at its own will. It is as though it is being piloted automatically toward some unknown land')
		self.event.append('You and the princess sit perplexed as the metal castle barrels through space.')
		self.event.append('You prepare yourself, knowing that this adventure has only just begun...')
		self.event.append('** THE END **')
		request.session['summary'] = {
				'location' : self.location,
				'event' : self.event,
			}
		log.append(request.session['summary'])
		return render(request, 'game/index.html', story)



