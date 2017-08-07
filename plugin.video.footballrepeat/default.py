'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import sys
import urlparse
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_Pand = (Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8='))
addon_id='plugin.video.footballrepeat'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Football Repeat"
VERSION = "1.0.1"
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))



def Home_Menu():
    addDirFolder('Highlights','',3,ART + 'icon.png',FANART,'')
    addDirFolder('Fixtures','',4,ART + 'icon.png',FANART,'')

def FootballFixturesDay():
    html=OPEN_URL(Decode('http://liveonsat.com/quickindex.html'))
    match = re.compile('<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"',re.DOTALL).findall(html)
    for url,img,name in match:
        addDirFolder((name).replace('amp;',''),Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + url,5,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + img,FANART,'')
		
def FootballFixturesGame(url):
    HTML = OPEN_URL(url)
    block = re.compile('AndClearL.+?><h2.+?head>(.*?)float',re.DOTALL).findall(HTML)
    for block in block:
        day = re.compile('(.*?)</h2>').findall(str(block))
        for Day in day:
            Day = Day
        game = re.compile('comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->',re.DOTALL).findall(str(block))
        for comp,img,time,chan in game:
            channel = re.compile(",CAPTION, '(.+?)&nbsp").findall(chan)
            addDirFolder(Day + ' - ' + comp + ' - ' + time,'',5,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20=') + img,FANART,(str(channel)))

    setView('tvshows', 'Media Info 3')

def Football_Highlights():

    addDirFolder('Latest','http://www.fullmatchesandshows.com',1,'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png',ART + 'fanart.jpg','')
    addDirFolder('EURO 2016','http://www.fullmatchesandshows.com/euro-2016/',1,'http://football.mywapblog.com/files/uefa-euro-2016-logo.png',ART + 'fanart.jpg','')
    addDirFolder('Shows','http://www.fullmatchesandshows.com/category/show/',1,'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png',ART + 'fanart.jpg','')
    addDirFolder('Premier League','http://www.fullmatchesandshows.com/premier-league/',1,'https://footballseasons.files.wordpress.com/2013/05/premier-league.png',ART + 'fanart.jpg','')
    addDirFolder('La Liga','http://www.fullmatchesandshows.com/la-liga/',1,'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png',ART + 'fanart.jpg','')
    addDirFolder('Bundesliga','http://www.fullmatchesandshows.com/bundesliga/',1,'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg',ART + 'fanart.jpg','')
    addDirFolder('Champions League','http://www.fullmatchesandshows.com/champions-league/',1,'http://www.ecursuri.ro/images/teste/test-champions-league.jpg',ART + 'fanart.jpg','')
    addDirFolder('Serie A','http://www.fullmatchesandshows.com/category/serie-a/',1,'http://files.jcriccione.it/200000223-2484526782/serie%20a.png',ART + 'fanart.jpg','')
    addDirFolder('Ligue 1','http://www.fullmatchesandshows.com/category/ligue-1/',1,'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg',ART + 'fanart.jpg','')
    addDirFolder('Copa America 2015','http://www.fullmatchesandshows.com/copa-america-2015/',1,'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png',ART + 'fanart.jpg','')
    addDirFolder('CONCACAF','http://www.fullmatchesandshows.com/category/concacaf/',1,'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png',ART + 'fanart.jpg','')
    addDirFolder('Women World Cup','http://www.fullmatchesandshows.com/category/women-world-cup/',1,'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png',ART + 'fanart.jpg','' )


		
def get_All_Rows(url):
    HTML = OPEN_URL(url)
    match = re.compile('class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>',re.DOTALL).findall(HTML)
    for img,url,name in match:
        Name = name.replace('&#8211;', '-').replace('&#038;', '&')
        addDir(Name,url,2,img,'','')

def get_PLAYlink(url):
    HTML = OPEN_URL(url)
    match = re.compile('<script data-config="(.+?)" data-height').findall(HTML)
    for playlink in match:
        Playlink = (playlink).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
        Resolve('http:'+Playlink)

	

def addDir(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirFolder(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

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

def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass

def OPEN_URL(url):
        req = urllib2.Request(url)
        IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
        FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
        IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
        ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)


if mode == None     : Home_Menu()
elif mode == 1 		: get_All_Rows(url)
elif mode == 2 		: get_PLAYlink(url)
elif mode == 3 		: Football_Highlights()
elif mode == 4 		: FootballFixturesDay()
elif mode == 5 		: FootballFixturesGame(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
