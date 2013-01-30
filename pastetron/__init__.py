"""
Pastetron - A pastebin application.
"""

import pastetron.views
import pastetron.utils


__version__ = '0.1.0'
__author__ = 'Keith Gaughan'
__email__ = 'k@stereochro.me'


def paste(global_config, **settings):
    """
    PasteDeploy runner.
    """
    app = pastetron.utils.initialise(pastetron.views, global_config, settings)
    return app.wsgifunc()
