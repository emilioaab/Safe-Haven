from django.test import TestCase
from django.urls import reverse, resolve
from aid_org.views import aid_org_detail  # Import the actual view function for the 'aid_org_detail' URL

class TestUrls(TestCase):
    def test_aid_org_detail_url_is_resolved(self):
        url = reverse('aid_org:detail', args=['latet'])  # Replace 'some-slug' with an actual slug  # Replace 'some-slug' with an actual slug
        self.assertEqual(resolve(url).func, aid_org_detail)  # Compare the resolved URL function to the actual view function