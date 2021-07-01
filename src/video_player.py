"""A video player class."""

from src.video_playlist import Playlist
from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_info = self._video_library.get_all_videos()
        all_videos = []
        for i in video_info:
            video_information = {}
            video_information['title'] = i.title
            video_information['video_id'] = i.video_id
            video_information['tags'] = i.tags
            all_videos.append(video_information)
        print("Here's a list of all available videos:")
        def get_names(all_videos):
            return all_videos.get('title')
        all_videos.sort(key = get_names)
        for i in all_videos:
            print(f"    {i['title']} ({i['video_id']}) {i['tags']}")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video_info = self._video_library.get_all_videos()
        for i in video_info:
            if video_id == i.video_id:
                print(f"Playing video: {i.title}")
        def search(list, platform):
            for i in range(len(list)):
                if list[i] == platform:
                    return False
            return True
        video_id_list = []
        for i in video_info:
            video_id_list.append(i.video_id)
        if search(video_id_list, video_id):
            print("Cannot play video: Video does not exist")
        

    def stop_video(self):
        """Stops the current video."""
        stopped_video = self.video_id
        if stopped_video == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {stopped_video}")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.video_id != None:
            print(f"Stopping video: {self.video_id}")
        video_info = self._video_library.get_all_videos()
        a_list = []
        for i in video_info:
            a_list.append(video_info.title)
        a = random.randint(0, len(a_list)-1)
        print(f"Playing video: {a_list[a]}")

    def pause_video(self):
        """Pauses the current video."""
        current_video = self._video_library.get_video()
        if self.title == current_video.title:
            print(f"Pausing video: {self.title}")
        elif current_video == None:
            print(f"Cannot pause video: No video is currently playing")
        else:
            print(f"Video already paused: {self.title}")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        playlist_name = Playlist()
        if self != playlist_name:
            print(f"successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        for i in playlist_name:
            if i.title == video.title:
                print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print(f"Showing playlist: {playlist_name}")
        print(" No videos here yet")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        for i in playlist_name:
            if i.video_id == video_id:
                print(f"Removed video from {playlist_name}: {self.title}")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
