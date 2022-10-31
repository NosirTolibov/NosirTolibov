import pytest
from audio_play_list import AudioPlayList

TRACK_LIST = ['track1', 'track2', 'track3', 'track4', 'track5', 'track6', 'track7', 'track8', 'track9', 'track10']


class TestAudioPlayList:
    @pytest.fixture
    def audio_play_list_empty(self):
        return AudioPlayList()

    @pytest.fixture
    def audio_play_list_with_tracks(self):
        audio_play_list = AudioPlayList()
        audio_play_list.add_playlist(TRACK_LIST)
        return audio_play_list

    @pytest.fixture
    def audio_play_list_with_tracks_and_shuffling(self):
        audio_play_list = AudioPlayList()
        audio_play_list.add_playlist(TRACK_LIST)
        audio_play_list.shuffle()
        return audio_play_list

    @pytest.fixture
    def audio_play_list_with_tracks_and_repeat(self):
        audio_play_list = AudioPlayList()
        audio_play_list.add_playlist(TRACK_LIST)
        audio_play_list.repeat()
        return audio_play_list

    @pytest.fixture
    def audio_play_list_with_tracks_and_repeat_and_shuffling(self):
        audio_play_list = AudioPlayList()
        audio_play_list.add_playlist(['track1', 'track2', 'track3', 'track4', 'track5'])
        audio_play_list.repeat()
        audio_play_list.shuffle()
        return audio_play_list

    @pytest.mark.parametrize('audio_play_list', ['audio_play_list_empty', 'audio_play_list_with_tracks'])
    def test_add_track_to_playlist(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        audio_play_list.add('track100')
        assert 'track100' in audio_play_list.playlist

    @pytest.mark.parametrize('audio_play_list', ['audio_play_list_empty', 'audio_play_list_with_tracks'])
    def test_add_track_to_playlist_that_already_in_playlist(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        audio_play_list.add('track200')
        audio_play_list.add('track200')
        assert 'track200' in audio_play_list.playlist

    @pytest.mark.parametrize('audio_play_list', ['audio_play_list_empty', 'audio_play_list_with_tracks'])
    def test_add_list_of_tracks_to_playlist(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        new_track_list = ['track300', 'track301', 'track302']
        audio_play_list.add_playlist(new_track_list)
        assert all(element in audio_play_list.playlist for element in new_track_list)

    @pytest.mark.parametrize('audio_play_list', ['audio_play_list_empty', 'audio_play_list_with_tracks'])
    def test_add_playlist_to_playlist_that_already_in_playlist(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        new_track_list = ['track300', 'track301', 'track302']
        audio_play_list.add_playlist(new_track_list)
        audio_play_list.add_playlist(new_track_list)
        assert all(element in audio_play_list.playlist for element in new_track_list)

    def test_remove_track_from_playlist(self, audio_play_list_with_tracks):
        track_name = audio_play_list_with_tracks.playlist[2]
        audio_play_list_with_tracks.remove(2)
        assert track_name not in audio_play_list_with_tracks.playlist

    def test_get_track_position(self, audio_play_list_with_tracks):
        track_name = audio_play_list_with_tracks.playlist[2]
        assert audio_play_list_with_tracks.at(2) == track_name
        assert audio_play_list_with_tracks.at(100) is None

    def test_next_track_when_playlist_is_empty(self, audio_play_list_empty):
        audio_play_list_empty.next()
        assert audio_play_list_empty.current_track == 0

    @pytest.mark.parametrize('audio_play_list', ['audio_play_list_with_tracks'])
    def test_next_track_from_the_beginning(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        audio_play_list.next()
        assert audio_play_list.current_track == 1

    def test_next_track_in_last_track(self, audio_play_list_with_tracks):
        audio_play_list_with_tracks.current_track = len(audio_play_list_with_tracks.playlist) - 1
        assert audio_play_list_with_tracks.next() is None

    @pytest.mark.parametrize('audio_play_list', ['audio_play_list_with_tracks_and_repeat'])
    def test_next_track_in_last_track_with_repeat(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        audio_play_list.current_track = len(audio_play_list.playlist) - 1
        assert audio_play_list.next() == audio_play_list.playlist[0]
        assert audio_play_list.next() == audio_play_list.playlist[1]

    @pytest.mark.parametrize('audio_play_list', [
        'audio_play_list_with_tracks_and_shuffling', 'audio_play_list_with_tracks_and_repeat_and_shuffling'])
    def test_next_track_in_last_track_with_shuffling(self, audio_play_list, request):
        audio_play_list = request.getfixturevalue(audio_play_list)
        assert audio_play_list.next() in audio_play_list.playlist
