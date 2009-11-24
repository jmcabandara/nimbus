import zope.interface
import workspacecontrol.api

class Parameters(workspacecontrol.api.WCObject):
    """Parameters is the systemwide mechanism for propagating commandline and
    conf file settings to wcmodules.
    
    It maintains a two level hierarchy for the wcmodule author.  Key/values are
    stored by source: command line or conf file.
    
    Conf files require there to be a specified section qualifier before the key
    is used.  Only the values from the configured conf file will be included,
    not the union of all sections across all conf files related to wcmodules.
    
    See "etc/workspace-control/main.conf" which is where the wcmodule
    implementations and conf files are configured.
    """
  
    def get_cmdline_or_none(key):
        """Get string value of a commandline parameter if it existed.
        All values are stripped of extraneous spaces (string.strip()).
        Return None if it did not exist.  Empty string is impossible.
        """
    
    def get_conf_or_none(section, key):
        """Get string value of a configuration setting if it existed.
        All values are stripped of extraneous spaces (string.strip()).
        Return None if it did not exist.  Empty string is impossible, there
        is not distinguishing between "key not present" in the conf file vs.
        "key present with empty value," both cause None to be returned.
        """
