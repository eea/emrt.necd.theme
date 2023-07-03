# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import emrt.necd.theme


class EmrtNecdThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=emrt.necd.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'emrt.necd.theme:default')


EMRT_NECD_THEME_FIXTURE = EmrtNecdThemeLayer()


EMRT_NECD_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EMRT_NECD_THEME_FIXTURE,),
    name='EmrtNecdThemeLayer:IntegrationTesting',
)


EMRT_NECD_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EMRT_NECD_THEME_FIXTURE,),
    name='EmrtNecdThemeLayer:FunctionalTesting',
)


EMRT_NECD_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EMRT_NECD_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EmrtNecdThemeLayer:AcceptanceTesting',
)
