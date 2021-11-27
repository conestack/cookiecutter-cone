import json
import os
import shutil
import sys
import tempfile
import unittest
from cone.app.testing import Security

class {{cookiecutter.project_package.split(".")[-1].capitalize()}}Layer(Security):

    def make_app(self):
        ...

    def setUp(self, args=None):
        ...

    def tearDown(self):
        ...

    