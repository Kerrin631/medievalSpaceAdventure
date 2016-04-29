# import unittest
from django.test import Client
from django.test import TestCase

from pprint import pprint as pp

class SimpleTest(TestCase):
    def test_newgame(self):
        client = Client()
        response = client.get('/newGame/')
        # print response
        self.assertEqual(response.status_code, 302)

        response = client.get('/')
        print "GET /","=" * 20
        # print response
        print "context=",response.context
        print "=" * 20

        # http://54.191.235.170/postDirector/ = 302
        # form data:
        # csrfmiddlewaretoken:EYkGYGMztPhIXDOPjNrcsSOBLC0SZ1mK
        # action:read scroll

        response = client.post('/postDirector/', {'action': 'read scroll'})
        print "POST /postDirector/","=" * 20
        print "response=",response
        print "context=",response.context
        print "=" * 20
        self.assertEqual(response.status_code, 302)

    # def test_coldroom(self):
    #     client = Client()
    #     response = client.get('/coldRoom/')
    #     # print response
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "<p>You awaken in a prison cell.</p>")

    # def test_index(self):
    #     client = Client()
    #     response = client.get('/customer/index/')
    #     self.assertEqual(response.status_code, 200)
