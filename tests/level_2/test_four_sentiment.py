import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.fixture
def good_words() -> set[str]:
    return {"#g1", "#g2", "#g3"}


@pytest.fixture
def bad_words() -> set[str]:
    return {"#b1", "#b2", "#b3"}


@pytest.fixture
def text_good_words_more_than_bab_words() -> str:
    return "#g1 ev 4r #b1 #g3 er ed #b3 fr #g2"


def test__check_tweet_sentiment__check_that_good_words_nun_more_than_bad_words_num(
    text_good_words_more_than_bab_words: str,
    good_words: set[str],
    bad_words: set[str],
) -> None:
    assert (
        check_tweet_sentiment(
            text_good_words_more_than_bab_words, good_words, bad_words
        )
        == "GOOD"
    )


@pytest.fixture
def text_bad_words_more_than_good_words() -> str:
    return "#b1 ev 4r #g1 #b3 er ed #g3 fr #b2"


def test__check_tweet_sentiment__check_that_bad_words_nun_more_than_good_words_num(
    text_bad_words_more_than_good_words: str,
    good_words: set[str],
    bad_words: set[str],
) -> None:
    assert (
        check_tweet_sentiment(
            text_bad_words_more_than_good_words, good_words, bad_words
        )
        == "BAD"
    )


@pytest.fixture
def text_bad_words_equal_good_words() -> str:
    return "#b1 ev 4r #g1 #b3 #g2 er ed #g3 fr #b2"


def test__check_tweet_sentiment__check_that_bad_words_nun_equal_good_words_num(
    text_bad_words_equal_good_words: str,
    good_words: set[str],
    bad_words: set[str],
) -> None:
    assert (
        check_tweet_sentiment(text_bad_words_equal_good_words, good_words, bad_words)
        is None
    )


@pytest.fixture
def text_no_contents_both_good_and_bad_words() -> str:
    return "ev 4r er ed fr"


def test__check_tweet_sentiment__check_that_text_doesnt_content_both_good_and_bad_words(
    text_no_contents_both_good_and_bad_words: str,
    good_words: set[str],
    bad_words: set[str],
) -> None:
    assert (
        check_tweet_sentiment(
            text_no_contents_both_good_and_bad_words, good_words, bad_words
        )
        is None
    )
