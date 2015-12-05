import sys
import urlparse
import yt
import time
import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import base64
import urlresolver
from bs4 import BeautifulSoup
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from resources import streams,lists,utube,TV,Standup,Films,premierleague
from resources.lib.parsers import TVParser
from datetime import datetime

Decode = base64.decodestring
BASE2= lists.BASE2
BASE3= lists.BASE3
BASE4= lists.BASE4
BASE5= lists.BASE5
BASE6= lists.BASE6
BASE7= lists.BASE7
CAT=lists.CAT
BASE = lists.BASE
addon_id='plugin.video.originentertainment'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()
ADDON = xbmcaddon.Addon(id=addon_id)
GetAdultPassword = ADDON.getSetting('Password')
AdultURL = Decode('aHR0cDovL2JhY2syYmFzaWNzLngxMGhvc3QuY29tL0FkdWx0L2luZGV4LnBocD9tb2RlPVh4WCZwYXNzd29yZD0=')
AdultFinalURL = AdultURL + GetAdultPassword

Article_Cache = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id + 'Article_Dump.txt'))


addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addon_id)
if not os.path.exists(addon_data_dir):
        os.makedirs(addon_data_dir)

tmpListFile = os.path.join(addon_data_dir, 'tempList.txt')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def Home_Menu():

    addList('24/7 Shows',BASE+'24-7'+CAT,400,ART + '24shows.png')
    addDir('Sports','',64,ART + 'sports.png',ART + 'background.png','')
    addDir('Lists','',53,ART + 'lists.png',ART + 'background.png','')
    addDir('Live TV','',41,ART + 'livetv.png',ART + 'background.png','')
    addDir('M3U8 Lists','',54,ART + 'm3u8.png',ART + 'background.png','')
    addDir('Movies','',10,ART + 'movies.png',ART + 'background.png','')
    addDir('News','',72,ART + 'icon.png',ART + 'background.png','')
    addDir('Pandoras Box','',55,ART + 'pandorasbox.png',ART + 'background.png','')
    addDir('Radio','',63,ART + 'radio.png',ART + 'background.png','')	
    addDir('Stand Up','',12,ART + 'comedy.png',ART + 'background.png','') 
    addDir('Test Area','',52,ART + 'testarea.png',ART + 'background.png','')
    addDir('TV Guide','',71,ART + 'tvguide.png',ART + 'background.png','')		
    addDir('TV Shows','',11,ART + 'tv.png',ART + 'background.png','')	
#    addDir('Search','',13,ART + 'search.png',ART + 'background.png','')
    addList('World Cams',BASE+'worldcams'+CAT,400,ART + 'worldcams.png')
    if GetAdultPassword == Decode('Zm9yZGZpZXN0YQ=='):
        addList('Adult Movies',AdultFinalURL,400,ART + 'icon.png')
	
	
def Sports():

    addDir('Football','',57,ART + 'icon.png',ART + 'background.png','')

    
    xbmcplugin.endOfDirectory(addon_handle)

