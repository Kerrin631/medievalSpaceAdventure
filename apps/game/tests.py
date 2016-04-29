# import unittest
from django.test import Client
from django.test import TestCase
# from pprint import pprint as pp


class SimpleTest(TestCase):
    def print_response(self, response , display=False):
        #print "request=", response.request
        print response.request['REQUEST_METHOD'], response.request['PATH_INFO'],response.status_code
        if display:
            print "-" * 40
            print "response=", response
            print "-" * 40
        else:
            print "len=", len(response.content)

    def test_newgame(self):
        client = Client()

        response = client.get('/newGame/')
        self.print_response(response)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        response = client.get('/')
        self.print_response(response)
        print "context=", response.context

        # http://54.191.235.170/postDirector/ = 302
        # form data: csrfmiddlewaretoken:EYkGYGMztPhIXDOPjNrcsSOBLC0SZ1mK
        # action:read scroll

        response = client.post('/postDirector/', {'action': 'pick up scroll'})
        self.print_response(response)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')
        #expected_url, status_code=302, target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

        response = client.get('/startPost/')
        self.print_response(response, display=False)
        print "context=", response.context

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
