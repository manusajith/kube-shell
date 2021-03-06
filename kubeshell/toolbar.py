from __future__ import print_function, absolute_import, unicode_literals
from pygments.token import Token
from pygments.token import Keyword, Name, Operator, Generic, Literal, Text

class Toolbar(object):
    """Show information about the aws-shell in a tool bar.
    :type handler: callable
    :param handler: Wraps the callable `get_toolbar_items`.
    """

    def __init__(self, get_cluster_name, get_namespace, get_user, get_inline_help):
        self.handler = self._create_toolbar_handler(get_cluster_name, get_namespace, get_user, get_inline_help)

    def _create_toolbar_handler(self, get_cluster_name, get_namespace, get_user, get_inline_help):
        def get_toolbar_items():
            if get_inline_help():
                help_token = 'class:bottom-toolbar.on'
                help = "ON"
            else:
                help_token = 'class:bottom-toolbar.off'
                help = "OFF"

            return [
                ('class:prompt', 'Cluster: '),
                ('class:bottom-toolbar', get_cluster_name()),
                ('class:state', ' Namespace: '),
                ('class:bottom-toolbar', get_namespace()),
                ('class:path', ' User: '),
                ('class:bottom-toolbar', get_user())
            ]

        return get_toolbar_items
