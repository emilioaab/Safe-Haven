from django.urls import reverse
from django.test import TestCase, Client
from aid_org.models import AidOrg

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.aid_org = AidOrg.objects.create(
            name='Test Aid Org',
            slug='test-aid-org',
            image='aid_org_images/default.jpg',
            description='Test Description',
            logo='aid_org_logo/default.jpg',
            website='www.test.com',
            date='2022-01-01T00:00Z',
            thumb='default.png'
        )
        self.aid_org_url = reverse('aid_org:aid_org_detail', args=[self.aid_org.id])