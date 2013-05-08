from Acquisition import aq_inner
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements, Interface
from zope.component import getMultiAdapter

from medialog.easysliderviewlet import easysliderviewletMessageFactory as _
from medialog.easysliderviewlet.settings import EasysliderviewletSettings
from medialog.easysliderviewlet.settings import IEasysliderviewletSettings

#dont know if this is needed
#from Products.Five import BrowserView
#from Products.CMFCore.utils import getToolByName


class EasysliderViewlet(ViewletBase):
    render = ViewPageTemplateFile('easysliderviewlet.pt')
    
    implements(IEasysliderviewletSettings)
    
    @property
    @memoize
    def easysliderpath(self):
		context=self.context
		self.settings = EasysliderviewletSettings(context)
		
		try:
			portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
			portal = portal_state.portal()
			path = str(self.settings.easysliderpath)
			if path.startswith('/'):
				path = path[1:]
				
			return portal.restrictedTraverse(path, default=False)
		except:
			return False
			