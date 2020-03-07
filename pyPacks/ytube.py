import urllib.request
import urllib.parse
import re
#import pafy
#import vlc
import webbrowser		#for running the obtained url in default web_browser

class ytube():
	def __init__(self,wrd):
		self.wrd=wrd
	def srch_to_url(self):
		st_f01=self.wrd.replace('play','')     #st_f01 first filter
		query_string = urllib.parse.urlencode({"search_query" : st_f01})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
		print("http://www.youtube.com/watch?v=" + search_results[0])
		final_url= "http://www.youtube.com/watch?v=" + search_results[0]  #url obtained
		print("playing")
		#working with vlc player to play the video		
		#vl=vlc.Instance()
		#pl=vl.media_player_new()
		#player= vl.media_new(final_url)
		#player.get_mrl()
		#pl.set_media(player)
		#pl.play()
		webbrowser.open(final_url)
