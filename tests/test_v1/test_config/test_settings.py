from config import settings


def test_bucket_name() -> None:
    assert settings.BUCKET_NAME == "my-bucket"
