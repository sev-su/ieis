# coding=utf-8
from django.test import TransactionTestCase
from django.core.urlresolvers import reverse
from django.test.client import Client as DjangoClient


class TestFrontPage(TransactionTestCase):

    """ Testing an index view """

    reset_sequences = True

    def setUp(self):
        self.dj_client = DjangoClient()

    def test_home_page_go_to(self):
        # get request of home page
        response = self.dj_client.get(reverse('home'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_index_page_go_to(self):
        # get request of index page
        response = self.dj_client.get(reverse('index'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
