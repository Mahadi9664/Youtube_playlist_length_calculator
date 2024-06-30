from pytube import Playlist
from pytube import YouTube

def playlist_length(url):
    try:
        pl = Playlist(url)

        len = 0
        for p in pl.video_urls:
            vid = YouTube(p)
            len += vid.length

        print(f"hour: {len//3600}, minute: {(len%3600)//60}")
    except :
        print("You did not give a playlist.")



def main():
    url = input("give link of your url: ")
    playlist_length(url)

if __name__ == "__main__":
    main()



