from logic import test_logic
import pytest



@pytest.mark.unique_names
def test_check_unique_names():
    assert test_logic.test_names()


@pytest.mark.all_fields_db
def test_all_fields_db():
    assert test_logic.missing_fields() == []


@pytest.mark.all_fields_server
def test_all_fields_server():
    assert test_logic.user_fields_server() == []


def test_add_friend():
    assert test_logic.add_friend() == True


def test_song_search():
    assert test_logic.song_search() == []