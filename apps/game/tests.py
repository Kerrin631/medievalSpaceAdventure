# import unittest
from django.test import Client
from django.test import TestCase
#from django.core.urlresolvers import resolve


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def print_response(self, response, display=False):
        print " "
        print "test", response.request['REQUEST_METHOD'], response.request['PATH_INFO'], "code=", response.status_code,
        if display:
            print "-" * 80
            print "response=", response
            print "-" * 80
        else:
            print "len=", len(response.content)

    def test_refactoring_support(self):
        print "test /newGame/ -> '/'"
        response = self.client.get('/newGame/', follow=True)
        self.print_response(response)
        print "test redirect=", response.redirect_chain
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')

        print "test postDirector1 '/' -> 'pick up scroll' -> /startPost/ ", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'pick up scroll'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/startPost/')
        self.assertTrue("Scroll" in response.context['inventory'])
        self.assertContains(response, "<li><b>Palace Chambers</b></li>", count=1)
        self.assertContains(response, "Picked up scroll.", count=1)
        print "test inventory=", response.context['inventory']
        #print "test redirect=", response.redirect_chain

        print "test postDirector2 -> /startPost/ -> 'read scroll' -> '/startPost/'", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'read scroll'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/startPost/')
        self.assertTrue("Scroll" in response.context['inventory'])
        self.assertContains(response, "<li><b>Palace Chambers</b></li>", count=1)
        self.assertContains(response, ">Would you like to save the Princess? Y/N", count=1)
        self.assertContains(response, "read scroll", count=1)
        print "test inventory=", response.context['inventory']


        print "test postDirector3 /startPost/ -> 'Y' -> /mountains/", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'Y'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/mountains/')
        print "test inventory=", response.context['inventory']

        # jump ot coldRoom
        print "test postDirector4 /mountains/ -> 'Y'-> /coldRoom/", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'Y'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/coldRoom/')
        print "test inventory=", response.context['inventory']

        print "test postDirector5 /coldRoom/ -> 'grab key' -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'grab key'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/coldRoomPost/')
        self.assertTrue("Bronze Key" in response.context['inventory'])
        print "test inventory=", response.context['inventory']

        print "test postDirector6 -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use key'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHall/')
        self.assertTrue("Bronze Key" in response.context['inventory'])
        print "test inventory=", response.context['inventory']

        print "test postDirector7 /prisonHall/ -> 'use western door' -> /prisonHallPost/", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use western door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHallPost/')
        self.assertTrue("Bronze Key" in response.context['inventory'])
        print "test inventory=", response.context['inventory']

        print "test postDirector8 /prisonHallPost/ ->'grab sword'-> /prisonHallPost/", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'grab sword'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHallPost/')
        print "test inventory=", response.context['inventory']
        self.assertTrue("Sword" in response.context['inventory'])

        # prisonHallPost 'kill orc'
        print "test postDirector9 /prisonHallPost/ -> 'kill orc'-> /prisonHallPost/", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'kill orc'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHallPost/')

        print "test postDirector10 /prisonHallPost/ -> 'use northern door' -> openRoom", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use northern door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/openRoom/')
        self.assertContains(response, "<li><b>Open Room</b></li>", count=1)
        print "test inventory=", response.context['inventory']

        print "test postDirector11 -> sphinxLair", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use eastern door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLair/')
        self.assertContains(response, "<b>* #1: I live in light but die when it shines upon me. What am I?</b>", count=1)

        print "test postDirector12 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'shadow'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')

        print "test postDirector13 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'M'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')

        # needle
        print "test postDirector14 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'Needle'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')
        #print "context=", response.context

        # grab key
        print "test postDirector15 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'grab key'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')
        #print "context=", response.context
        print "test inventory=", response.context['inventory']

        print "test postDirector16 -> openRoom", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use western door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/openRoom/')
        #print "context=", response.context
        print "test inventory=", response.context['inventory']

        print "test postDirector17 -> openRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use northern door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/spaceRoom/')
        #print "test context=", response.context
        print "test inventory=", response.context['inventory']

        print "test postDirector18 spaceRoom -> cypherRoom", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'open west door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/cypherRoom/')
        #print "context=", response.context
        #print "inventory=", response.context['inventory']

        print "test postDirector19 cypherRoomPost -> dragonsLair", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'opensesame'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/dragonsLair/')

        print "test postDirector19 dragonsLair -> dragonsLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'chest'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/dragonsLairPost/')

        for i in range(1, 10):
            print "test postDirector19-", i, "dragonsLair -> dragonsLairPost", "=" * 40
            response = self.client.post('/postDirector/', {'action': 'chest'}, follow=True)
            self.print_response(response, display=False)
            self.assertRedirects(response, '/dragonsLairPost/')

        print "test postDirector20 dragonsLairPost -> cockpit", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use north door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/cockpit/')
        self.assertContains(response, "<b>** THE END **</b>", count=1)

        return
        #  Continue testing
