from zope.interface import implements, alsoProvides, noLongerProvides
from Products.Five.browser import BrowserView
from medialog.easysliderviewlet.interfaces import IEasysliderviewletUtilProtected, \
    IEasysliderviewletUtil, IEasysliderviewlet
from Products.CMFCore.utils import getToolByName

from plone.app.customerize import registration
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.component import getMultiAdapter

try:
    #For Zope 2.10.4
    from zope.annotation.interfaces import IAnnotations
except ImportError:
    #For Zope 2.9
    from zope.app.annotation.interfaces import IAnnotations


class EasysliderviewletUtilProtected(BrowserView):
    """
    a protected traverable utility for 
    enabling and disabling easysliderviewlet
    """
    implements(IEasysliderviewletUtilProtected)
    def enable(self):
        utils = getToolByName(self.context, 'plone_utils')

        if not IEasysliderviewlet.providedBy(self.context):
            alsoProvides(self.context, IEasysliderviewlet)
            self.context.reindexObject(idxs=['object_provides'])
            utils.addPortalMessage("Easysliderviewlet added.")
            self.request.response.redirect(self.context.absolute_url())
            
        else:  
            self.request.response.redirect(self.context.absolute_url())
        
    def disable(self):
        utils = getToolByName(self.context, 'plone_utils')
        
        if IEasysliderviewlet.providedBy(self.context):
            noLongerProvides(self.context, IEasysliderviewlet)
            self.context.reindexObject(idxs=['object_provides'])
            
            #now delete the annotation
            annotations = IAnnotations(self.context)
            metadata = annotations.get('medialog.easysliderviewlet', None)
            if metadata is not None:
                del annotations['medialog.easysliderviewlet']
                
            utils.addPortalMessage("Easysliderviewlet removed.")
            
        self.request.response.redirect(self.context.absolute_url())
        
class EasysliderviewletUtil(BrowserView):
    """
    a public traverable utility that checks if it is enabled etc
    more work to do here
    """
    implements(IEasysliderviewletUtil)

    def enabled(self):
        return IEasysliderviewlet.providedBy(self.context)    


    def view_enabled(self):
        utils = getToolByName(self.context, 'plone_utils')
        return True

    def should_include(self):
        return self.enabled() or self.view_enabled()
        
    
