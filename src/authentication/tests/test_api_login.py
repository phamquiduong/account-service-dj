import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

User = get_user_model()

TEST_CASES = {
    "email": "test_user@mail.com",
    "password": "Test@1234",
}


@pytest.mark.django_db
def test_login_success():
    assert reverse("auth_api_login") == "/auth/api/login"

    user = User.objects.create_user(email=TEST_CASES["email"], password=TEST_CASES["password"])  # type:ignore
    assert user.last_login is None

    client = APIClient()
    response = client.post(
        reverse("auth_api_login"),
        {
            "email": TEST_CASES["email"],
            "password": TEST_CASES["password"],
        },
        format="json",
    )

    assert response.status_code == 200  # type:ignore
    assert "access" in response.data  # type:ignore
    assert "refresh" in response.data  # type:ignore

    user.refresh_from_db()
    assert user.last_login is not None
