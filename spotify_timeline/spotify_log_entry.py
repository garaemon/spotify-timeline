

class SpotifyLogEntry(object):
    PLAYED_AT_INDEX = 0
    SONG_ID_INDEX = 1
    SONG_TITLE_INDEX = 2
    SONG_URL_INDEX = 3
    ARTIST_NAME_INDEX = 4
    ALBUM_ID_INDEX = 5
    ALBUM_NAME_INDEX = 6

    def __init__(self, row):
        self.playe_at = row[self.PLAYED_AT_INDEX]
        self.song_id = row[self.SONG_ID_INDEX]
        self.song_title = row[self.SONG_TITLE_INDEX]
        self.song_url = row[self.SONG_URL_INDEX]
        self.artist_name = row[self.ARTIST_NAME_INDEX]
        self.album_id = row[self.ALBUM_ID_INDEX]
        self.album_name = row[self.ALBUM_NAME_INDEX]
