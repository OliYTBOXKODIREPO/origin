import process,re,sys,urllib,yt

def Youtube_Grab_Playlist_Page(url):
    HTML = process.OPEN_URL(url)
    block = re.compile('<ul class="yt-lockup-meta-info">(.+?)<div class="yt-lockup-meta">',re.DOTALL).findall(HTML)
    for item in block:
        name = re.compile('dir="ltr" title="(.+?)"').findall(str(item))
        for name in name:
            name = (name).replace('	','').replace('&#39;','\'')
        url = re.compile('<a href="(.+?)" class="yt-pl-thumb-link yt-uix-sessionlink').findall(str(item))
        for url in url:
            url = 'https://www.youtube.com'+url
        image = re.compile('data-thumb="(.+?)"').findall(str(item))
        for image in image:
            image = image
        process.Menu(str(name),str(url),10001,str(image),'','','')   


 

def Youtube_Playlist_Grab(url):
    HTML = process.OPEN_URL(url)
    block = re.compile('<li class="yt-uix-scroller-scroll-unit.+?"(.+?)</li>',re.DOTALL).findall(HTML)
    for block in block:
        name = re.compile('data-video-title="(.+?)"').findall(str(block))
        for name in name:
            name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        url = re.compile('<a href="/w(.+?)&').findall(str(block))
        for url in url:
            url = (url).replace('atch?v=','')
        image = re.compile('src="(.+?)" >').findall(str(block))
        for image in image:
            image = image
        if 'elete' in name:
            pass
        elif 'rivate' in name:
            pass
        else:
            process.Play(name,url,10003,str(image),'','','')

	
def Youtube_Playlist_Grab_Duration(url):
   
    #Need to view the playlist to use this one (as a list on page) max 100 vids
    HTML = process.OPEN_URL(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
            if 'elete' in name:
                pass
            elif 'rivate Vid' in name:
                pass
            else:
    			name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)"').findall(str(block))
        for url in url:
            url = url
        process.Play('[COLORred]'+str(duration)+'[/COLOR] : '+str(name),str(url),10003,str(image),'','','' )
	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
	

if mode   == 10000: Youtube_Grab_Playlist_Page(url)
elif mode == 10001: Youtube_Playlist_Grab(url)
elif mode == 10002: Youtube_Playlist_Grab_Duration(url)
elif mode == 10003: yt.PlayVideo(url)