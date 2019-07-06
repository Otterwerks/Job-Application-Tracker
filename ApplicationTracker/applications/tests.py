from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from applications.models import Application

class ApplicationTest(TestCase):

    def create_application( \
        self, \
        user_id=1, \
        position='test position', \
        company='test company', \
        location='test location', \
        department='test department', \
        company_url='test url', \
        posting_url='test url', \
        portal_url='test url', \
        portal_login='test login', \
        portal_pass='test pass', \
        status='test status', \
        body='test body', \
        resume='test resume', \
        cover_letter='test cover letter', \
        is_active=True, \
        is_stale=False, \
    ):
        return (Application.objects.create(
            user_id=user_id,
            position=position,
            company=company,
            location=location,
            department=department,
            company_url=company_url,
            posting_url=posting_url,
            portal_url=portal_url,
            portal_login=portal_login,
            portal_pass=portal_pass,
            status=status,
            body=body,
            posted_on=timezone.now(),
            closes_on=timezone.now(),
            applied_on=timezone.now(),
            resume=resume,
            cover_letter=cover_letter,
            is_active=is_active,
            is_stale=is_stale,
            last_updated=timezone.now()
        ))

    def test_application_creation(self):
        a = self.create_application()
        self.assertTrue(isinstance(a, Application))
        self.assertEqual(a.__unicode__(), a.__str__())

    def test_application_detail_view(self):
        a = self.create_application()
        res = self.client.get(reverse('application-detail'), {'application_id': 1})

        self.assertEqual(res.status_code, 200)
        self.assertIn(a.position, res.content)

    def test_application_index_view(self):
        a = self.create_application()
        res = self.client.get(reverse('application-list'))

        self.assertEqual(res.status_code, 200)
        self.assertIn(a.position, res.content)