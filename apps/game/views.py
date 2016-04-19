from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
# Declare Global variables
log = []
inventory = []
story = {
		'log' : log,
		'inventory' : inventory
	}
actions = 0
# event = []
# location = []
startPostprivateLog = ['dummy']
firstScroll = '******** Your Princess now belongs in my castle... Bring 2000 gold pieces to the castle North of the mountains for her return *********'
startBanner = '******** Welcome to Medieval Space Adventure. MSA is a game of adventure, peril and cunning. You are about to embark on a journey, the likes of which few have ever imagined. In MSA the courageous adventurer discovers the secrets of his worlds mythical creatures origins. He is cast into a series of puzzles, only the most cunning are to survive. MSA was developed by Kerrin Arora during a rainy week in Houston, TX. It was inspired by the 1980s game, ZORK. MSA was written in Python using the Django Framework. For any comments, feel free to email me at kerrin.arora@gmail.com! *********'

def postDirector(request):
	request.session['action'] = request.POST['action']
	if request.session['location'] == 'Palace Chambers':
		return redirect('startPost')
	elif request.session['location'] == 'North of Mountains':
		return redirect('mountainsPost')
	else:
		return redirect('start')

def start(request):
	event = []
	location = 'Palace Chambers'
	request.session['location'] = location
	event.append('It is a beautiful day in the Kingdom.')
	event.append('The princess sits on her throne ready to lead.')
	event.append('There is a banner on the wall.')
	event.append('BRAKOOMMMMMMMMM')
	event.append('You hear a large crash up above as a winged behemoth swoops down and grabs up the princess.')
	event.append('As it flies off it drops a scroll...')
	def startPost(request):
		event.append('> ' + request.session["action"])
		if ('pick up scroll' or 'Pick up scroll') not in startPostprivateLog:
			scroll = False
		else:
			scroll = True

		if ('read scroll' or 'Read scroll') not in startPostprivateLog[-1]:
			scrollRead = False
		else:
			scrollRead = True
		
		if (request.session['action'] == 'pick up scroll' and scroll == True) or (request.session['action'] == 'Pick up scroll' and scroll == True):
			event.append('Nothing to pick up.')
		elif (request.session['action'] == 'pick up scroll' and scroll == False) or (request.session['action'] == 'Pick up scroll' and scroll == False):
			event.append('Picked up scroll.')
			scroll = True
			inventory.append('scroll')
		elif (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
			event.append('There is a scroll on the ground and a banner on the wall. Also the palace just got a new sun roof.')
		elif (request.session['action'] == 'pick up banner') or (request.session['action'] == 'Pick up banner'):
			event.append('You cannot pick up the banner. It is attached to the wall.')
		elif (request.session['action'] == 'read banner') or (request.session['action'] == 'Read banner'):
			event.append(startBanner)
		elif (scroll == False and request.session['action'] == 'read scroll') or (scroll == False and request.session['action'] == 'Read scroll'):
			event.append('You must first pick up scroll')
		elif (scroll == True and request.session['action'] == 'read scroll') or (scroll == True and request.session['action'] == 'Read scroll'):
			event.append(firstScroll)
			scrollRead = True
			event.append('Would you like to save the Princess? Y/N')
		elif scrollRead == True:
			if (request.session['action'] == 'Y') or (request.session['action'] == 'y') or (request.session['action'] == 'yes') or (request.session['action'] == 'Yes'):
				return redirect('mountains')
			else:
				scrollRead = False
		else:
			event.append('Not Understood.')
		startPostprivateLog.append(request.session["action"])
		return render(request, 'game/index.html', story)
	summary = {
			'location' : location,
			'event' : event,
		}
	log.append(summary)
	return render(request, 'game/index.html', story)

# def startPost(request):
# 	event.append('> ' + request.session["action"])
# 	if ('pick up scroll' or 'Pick up scroll') not in startPostprivateLog:
# 		scroll = False
# 	else:
# 		scroll = True

# 	if ('read scroll' or 'Read scroll') not in startPostprivateLog[-1]:
# 		scrollRead = False
# 	else:
# 		scrollRead = True
	
# 	if (request.session['action'] == 'pick up scroll' and scroll == True) or (request.session['action'] == 'Pick up scroll' and scroll == True):
# 		event.append('Nothing to pick up.')
# 	elif (request.session['action'] == 'pick up scroll' and scroll == False) or (request.session['action'] == 'Pick up scroll' and scroll == False):
# 		event.append('Picked up scroll.')
# 		scroll = True
# 		inventory.append('scroll')
# 	elif (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
# 		event.append('There is a scroll on the ground and a banner on the wall. Also the palace just got a new sun roof.')
# 	elif (request.session['action'] == 'pick up banner') or (request.session['action'] == 'Pick up banner'):
# 		event.append('You cannot pick up the banner. It is attached to the wall.')
# 	elif (request.session['action'] == 'read banner') or (request.session['action'] == 'Read banner'):
# 		event.append(startBanner)
# 	elif (scroll == False and request.session['action'] == 'read scroll') or (scroll == False and request.session['action'] == 'Read scroll'):
# 		event.append('You must first pick up scroll')
# 	elif (scroll == True and request.session['action'] == 'read scroll') or (scroll == True and request.session['action'] == 'Read scroll'):
# 		event.append(firstScroll)
# 		scrollRead = True
# 		event.append('Would you like to save the Princess? Y/N')
# 	elif scrollRead == True:
# 		if (request.session['action'] == 'Y') or (request.session['action'] == 'y') or (request.session['action'] == 'yes') or (request.session['action'] == 'Yes'):
# 			return redirect('mountains')
# 		else:
# 			scrollRead = False
# 	else:
# 		event.append('Not Understood.')
# 	startPostprivateLog.append(request.session["action"])
# 	return render(request, 'game/index.html', story)

def mountains(request):
	location.append('North of Mountains')
	return render(request, 'game/index.html', story)

def mountainsPost(request):
	return render(request, 'game/index.html', story)



