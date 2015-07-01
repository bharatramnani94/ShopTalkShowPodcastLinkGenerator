import urllib2
import re

start = 0
end = 171
audioLinks = []

htmlBefore = "<body>"
htmlAfter = "</body>"
linkBefore = "<a href="
linkAfter = "</a>"

counter = start
while counter <= end:
	try:
		currentUrl = 'http://shoptalkshow.com/episodes/' + format(counter, '03d') + '/';
		response = urllib2.urlopen(currentUrl)
		html = response.read()

		currentAudioLink = re.search(r'source src="(http://audio\.simplecast\.fm/\d{1,5}\.mp3)', html)
		currentAudioLink = currentAudioLink.group(1)

		currentHtmlLink = linkBefore + currentAudioLink + ">Audio " + str(counter) + linkAfter

		audioLinks.append(currentHtmlLink)
		print 'Done', format(counter, '03d')

		response.close()

	except:
		print 'Error with Audio ', format(counter, '03d')

	counter += 1

myFile = open("ShopTalkShowAudioLinks.html", 'w')
myFile.write(htmlBefore + '\n'.join(audioLinks) + htmlAfter)
