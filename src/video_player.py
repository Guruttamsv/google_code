"""A video player class."""

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
        a=self._video_library.get_all_videos()
        for x,y in a.items():
            print(x, "(",y[0],")",y[1])

    def play_video(self,video_id,fix):
        a=self._video_library.get_video(video_id)
        if fix is not None and a is not None:
            print("Stopping video:", fix)
        if  a is None:
            print("Cannot Play video: Video does not exist")
        else:
            fix=a
            print("Playing video:",fix)
        return fix

    def stop_video(self,fix):
        """Stops the current video."""
        if fix is not None:
            print("Stopping Video", fix)
            fix=None
        else:
            print("Cannot stop video: No video is currently playing")
        return fix    

    def play_random_video(self, fix):
        if fix is not None:
            print("Stopping video:", fix)
        a=self._video_library.get_all_videos()
        fix=random.choice(list((a.keys())))
        print("Playing video:",fix)
        return fix

    def pause_video(self,fix,con):
        if fix is not None:
            if con==1:
                print("Video already paused:",fix)
            else:    
                print("Pausing video", fix)
                con=1
        else:
            print("Cannot pause video: No video is currently playing")
        return con
    def continue_video(self,fix,con):
        if fix is None:
            print("Cannot continue video: No video is currently playing")
        else:
            if(con==1):
                print("Continuing video:", fix)
                con=0
            else:
                print("Cannot continue video: Video is not paused")
        return con

    def show_playing(self,fix):
        if fix is not None:
            print("Currently playing:",fix)
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name,playlists):
        if playlist_name in playlists:
            print("Cannot create playlist: A playlist with this name already exists") 
        else:    
            playlists[playlist_name]=[]
            print("Successfully created new playlist:", playlist_name)
        return playlists

    def add_to_playlist(self, playlist_name, video_id,playlists):
        a=self._video_library.get_video(video_id)
        if playlist_name not in playlists:
            print("Cannot add video to ",playlist_name,": Playlist does not exist")
            return playlists
        elif  a is None:
            print("Cannot add video to",playlist_name,": Video does not exist")
            return playlists
        
        else:
            n=playlists[playlist_name]
            if(a in n):
              print("Cannot add video to ",playlist_name,": Video already added") 
            else: 
                n.append(a)
                playlists[playlist_name]=n
                print("Added video to",playlist_name,":",a)
        print(playlists)
        return playlists

    def show_all_playlists(self,playlists):
        r=False
        for element in playlists:
            if element:
                r=True
        if r==True:
            print("Showing all playlists:")
            for i in playlists.keys():
                print(i)
        else:
            print("No playlist exists")

    def show_playlist(self, playlist_name,playlists):
        if playlist_name not in playlists:
            print("Cannot show ",playlist_name,": Playlist does not exist")
        print("Showing Playlist",playlist_name)
        if playlists[playlist_name]==[]:
            print("No videos in playlist")
        else:    
            for i in playlists[playlist_name]:
                print(i)

    def remove_from_playlist(self, playlist_name, video_id,playlists):
        if playlist_name not in playlists:
            print("Cannot remove video from",playlist_name,": Playlist does not exist")
        n=playlists[playlist_name]
        if(video_id not in n):
              print("Cannot remove video in ",playlist_name,": Video is not in playlist") 
        else: 
            n.aremove(video_id)
            playlists[playlist_name]=n
            print("Removed video from",playlist_name,":",a)  
        return playlists
            

    def clear_playlist(self, playlist_name,playlists):
        if playlist_name not in playlists:
            print("Cannot clear playlist ",playlist_name,": Playlist does not exist")
        else:    
            playlists[playlist_name]=[]
            print("Successfully cleared all videos from playlist")
        return playlists

    def delete_playlist(self, playlist_name,playlists,fix):
        if playlist_name not in playlists:
            print("Cannot delete playlist",playlist_name,": Playlist does not exist")
        else:
            del playlists[playlist_name]
            print("Deleted playlist:",playlist_name)
        return playlists

    def search_videos(self, search_term):
        a=self._video_library.get_all_videos()
        t=1
        j=1
        sign=[]
        for x,y in a.items():
            if(search_term in x):
                sign.append(x)
                print(t,")",x, "(",y[0],")",y[1])
                t=+1
                j=0
        if j==1:
            print("No search results for",search_term)
        else:
            print("""Would you like to play any of the above? If yes, specify the number of the video.
If your answer is not a valid number, we will assume it's a no.""")
        ijk=input()
        if ijk.isdigit():
            if int(ijk)>0 and int(ijk)<0:
                print("Playing",sign[int(ijk)-1])
                fix=sign[int(ijk)-1]
            return fix      

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
