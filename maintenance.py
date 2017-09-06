import xbmc,xbmcaddon
ADDON = xbmcaddon.Addon()
id = ADDON.getAddonInfo('id')
version = ADDON.getAddonInfo('version')
xbmc.log("%s %s" % (id,version))