from collective.grok import gs
from eappi.policy import MessageFactory as _

@gs.importstep(
    name=u'eappi.policy', 
    title=_('eappi.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eappi.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
