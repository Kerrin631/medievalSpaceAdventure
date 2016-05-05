# import unittest
from django.test import Client
from django.test import TestCase
#from django.core.urlresolvers import resolve


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def print_response(self, response, display=False):
        print " "
        print response.request['REQUEST_METHOD'], response.request['PATH_INFO'], response.status_code
        if display:
            print "-" * 80
            print "response=", response
            print "-" * 80
        else:
            print "len=", len(response.content)

    def test_refactoring_support(self):
        print "=" * 80
        response = self.client.get('/newGame/', follow=True)
        self.print_response(response)
        print "redirect=", response.redirect_chain
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')
        print "/newGame/ context=", response.context

        print "postDirector", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'pick up scroll'}, follow=True)
        self.print_response(response, display=False)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')
        print "inventory=", response.context['inventory']
        self.assertTrue("Scroll" in response.context['inventory'])
        self.assertContains(response, "<li><b>Palace Chambers</b></li>", count=1)
        self.assertContains(response, "Picked up scroll.", count=1)

        print "postDirector2", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'read scroll'}, follow=True)
        self.print_response(response, display=False)
        print "context=", response.context
        self.assertRedirects(response, '/startPost/')
        #print "inventory=", response.context['inventory']
        self.assertTrue("Scroll" in response.context['inventory'])
        self.assertContains(response, "<li><b>Palace Chambers</b></li>", count=1)
        self.assertContains(response, ">Would you like to save the Princess? Y/N", count=1)
        self.assertContains(response, "read scroll", count=1)

        print "postDirector3", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'Y'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/mountains/')
        print "inventory=", response.context['inventory']

        # jump ot coldRoom
        print "postDirector4", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'Y'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/coldRoom/')
        print "inventory=", response.context['inventory']

        print "postDirector5 -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'grab key'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/coldRoomPost/')
        self.assertTrue("Bronze Key" in response.context['inventory'])

        print "inventory=", response.context['inventory']

        print "postDirector6 -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use key'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHall/')
        self.assertTrue("Bronze Key" in response.context['inventory'])
        print "inventory=", response.context['inventory']

        # prisonHall
        print "postDirector7 -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use western door'}, follow=True)
        self.print_response(response, display=False)
        #self.assertRedirects(response, '/prisonHall/')
        #self.assertTrue("Bronze Key" in response.context['inventory'])
        print "inventory=", response.context['inventory']

        # prisonHallPost 'grab sword'
        print "postDirector8 -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'grab sword'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHallPost/')
        print "inventory=", response.context['inventory']
        self.assertTrue("Sword" in response.context['inventory'])

        # prisonHallPost 'kill orc'
        print "postDirector9 -> coldRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'kill orc'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/prisonHallPost/')
        #print "inventory=", response.context['inventory']
        #print "context=", response.context

        # prisonHallPost 'use northern door'
        print "postDirector10 -> openRoom", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use northern door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/openRoom/')
        self.assertContains(response, "<li><b>Open Room</b></li>", count=1)

        print "postDirector11 -> sphinxLair", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use eastern door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLair/')
        self.assertContains(response, "<b>* #1: I live in light but die when it shines upon me. What am I?</b>", count=1)

        print "postDirector12 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'shadow'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')

        print "postDirector13 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'M'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')

        # needle
        print "postDirector14 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'Needle'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')
        #print "context=", response.context

        # grab key
        print "postDirector15 -> sphinxLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'grab key'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/sphinxLairPost/')
        #print "context=", response.context
        print "inventory=", response.context['inventory']

        print "postDirector16 -> openRoom", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use western door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/openRoom/')
        print "context=", response.context
        print "inventory=", response.context['inventory']

        print "postDirector17 -> openRoomPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use northern door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/spaceRoom/')
        print "context=", response.context
        print "inventory=", response.context['inventory']

        print "postDirector18 spaceRoom -> cypherRoom", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'open west door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/cypherRoom/')
        #print "context=", response.context
        #print "inventory=", response.context['inventory']

        print "postDirector19 cypherRoomPost -> dragonsLair", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'opensesame'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/dragonsLair/')

        print "postDirector19 dragonsLair -> dragonsLairPost", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'chest'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/dragonsLairPost/')

        for i in range(1, 10):
            print "postDirector19-",i,"dragonsLair -> dragonsLairPost", "=" * 40
            response = self.client.post('/postDirector/', {'action': 'chest'}, follow=True)
            self.print_response(response, display=False)
            self.assertRedirects(response, '/dragonsLairPost/')

        print "postDirector19-3 dragonsLairPost -> ?cockpit?", "=" * 40
        response = self.client.post('/postDirector/', {'action': 'use north door'}, follow=True)
        self.print_response(response, display=False)
        self.assertRedirects(response, '/cockpit/')
        # <b>** THE END **</b><
        self.assertContains(response, "<b>** THE END **</b>", count=1)

        return
        #  Continue testing
