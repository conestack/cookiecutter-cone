from node.tests import NodeTestCase
from {{cookiecutter.project_package}}.tests.layers import {{cookiecutter.project_package.split(".")[-1].capitalize()}}Layer


class TestMain(NodeTestCase):
    layer =  {{cookiecutter.project_package.split(".")[-1].capitalize()}}Layer()


    def test_main(self):
        ...