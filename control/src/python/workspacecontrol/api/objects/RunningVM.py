import zope.interface
import workspacecontrol.api

class RunningVM(workspacecontrol.api.WCObject):
    """RunningVM is what the Platform module's info command returns, given
    a handle (that must be supplied externally).
    """
    
    handle = zope.interface.Attribute(
    """handle ...
    """)
    
    state = zope.interface.Attribute(
    """state ...
    """)
    
    # TODO: many other fields are coming
    