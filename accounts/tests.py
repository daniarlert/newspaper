from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpView


class LoginPageTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create("tester", "testpassword")

        cls.user.is_active = True
        cls.user.save()

    def test_user_information(self):
        self.assertEqual(self.user.username, "tester")
        self.assertEqual(self.user.password, "testpassword")

    def test_login_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_login_success(self):
        login_data = {
            "username": self.user.username,
            "password": "testpassword",
        }

        response = self.client.post(reverse("login"), data=login_data, follow=True)
        self.assertEqual(response.context["user"].is_authenticated, True)


class SignUpPageTest(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
