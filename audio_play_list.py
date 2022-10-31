import random


class AudioPlayList:

    def __init__(self):
        """ inits a player """
        self._repeat = False
        self._shuffle = False
        self.playlist = []
        self.current_track = 0

    def add(self, track: str):
        """ check that a track is not in the player and adds it """
        if track in self.playlist:
            print(f'Track "{track}" is already in the playlist')
        else:
            self.playlist.append(track)
            print(f'Track "{track}" successfully added to the playlist')

    def add_playlist(self, _playlist: list):
        """ add a list of tracks to the playlist """
        for track_item in _playlist:
            if track_item not in self.playlist:
                self.playlist.append(track_item)

    def next(self):
        """ returns a next track (or None on last track, when repeat mode is off) """
        if self.playlist:
            if self._repeat:
                if self._shuffle:
                    self.current_track = random.randint(0, len(self.playlist) - 1)
                else:
                    if self.current_track == len(self.playlist) - 1:
                        self.current_track = 0
                    else:
                        self.current_track += 1
                return self.playlist[self.current_track]
            else:
                if self._shuffle:
                    self.current_track = random.randint(0, len(self.playlist) - 1)
                    return self.playlist[self.current_track]
                else:
                    if self.current_track == len(self.playlist) - 1:
                        return None
                    else:
                        self.current_track += 1
                        return self.playlist[self.current_track]
        else:
            return None

    def at(self, pos: int):
        """ return a track at the `pos` position """
        if len(self.playlist) > pos > 0:
            self.current_track = pos
            return self.playlist[self.current_track]
        else:
            return None

    def shuffle(self):
        """ shuffles tracks list and makes the `next` method returns random tracks """
        self._shuffle = True

    def unshuffle(self):
        """ makes next to return tracks one by one according to the original order """
        self._shuffle = False

    def repeat(self):
        """ turn on repeat mode: `next` method returns first track after last track """
        self._repeat = True

    def unrepeat(self):
        """ turn off repeat mode: `next` after last track returns None """
        self._repeat = False

    def remove(self, pos: int):
        """ remove a track at the `pos` position from the player """
        if len(self.playlist) > pos > 0:
            print(f'Track "{self.playlist[pos]}" successfully removed from the playlist')
            self.playlist.pop(pos)
        else:
            print(f'No track at position {pos}')







