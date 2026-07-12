import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

TEST_CASES = {
    "username": "test_user",
    "password": "Test@1234",
}


@pytest.mark.django_db
def test_create_normal_user():
    user = User.objects.create_user(username=TEST_CASES["username"], password=TEST_CASES["password"])

    assert user.id is not None  # type:ignore
    assert user.username == TEST_CASES["username"]
    assert user.check_password(raw_password=TEST_CASES["password"]) is True


@pytest.mark.django_db
def test_create_super_user():
    user = User.objects.create_superuser(username=TEST_CASES["username"], password=TEST_CASES["password"], email=None)

    assert user.id is not None  # type:ignore
    assert user.username == TEST_CASES["username"]
    assert user.check_password(raw_password=TEST_CASES["password"]) is True

    assert user.is_active is True
    assert user.is_staff is True
    assert user.is_superuser is True
