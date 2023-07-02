from src.channel import Channel

class Video(Channel):

    def __init__(self, id_video):
        self.__id_video = id_video
        video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.title = str(video_response['items'][0]['snippet']['title'])
        self.url = f"https://youtu.be/{self.__id_video}"
        self.count_of_views = int(video_response['items'][0]['statistics']['viewCount'])
        self.count_of_likes = int(video_response['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return f"{self.title}"

    @property
    def channel_id(self):
        return self.__id_video

class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.get_service().playlistItems().list(playlistId=id_playlist, part='contentDetails', maxResults=20).execute()