def Radiocountry():

    html=OPEN_URL(Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw=='))
    match = re.compile('<tr>.+?<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(html)
    for url,name in match:
			    addList((name).replace('email me','').replace('External services',''),Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1LyVz')%url,62,ART + 'icon.png')

	
def Radio(url):

    html=OPEN_URL(url)
    match = re.compile('<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">',re.DOTALL).findall(html)
    for name,url in match:
		addDir4(name,url,401,ART + 'icon.png')


def Football():
	addList('Fixtures','',58,ART + 'icon.png')
	addDir4('Premier League Table','',75,ART+'icon.png')
	

	
def Pandoras_Box():

    html=OPEN_URL(Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA=='))
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,url,img,fanart,mode in match:
			    addList(name,url,mode,ART + 'icon.png')
				
def open_Menu(url):

    html=OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,url,img,fanart,mode in match:
			    addList(name,url,mode,ART + 'icon.png')
	
	
    
def M3u8Lists():

    addList('List 1','',411,ART + 'icon.png')
    addList('List 2','',413,ART + 'icon.png')
    addList('List 3','',414,ART + 'icon.png')
    addList('List 4','',415,ART + 'icon.png')
    addList('List 5','',416,ART + 'icon.png')
#    addDir('Multi Lists',Decode('aHR0cDovL2ljaGkxMzQubmV0MTYubmV0L0lQVFYv'),418,ART + 'icon.png',ART + 'background.png','')

def Test():

    addList('Test Area',BASE+'test'+CAT,400,ART + 'icon.png')
    addList('Sponge Test',BASE5+'badlands'+CAT,400,ART + 'icon.png')
#    addList('Dizilab Scraper Test','',410,ART + 'icon.png')
	

    xbmcplugin.endOfDirectory(addon_handle)
    
    
 
    
def addDir(name,url,mode,iconimage,fanart,description): 
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return ok
        
def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
'''       
def Parsem3uURL(url): 
    response = urlOpener.open(url).read()
        
    try:
        Titles = re.findall(r'<a .*?>(.*?)</a>',response)
        Links = re.findall(('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S),response)
'''

def M3UCATS():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u1.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')

def M3UCATS2():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u2.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
       addDir4(name,url,401,ART+'icon.png')

def M3UCATS3():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u3.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')

def M3UCATS4():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u4.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')

def M3UCATS5():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u5.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')
        
#elif mode == 58 	: FootballFixturesDay()
#elif mode == 59 	: FootballFixturesGame()
#elif mode == 60 	: FootballFixturesChannel()

def FootballFixturesDay():
    html=OPEN_URL('http://liveonsat.com/quickindex.html')
    match = re.compile('<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"',re.DOTALL).findall(html)
    for url,img,name in match:
        addDir3((name).replace('amp;',''),'http://liveonsat.com/%s'%url,59,'http://liveonsat.com/%s'%img)
		
def FootballFixturesGame(url):
    html=OPEN_URL(url)	
    match = re.compile('time_head>(.+?)</h2>.+?comp_head>(.+?)</span>.+?<div class = fLeft width = "250"><img src="(.+?)"></div>.+?ST: (.+?)</div>',re.DOTALL).findall(html)
    for date,comp,img,time in match:
		addDir3(date + ' - ' + comp + ' - ' + time,'',65,'http://liveonsat.com' + img)

		
def Guidemenu():

#    addDir('Interactive','',65,ART + 'tvguide.png',ART + 'background.png','')		
    addDir('Basic','',65,ART + 'tvguide.png',ART + 'background.png','')		
    addDir('Full','',70,ART + 'tvguide.png',ART + 'background.png','')		



def whatsoncat():
    html=OPEN_URL('http://tvguideuk.telegraph.co.uk/')
    match = re.compile('<li class="tabs"><span><a href="(.+?)">(.+?)</a></span></li>').findall(html)
    for url,name in match:
        if 'amp;' in url:
	    url = url.replace ('amp;','')
        addDir3(name,'http://tvguideuk.telegraph.co.uk/' + url,65,'')
		
        

def whatson(url):
    #url = 'http://tvguideuk.telegraph.co.uk/grid.php?&day=2015-12-04&oclock=&tab=0e0a6394b2f90a3e6c4783fa1a895ffd&tabname=Radio&region='
    html=OPEN_URL(url)
    match = re.compile('<div class="channel_name">(.+?)<.+?channel_id=(.+?).+?>(.+?)</a>',re.DOTALL).findall(html)
    for name,id,whatson in match:
        addDir3(name + ' - ' + whatson,'',41,'')

def TESTMOVIE():
    html=OPEN_URL('')
    match = re.compile('<td><a href="(.+?)"><img src="(.+?)" width="100" height="100" border="0"><br>(.+?)</a></td>').findall(html)
    for url,img,name in match:
        addDir3(name,'',420,ART+'icon.png')

def Movie2(url):
    html=OPEN_URL(url)
    match = re.compile('',re.DOTALL).findall(html)
    for url,name,img in match:
        addDir3(name,url,421,'http://www.movietubenow.biz%s'%img)

def Movie3(url):
    html=OPEN_URL(url)
    match = re.compile('<iframe width="680" height="430" scrolling="no" frameborder="0" src="(.+?)"',re.DOTALL).findall(html)
    for url in match:
        addDir3(name,url,422,ART + 'icon.png')

def Movie4(url):
    html=OPEN_URL(url)
    match = re.compile('<source src="(.+?)" type="video/mp4"/>').findall(html)
    for url in match:
        addDir3(name,url,401,'')


def TESTCATS():
    html=OPEN_URL('http://www.animetoon.org/cartoon')
    match = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(html)
    for url,name in match:
        addDir3(name,url,407,ART+'icon.png')

def NewsCat():
    html=OPEN_URL('http://www.mirror.co.uk/')
    match = re.compile('<a href="(.+?)" data-type="section-head_.+?" data-action="section:.+?">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3((name).replace('amp;',''),url,73,ART+'icon.png')
        

def NewsStory(url):
    html=OPEN_URL(url)
    match = re.compile('<figure>.+?<img src="(.+?)" class="aboveHeadline .+?<a href="(.+?)".+?&#xa;(.+?)</a>',re.DOTALL).findall(html)
    for img,url,name in match:
        addDir4((name).replace('amp;','').replace('&#x3a','').replace('&#xa; </a>','').replace('&#xa;','').replace('&quot;','').replace('&#x27;',''),url,74,img)
        print '>>>>>>>>>>' + url        

		
def LISTS(url):
    html=OPEN_URL(url)
    match = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,url,408,ART+'icon.png')
        
def LISTS2(url):
    html=OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url in match:
        addDir3(name,url,409,ART+'icon.png')
        
def LISTS3(url):
    html=OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        addDir4('STREAM',url,401,ART+'icon.png')

        
        
def addVID(type,name,url,mode,iconimage = '',fanart = '',video = '',description = ''):
    if type != 'folder2' and type != 'addon':
        if len(iconimage) > 0:
            iconimage = ART + iconimage
        else:
            iconimage = 'DefaultFolder.png'
    if type == 'addon':
        if len(iconimage) > 0:
            iconimage = iconimage
        else:
            iconimage = 'http://totalxbmc.tv/addons/cache/images/4c79319887e240789ca125f144d989_addon-dummy.png'
    if fanart == '':
        fanart = FANART
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&video="+urllib.quote_plus(video)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    liz.setProperty( "Build.Video", video )
    if (type=='folder') or (type=='folder2') or (type=='tutorial_folder') or (type=='news_folder'):
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    else:
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def Add_Directory_Item(handle, url, listitem, isFolder):

    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 

def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def Live(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addList3('%s'%(name).replace('Origin Entertainment','Origin Entertainment').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),401,'%s'%(iconimage))

def Live2(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addList2(name,url,402,iconimage)


def addMenu(url):
    
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
    menulocation=('%s%s'%(BASE,url))
    link = OPEN_URL(url)
    match=re.compile("addDir('','','','','','')").findall(link)

    
                
def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('LOADING','Opening %s Now'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve()
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
             return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()

def addSearch():
    searchStr = ''
    keyboard = xbmc.Keyboard(searchStr, 'Search')
    keyboard.doModal()
    if (keyboard.isConfirmed()==False):
      return
    searchStr=keyboard.getText()
    if len(searchStr) == 0:
      return
    else:
      return searchStr
        
def TestPlayUrl(name, url, iconimage=None):
    print '--- Playing "{0}". {1}'.format(name, url)
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
        
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
      
def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addList2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addList3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


def News_Article(name, url):
    req = OPEN_URL(url)
    soup = BeautifulSoup(req)
    Dump_Article = open(Article_Cache,'w')
    Heading = name

    Article_Body = soup.find_all('div', {'class': 'body'})
    for Article in Article_Body:
        Article_Paragraph = Article.find_all('p')
        for Paragraph in Article_Paragraph:
            Paragraph = Paragraph.text
            Paragraph = Paragraph.encode('utf-8')

            Write_Paragraph = open(Article_Cache,'a')
            Write_Paragraph.write(Paragraph)
            Write_Paragraph.write('\n')

        Get_Article = open(Article_Cache,'r')
        Read_Article = Get_Article.read()
        Text_Boxes(Heading,Read_Article)
        Write_Paragraph.close()



def Text_Boxes(heading,anounce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(anounce); text=f.read()
      except: text=anounce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()

        

		
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
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

def resolve2(url):
    try:
        url = url.replace('/embed-', '/')
        url = re.compile('//.+?/([\w]+)').findall(url)[0]
        page = 'http://allmyvideos.net/%s' % url

        result = client.request(page, close=False)

        post = {}
        f = client.parseDOM(result, 'form', attrs = {'action': ''})
        k = client.parseDOM(f, 'input', ret='name', attrs = {'type': 'hidden'})
        for i in k: post.update({i: client.parseDOM(f, 'input', ret='value', attrs = {'name': i})[0]})
        post = urllib.urlencode(post)

        result = client.request(page, post=post)

        url = re.compile('"file" *: *"(http.+?)"').findall(result)[-1]
        url += '&direct=false&ua=false'
        return url
    except:
        return




if mode == None     : Home_Menu()
elif mode == 9      : yt.PlayVideo(url)
elif mode == 10     : Films.Films()
elif mode == 11     : TV.TV_Shows()
elif mode == 12     : Standup.Stand_Up()
elif mode == 13     : addSearch()
elif mode == 14     : TV.Animated_TV()
elif mode == 15     : TV.Action_TV()
elif mode == 16     : TV.Childrens_TV()
elif mode == 17     : TV.Comedy_TV()
elif mode == 18     : TV.Drama_TV()
elif mode == 19     : TV.Entertainment_TV()
elif mode == 20     : TV.Fantasy_TV()
elif mode == 21     : TV.Music_TV()
elif mode == 22     : TV.Scifi_TV()
elif mode == 23     : TV.Soap_TV()
elif mode == 24     : Standup.Jeff_Dunham()
elif mode == 25     : TV.DrWho()
elif mode == 26     : TV.Arrow()
elif mode == 27     : TV.Flash()
elif mode == 28     : utube.Mock_the_week()
elif mode == 29     : utube.Inbetweeners()
elif mode == 30     : utube.WouldILieToYou()
elif mode == 31     : TV.Flash_Series2()
elif mode == 32     : TV.The_Last_Man_On_Earth()
elif mode == 33     : TV.Fargo()
elif mode == 34     : TV.The_Knick()
elif mode == 35     : TV.Gotham()
elif mode == 36     : TV.Sons_Of_Anarchy()
elif mode == 37     : TV.Homelands()
elif mode == 38     : TV.Daredevil()
elif mode == 39     : TV.New_girl()
elif mode == 40     : TV.Dexter()
elif mode == 41     : TV.Live_TV()
elif mode == 42     : TV.Breaking_bad()
elif mode == 43     : TV.Grimm()
elif mode == 44     : TV.Brooklyn_Nine_Nine()
elif mode == 45     : TV.Game_of_thrones()
elif mode == 46     : TV.Bates_motel()
elif mode == 47     : TV.Black_list()
elif mode == 48     : TV.Legends()
elif mode == 49     : TV.Suits()
elif mode == 50     : TV.Once_upon_a_time()
elif mode == 51     : TV.How_I_Met_Your_Mother()
elif mode == 52     : Test()
elif mode == 53     : lists.Lists()
elif mode == 54     : M3u8Lists()
elif mode == 55     : Pandoras_Box()
elif mode == 56 	: TESTMOVIE()
elif mode == 57 	: Football()
elif mode == 58 	: FootballFixturesDay()
elif mode == 59 	: FootballFixturesGame(url)
elif mode == 60 	: FootballFixturesChannel()
elif mode == 61 	: Sponge_TV()
elif mode == 62 	: Radio(url)
elif mode == 63 	: Radiocountry()
elif mode == 64 	: Sports()
elif mode == 65 	: whatson(url)
elif mode == 66 	: TV.WorldNews()
elif mode == 67 	: TV.WorldPlayUrl(url)
elif mode == 68 	: TV.WorldPlayVid(url)
elif mode == 69 	: Guidemenu()
elif mode == 70		: whatsonsky()
elif mode == 71 	: whatsoncat()
elif mode == 72 	: NewsCat()
elif mode == 73 	: NewsStory(url)
elif mode == 74 	: News_Article(name, url)
elif mode == 75 	: premierleague.Premier_League_Table()
elif mode == 401    : Resolve(url)
elif mode == 400    : Live(url)
elif mode == 402    : streams.ParseURL(url)
elif mode == 403    : Live2(url)
elif mode == 404    : TestPlayUrl(name, url, iconimage)
elif mode == 405    : lists.TESTCATS2()
elif mode == 406    : TESTCATS()
elif mode == 407    : LISTS(url)
elif mode == 408    : LISTS2(url)
elif mode == 409    : LISTS3(url)
elif mode == 410    : lists.TestDizi()
elif mode == 411    : M3UCATS()
elif mode == 412    : M3UPLAY(url)
elif mode == 413    : M3UCATS2()
elif mode == 414    : M3UCATS3()
elif mode == 415    : M3UCATS4()
elif mode == 416    : M3UCATS5()
elif mode == 417    : Parsem3uURL(url)
elif mode == 418    : TVParser.GetLinks(url)
elif mode == 419 	: TVParser.m3uCategory(url)
elif mode == 420 	: Movie2(url)
elif mode == 421 	: Movie3(url)
elif mode == 422 	: Movie4(url)
elif mode == 423 	: open_Menu(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
