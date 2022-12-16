#
#
#

from unittest import TestCase

from octodns_namedfileyaml import NamedFileYamlProvider


class TestNamedFileYamlProvider(TestCase):

    # TODO: test provider
    def test_nothing(self):
        self.assertTrue(True)
        provider = NamedFileYamlProvider('waitwhat', 'test', 'test')
        provider.get_filenames('test')
