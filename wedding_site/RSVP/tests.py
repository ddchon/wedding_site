from django.test import SimpleTestCase

# Create your tests here.

class RSVPTests(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
