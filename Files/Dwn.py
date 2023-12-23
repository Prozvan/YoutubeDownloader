from pytube import YouTube



def downloadMusic(PATH, LINK, FORMAT, NAME="Unnamed"):

    yt = YouTube(LINK)
    NAME = yt.title

    print()
    try:
        
        if FORMAT == "1":   #MP3

            audio = yt.streams.get_audio_only().download(output_path=PATH, filename=NAME+".mp3")

            print(f"\t\t\tDownloaded: {NAME}.mp3")

        elif FORMAT == "2":
            
            video = yt.streams.get_highest_resolution().download(output_path=PATH, filename=NAME+".mp4")
 
            print(f"\t\t\tDownloaded: {NAME}.mp4")

        
    except FileExistsError: pass


