from yt_video.yt_video import vid_downloader, convrt_to_cap_audio
import sys

vid_downloader(sys.argv[1], sys.argv[2])
convrt_to_cap_audio(sys.argv[2], sys.argv[3])
