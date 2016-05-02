# import unittest
from django.test import Client
from django.test import TestCase
#from django.core.urlresolvers import resolve
from pprint import pprint as pp


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def print_response(self, response, display=False):
        print " "
        print response.request['REQUEST_METHOD'], response.request['PATH_INFO'], response.status_code
        if display:
            print "-" * 40
            print "response=", response
            print "-" * 40
        else:
            print "len=", len(response.content)

    def test_refactoring_support(self):
        print "=" * 80
        response = self.client.get('/newGame/',follow=True)
        self.print_response(response)
        print "redirect=", response.redirect_chain
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')
        print "/newGame/ context=", response.context

        print "postDirector", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'pick up scroll'}, follow=True)
        self.print_response(response,display=False)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')
        print "inventory=", response.context['inventory']
        self.assertTrue("Scroll" in response.context['inventory'])
        self.assertContains(response,"<li><b>Palace Chambers</b></li>",count=1)
        self.assertContains(response,"Picked up scroll.",count=1)

        print "postDirector2", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'read scroll'}, follow=True)
        self.print_response(response,display=True)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')
        #print "inventory=", response.context['inventory']
        # self.assertTrue("Scroll" in response.context['inventory'])
        # self.assertContains(response,"<li><b>Palace Chambers</b></li>",count=1)
        # self.assertContains(response,"Picked up scroll.",count=1)
        print "ascroll=", response.context['ascroll']

        response = self.client.get('/mountains/')
        self.assertEqual(response.status_code, 200)
        self.print_response(response,display=True)
        print "/mountains/ context=", response.context
        return
        
        return
        #  Continue testing


        response = self.client.get('/mountainsPost/')
        self.assertEqual(response.status_code, 200)
        self.print_response(response)
        print "/mountainsPost/ context=", response.context

        response = self.client.get('/coldRoom/')
        self.assertEqual(response.status_code, 200)
        self.print_response(response)
        print "/coldRoom/ context=", response.context


        #response = self.client.get('/coldRoomPost/', {'action': 'pick up scroll'}, follow=False)
        response = self.client.get('/coldRoomPost/', follow=False)
        self.assertEqual(response.status_code, 200)
        self.print_response(response, display=True)
        print "/coldRoomPost/ context=", response.context



        response = self.client.get('/coldRoomPost/', follow=False)
        self.assertEqual(response.status_code, 200)
        self.print_response(response, display=False)
        print "/coldRoomPost/ context=", response.context

        return        

    def skip_test_newgame(self):
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

    def skip_test_inventory(self):
        client = Client()

        # response = client.get('/newGame/')
        # self.print_response(response)
        # self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, '/')

        # response = client.get('/')
        # self.assertEqual(response.status_code, 200)
        # self.print_response(response)
        # print "context=", response.context



        print "postDirector", "=" * 40
        response = client.post('/postDirector/', {'action': 'pick up scroll'}, follow=False)
        self.print_response(response)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')
        return        



        print "startPost", "=" * 40
        response = client.get('/startPost/')
        self.print_response(response, display=False)
        print "context=", response.context

        # Enter: read scrol ....
        response = client.post('/postDirector/', {'action': 'read scroll'})
        self.print_response(response)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')

        response = client.get('/startPost/')
        self.print_response(response, display=False)
        print "context=", response.context
        return


        # Answer Y
        print "/postDirector action:y"
        response = client.post('/postDirector/', {'action': 'n'},follow=False)
        #print "redirect_chain=",response.redirect_chain

        self.print_response(response,display=False)
        self.assertRedirects(response, '/startPost/', fetch_redirect_response=False)
        print "context=", response.context
        print "qq=",response.request

        response = client.get('/startPost/',follow=True)
        self.print_response(response, display=False)
        print "context=", response.context

        # Answer Y
        print "/postDirector action:y"
        response = client.post('/postDirector/', {'action': 'n'},follow=False)
        self.print_response(response,display=False)
        self.assertRedirects(response, '/startPost/', fetch_redirect_response=False)

        response = client.get('/startPost/')
        self.print_response(response,display=True)
        # Check content

        #import pdb;pdb.set_trace();

        print "END"
        #print "PATH_INFO", response.request['PATH_INFO']
        #print resolve('/mountains/')
        #import pdb;pdb.set_trace();


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
