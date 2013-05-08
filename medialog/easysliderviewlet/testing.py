from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class MedialogEasysliderviewlet(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import medialog.easysliderviewlet
        xmlconfig.file('configure.zcml',
                       medialog.easysliderviewlet,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.easysliderviewlet:default')

MEDIALOG_EASYSLIDERVIEWLET_FIXTURE = Medialoggeasysliderviewlet()
MEDIALOG_EASYSLIDERVIEWLET_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MEDIALOG_EASYSLIDERVIEWLET_FIXTURE, ),
                       name="MedialogEasysliderviewlet:Integration")