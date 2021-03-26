import os 

REFRESH_LOGO = os.path.abspath(os.path.join(os.path.dirname(__file__), 'glue_refresh.png'))

def setup():
    from .StatsDataViewer import StatsDataViewer
    from glue.config import qt_client
    qt_client.add(StatsDataViewer)
