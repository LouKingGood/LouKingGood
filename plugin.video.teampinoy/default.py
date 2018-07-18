import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon
import urlresolver
from addon.common.addon import Addon
import requests
import base64
s = requests.session() 
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.teampinoy'
BASEURL = base64.b64decode(b'aHR0cDovL3d3dy5waW5veW1vdmllcGVkaWEuc3U=')
BASEURL1 = base64.b64decode(b'aHR0cDovL3d3dy5sYW1iaW5nYW4uc3U=')
BASEURL2 = base64.b64decode(b'aHR0cDovL3dhdGNocGlub3ltb3ZpZXNvbmxpbmUuaW5mby8=')
BASEURL3 = base64.b64decode(b'aHR0cDovL3d3dy5rYXB1c28uYmUv')
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ADDON      = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
ICON = ADDON.getAddonInfo('icon')
FANART = ADDON.getAddonInfo('fanart')
PATH = 'Team Pinoy'
VERSION = ADDON.getAddonInfo('version')
ART = ADDON_PATH + "/resources/icons/"

def MENU():
    xbmcgui.Dialog().ok("[B][COLOR dodgerblue]TeamPinoy Pilipinas[/COLOR][/B]","Thank you for using TeamPinoy Pilipinas. Any questions or inquiries please feel free to contact us @ support@teampinoy.ml...Enjoy Watching")
    addDir('[B][COLOR dodgerblue]Pinoy[/COLOR][COLOR yellow] Teleserye[/COLOR][/B]','url',2,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    addDir('[B][COLOR dodgerblue]Pinoy[/COLOR][COLOR yellow] Movies[/COLOR][/B]','url',3,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    addDir('[B][COLOR dodgerblue]Hollywood[/COLOR][COLOR yellow] Movies[/COLOR][/B]','url',8,ART + 'teampinoy.png',FANART,'')
    addDir('[B][COLOR dodgerblue]Asian[/COLOR][COLOR yellow] Movies[/COLOR][/B]',BASEURL+'/category/asian-movies/',5,ART + 'teampinoy.png',FANART,'')
    addDir('[B][COLOR dodgerblue]Tagalog[/COLOR][COLOR yellow] Dubbed[/COLOR][/B]',BASEURL2+'category/tagalog-dubbed/',20,ART + 'teampinoy.png',FANART,'')
    setView('tvshows', 'tvshows-view')
    
def teampinoy_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile("<a class='thumbx' href='(.+?)' title='(.+?)'.+?src='(.+?)'/></a>",re.DOTALL).findall(OPEN)
    for url,name,icon in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&amp;#038;','&')
        icon = icon.replace('s72-c/','')
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,icon,FANART,'')
    np = re.compile("<a class='blog-pager-older-link' href='(.+?)'",re.DOTALL).findall(OPEN)
    for url in np:
        if 'kapuso' in url:
            icon = ART + 'nextpage.jpg'
        if 'pacitalaflakes' in url:
            icon = ART + 'nextpage.jpg'
        addDir('[B][COLOR red]Older Posts>>>[/COLOR][/B]',url,5,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def BayanihanTV_links(name,url):
    OPEN = Open_Url(url)
    Regex = re.compile('<[iI][fF][rR][aA][mM][eE] [sS][rR][cC]="(.+?)"',re.DOTALL).findall(OPEN)
    for url in Regex:
        try:
            name2 = url.split('//')[1].replace('www.','')
            name2 = name2.split('/')[0].split('.')[0].title()
        except:pass
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,11,iconimage,FANART,name)
    altlinks = re.compile('DM.player.+?"player(.+?)".+?video: "(.+?)"',re.DOTALL).findall(OPEN)
    for name2,url in altlinks:
        addDir('[B][COLOR white]Part %s[/COLOR][/B]' %name2,'http://www.dailymotion.com/embed/video/%s'%url,11,iconimage,FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')

def bangonPinoy_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile("<a class='thumbx' href='(.+?)' title='(.+?)'.+?src='(.+?)'/></a>",re.DOTALL).findall(OPEN)
    for url,name,icon in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&amp;#038;','&')
        icon = icon.replace('s72-c/','')
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,7,icon,FANART,'')
    np = re.compile("<a class='blog-pager-older-link' href='(.+?)'",re.DOTALL).findall(OPEN)
    for url in np:
        if 'kapuso' in url:
            icon = ART + 'nextpagekap.jpg'
        if 'pacitalaflakes' in url:
            icon = ART + 'nextpagetamb.jpg'
        addDir('[B][COLOR red]Older Posts>>>[/COLOR][/B]',url,6,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def bangonPinoy_links(name,url):
    OPEN = Open_Url(url)
    Regex = re.compile('<[iI][fF][rR][aA][mM][eE] [sS][rR][cC]="(.+?)"',re.DOTALL).findall(OPEN)
    for url in Regex:
        try:
            name2 = url.split('//')[1].replace('www.','')
            name2 = name2.split('/')[0].split('.')[0].title()
        except:pass
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,11,iconimage,FANART,name)
    altlinks = re.compile('DM.player.+?"player(.+?)".+?video: "(.+?)"',re.DOTALL).findall(OPEN)
    for name2,url in altlinks:
        addDir('[B][COLOR white]Part %s[/COLOR][/B]' %name2,'http://www.dailymotion.com/embed/video/%s'%url,11,iconimage,FANART,name)
	
def bayanihanTV():
    addDir('[B][COLOR dodgerblue]Latest Pinoy Shows[/COLOR][/B]','http://www.lambingan.su/',30,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    addDir('[B][COLOR dodgerblue]ABS-SERVER-1[/COLOR][/B]',BASEURL1+'/category/abs-cbn/',30,ART + 'teampinoy.png',ART + 'fanart2.jpg','') 
    addDir('[B][COLOR dodgerblue]ABS-SERVER-2[/COLOR][/B]','http://pacitalaflakes.blogspot.com/search/label/ABS-CBN?m=0',6,ART + 'teampinoy.png',FANART,'')
    addDir('[B][COLOR dodgerblue]GMA SERVER-1[/COLOR][/B]',BASEURL3 + 'search/label/GMA?&max-results=24',6,ART + 'teampinoy.png',FANART,'')
    addDir('[B][COLOR dodgerblue]GMA-SERVER-2[/COLOR][/B]',BASEURL1+'/category/Gma7/',30,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    addDir('[B][COLOR dodgerblue]Search TV Shows[/COLOR][/B]','url',22,ART + 'search.jpg',FANART,'')
    setView('tvshows', 'tvshows-view') 
	
def bangonPinoy():
    addDir('[B][COLOR dodgerblue]SERVER-1[/COLOR][/B]',BASEURL+'/category/tagalog-movies/',5,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    addDir('[B][COLOR dodgerblue]SERVER-2[/COLOR][/B]',BASEURL2+'category/latest/',20,ART + 'teampinoy.png',FANART,'')
    addDir('[B][COLOR dodgerblue]SERVER-3[/COLOR][/B]',BASEURL2+'category/pinoy-classic-movies/',20,ART + 'teampinoy.png',FANART,'')
    addDir('[B][COLOR dodgerblue]Search Movies[/COLOR][/B]','url',24,ART + 'search.jpg',FANART,'')
    setView('tvshows', 'tvshows-view')
	
def bangonpinoyonlinemenu():
    
    addDir('[B][COLOR white]HOLLYWOOD MOVIES[/COLOR][/B]','url',8,ART + 'hmov.jpg',FANART,'')	
    setView('tvshows', 'tvshows-view')
	
def Mov_Menu(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div id="content" role="main">(.+?)<!-- end #content -->',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<a class="clip-link".+?href="(.+?)".+?<img src="(.+?)" alt="(.+?)"',re.DOTALL).findall(str(Regex))
    for url,icon,name in Regex2:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#039;','\'').replace('&#038;','&').replace('&#8230;','...')
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,11,icon,ART + 'fanart2.jpg','')
    np = re.compile('rel="next".+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR red]Next Page>>>[/COLOR][/B]',url,20,ART + 'n_p.png',ART + 'fanart2.jpg','')
    setView('tvshows', 'default-view') 
	
def bayani_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('class="post-thumbnail".+?img src="(.+?)".+?href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        if 'http' not in icon:
            icon = 'http:' + icon
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,35,icon,FANART,'')
    np = re.compile('class="current".+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR red]Next Page>>>[/COLOR][/B]',url,30,ART + 'nextpage.png',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)') 

def bayani_vids(name,url):
    OPEN = Open_Url(url)
    Regex = re.compile('<iframe frameborder="0".+?src="(.+?)"',re.DOTALL).findall(OPEN)
    for url in Regex:
        if 'http:' not in url:
            url = 'http:' + url
        if '/dm-' in url:
            name2 = 'Main Link [COLOR blue](Dailymotion)[/COLOR]'
        elif '/mo-'in url:
            name2 = 'Main Link [COLOR cyan](Openload)[/COLOR]'
        elif '/all-'in url:
            name2 = 'Main Link [COLOR yellow](Estream)[/COLOR]'
        else:
            name2= 'Short Clip'
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,40,iconimage,FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)') 

def bayani_res(url):
    if 'watchnew.asia' in url:
        OPEN = Open_Url(url)
        try:
            url = re.compile('<[iI][fF][rR][aA][mM][eE].+?[sS][rR][cC]="(.+?)"',re.DOTALL).findall(OPEN)[0]
            if 'http:' not in url:
                url = 'http:' + url
                stream_url = urlresolver.resolve(url)
            else:
                stream_url = urlresolver.resolve(url)
        except:
            url = re.compile('<div class=.+?container.+?href="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
    elif 'libangan' in url:
        Holder = Open_Url(url)
        if 'www.dailymotion.com' in Holder:
            url = re.compile('<iframe.+?src="(.+?)"',re.DOTALL).findall(Holder)[0]
            url = 'http:' + url
        else:
            url = re.compile('<div class=.+?container.+?href="(.+?)"',re.DOTALL).findall(Holder)[0]
        stream_url = urlresolver.resolve(url)
    else:
        stream_url = urlresolver.resolve(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)	
    
def teampinoy_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<li class="border-radius.+?src="(.+?)".+?href="(.+?)" title="(.+?)">',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&')
        icon = icon.replace('-210x142','').replace('-199x142','')
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,23,icon,ART + 'fanart2.jpg','')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR red]Next Page >>>[/COLOR][/B]',url,5,ART + 'nextpage.jpg',ART + 'fanart2.jpg','')
    xbmc.executebuiltin('Container.SetViewMode(50)')    

def bayanihan_TV(url):
    OPEN = Open_Url(url)
    Regex = re.compile('tag menu-item.+?href="(.+?)">(.+?)</a>',re.DOTALL).findall(OPEN)
    for url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&')
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,81,ART + 'pedia_shows.jpg',ART + 'fanart2.jpg','')
    xbmc.executebuiltin('Container.SetViewMode(50)') 
    
def bayanihan_links(name,url):
    OPEN = Open_Url(url)
    Regex = re.compile('data-lazy-src="(.+?)"',re.DOTALL).findall(OPEN)
    for url in Regex:
        url = url.replace('https://href.li/?','')
        if urlresolver.HostedMediaFile(url).valid_url():
            try:
                name2 = url.split('//')[1].replace('www.','')
                name2 = name2.split('/')[0].split('.')[0].title()
            except:pass
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,11,iconimage,ART + 'fanart2.jpg',name)
    altlinks = re.compile('<iframe.+?src="(.+?)"',re.DOTALL).findall(OPEN)
    for url in altlinks:
        if 'dailymotion' in altlinks:
            url = 'http:' + url
        if urlresolver.HostedMediaFile(url).valid_url():    
            try:
                name2 = url.split('//')[1].replace('www.','')
                name2 = name2.split('/')[0].split('.')[0].title()
            except:pass
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,11,iconimage,ART + 'fanart2.jpg',name)
    xbmc.executebuiltin('Container.SetViewMode(50)')
	
