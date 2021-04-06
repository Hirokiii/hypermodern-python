from hypermodern_python import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="ja")
    args, _ = mock_requests_get.call_args
    assert "ja.wikipedia.org" in args[0]
