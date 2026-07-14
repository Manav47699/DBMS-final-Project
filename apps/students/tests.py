"""
Student module tests - CRUD, search, edge cases.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class StudentViewsTest(TestCase):
    """Test student views with raw SQL backend."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testadmin', password='testpass123')
        self.client.login(username='testadmin', password='testpass123')

    def test_student_list_requires_login(self):
        self.client.logout()
        resp = self.client.get(reverse('students:list'))
        self.assertRedirects(resp, f"{reverse('accounts:login')}?next=/students/")

    def test_student_list_loads(self):
        resp = self.client.get(reverse('students:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Students')

    def test_student_create_page_loads(self):
        resp = self.client.get(reverse('students:create'))
        self.assertEqual(resp.status_code, 200)

    def test_student_create_valid(self):
        from repositories import course_repo
        # Ensure we have a course
        cid = course_repo.insert_course('Test Course', '6 months', 100, 'Desc')
        resp = self.client.post(reverse('students:create'), {
            'name': 'John Doe',
            'email': 'john@test.com',
            'gender': 'male',
            'course_id': str(cid),
        })
        self.assertRedirects(resp, reverse('students:list'))

    def test_student_create_invalid_missing_name(self):
        resp = self.client.post(reverse('students:create'), {
            'name': '',
            'email': 'j@test.com',
            'gender': 'male',
        })
        self.assertEqual(resp.status_code, 200)
        # Form is re-displayed (no redirect)
        self.assertNotEqual(resp.status_code, 302)