def bangonmoviechannel():
    addDir('[B][COLOR white]SERVER-1[/COLOR][/B]',BASEURL+'/category/hollywood-movies/',5,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    addDir('[B][COLOR white]SERVER-2[/COLOR][/B]',BASEURL+'/category/bluray/',5,ART + 'teampinoy.png',ART + 'fanart2.jpg','')
    setView('tvshows', 'tvshows-view')

def bayanihan_Search():
    keyb = xbmc.Keyboard('', 'Search')
    keyb.doModal()
    if (keyb.isConfirmed()):
            search = keyb.getText().replace(' ','+')
            url = BASEURL1 + '/?s=' + search
            bayani_content(url)
			
def teampinoy_Search():
    keyb = xbmc.Keyboard('', 'Search')
    keyb.doModal()
    if (keyb.isConfirmed()):
            search = keyb.getText().replace(' ','+')
            url = BASEURL + '/?s=' + search
            teampinoy_content(url)
    


def RESOLVE(url):
   
    try:
        if 'speedvid.net' in url:
            OPEN = Open_Url(url)
            link = re.compile('primary\|8777\|.+?primary\|(.+?)\|(.+?)\|.+?image\|mp4\|(.+?)\|',re.DOTALL).findall(OPEN)
            for port,server,hash in link:
                url = 'http://'+ server +'.speedvid.net:'+port+'/'+hash+'/v.mp4'
            stream_url=url
        elif 'watchpinoymoviesonline.info' in url:
            OPEN = Open_Url(url)
            url = re.compile('<iframe src="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
        else:
            stream_url = urlresolver.resolve(url)
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR cornflowerblue]Sorry[/COLOR],[COLOR red]Link Unavailable[/COLOR] ,3000)") 

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

def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link

    
    
def addDir(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
	liz.setProperty('fanart_image', fanart)
	if mode==11 or mode==40:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
    
params=get_params()
url=None
name=None
mode=None
iconimage=None
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
	description=urllib.unquote_plus(params["description"])
except:
	pass

if mode==None or url==None or len(url)<1 : MENU()

elif mode == 2 : bayanihanTV()
elif mode == 3 : bangonPinoy()
elif mode == 4 : bangonpinoyonlinemenu()
elif mode == 5 : teampinoy_content(url) 
elif mode == 6 : bangonPinoy_content(url)
elif mode == 7 : bangonPinoy_links(name,url)
elif mode == 8 : bangonmoviechannel()
elif mode == 10 : BayanihanTV_links(name,url)
elif mode == 11	: RESOLVE(url)
elif mode == 20 : Mov_Menu(url)
elif mode == 22 : bayanihan_Search()
elif mode == 24 : teampinoy_Search()
elif mode == 23 : bayanihan_links(name,url)
elif mode == 30 : bayani_content(url)
elif mode == 35 : bayani_vids(name,url)
elif mode == 40 : bayani_res(url)
elif mode == 81 : bayanihan_content(url)
elif mode == 91 : bayanihan_TV(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))

















