from zope.formlib import form
from zope.interface import implements
from zope.component import adapts
import zope.lifecycleevent
from zope.component import getMultiAdapter

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from plone.app.form import base as ploneformbase

from medialog.easysliderviewlet.interfaces import IEasysliderviewletSettings 
from medialog.easysliderviewlet import easysliderviewletMessageFactory as _
from medialog.easysliderviewlet.settings import EasysliderviewletSettings
  

class EasysliderviewletSettingsForm(ploneformbase.EditForm):
    """
    The page that holds all the settings
    """
    form_fields = form.FormFields(IEasysliderviewletSettings)
      
    label = _(u'heading_easysliderviewlet_settings_form', default=u"Easysliderviewlet Settings")
    description = _(u'description_easysliderviewlet_settings_form', default=u"Configure the parameters for this file.")
    form_name = _(u'title_easysliderviewlet_settings_form', default=u"Easysliderviewlet settings")
    
    