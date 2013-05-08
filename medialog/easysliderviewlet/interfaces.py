from zope.interface import Interface, Attribute
from zope import schema
from medialog.easysliderviewlet import easysliderviewletMessageFactory  as _


 
class IEasysliderviewletLayer(Interface):
    """
    marker interface for easysliderviewlet layer
    
    """
    
class IEasysliderviewlet(Interface):
    """
    marker interface for content types that can use the viewlet 
    """

    
class IEasysliderviewletUtilProtected(Interface):

    def enable():
        """
        enable easysliderviewlet on this object
        """

    def disable():
        """
        disable easysliderviewlet on this object
        """


class IEasysliderviewletUtil(Interface):

    def enabled():
        """
        checks if easysliderviewlet is enabled  
        """

    def view_enabled():
        """
        checks if the easysliderviewlet is selected
        """

class IEasysliderviewletSettings(Interface):
    """
    The actual easysliderviewlet settings
    """
     
    easysliderpath = schema.TextLine(
        title=_(u"label_width_title_easysliderviewlet_setting", default=u"Which Easyslider"),
        description=_(u"label_width_description_easysliderviewlet_setting", 
        default=u"The path to the easyslider you want to  show."),
        default=u'my/path',
        required=True)

    def __call__(self, context):
        self.context = context
    
    
    def __init__(self, context):
        self.context = context
        
        