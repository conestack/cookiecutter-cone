{%- if cookiecutter.browser=="y" %}
from cone.app import main_hook, Configurator
from collections import OrderedDict
from typing import Dict
from pyramid.session import SignedCookieSessionFactory

from cone.something import browser


def register_session_factory(config: Configurator):
    sf = SignedCookieSessionFactory("wm-secret")
    config.set_session_factory(sf)


@main_hook
def init_app(config: Configurator, global_config: OrderedDict, settings: Dict[str, str]):
    register_session_factory(config)

    config.scan(browser)
    
{% endif %}