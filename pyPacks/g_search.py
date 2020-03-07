from googlesearch import search
import webbrowser			#for running the obtained url in default web_browser
class g_search():
	def __init__(self,s):
		self.s=s
	def g_url(self):
		lst=["search","read","provide update on","tell me the","update me with","find me","tell me about","update about","show me","provide","who is the","which is the","what is "]
		for i in lst:
			if i in self.s:
				t=self.s.replace(i,'')
		#if "search" in self.s:
		#	t=self.s.replace('search','')
		#elif "read" in self.s:
		#	t=self.s.replace('read','')
		#elif "update" in self.s:
		#	t=self.s.replace("update",'')
		#elif "provide" in self.s:
		#	t=self.s.replace("provide",'')
		#elif "find me" in self.s:
		#	t=self.s.replace("find me",'')
		
		print (t)
		j= list(search(t, tld="com", num=1, start=0, stop=1, pause=3))	#tld:top-level domain, num:no.of results, start: start link index , stop= number of results, pause: time lapse for result fetching 
		print (j[0])
		webbrowser.open(j[0])
