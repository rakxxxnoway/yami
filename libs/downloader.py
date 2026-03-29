import os
from pathlib import Path

from ffmpeg import FFmpeg
from pytubefix import YouTube
from pytubefix.cli import on_progress

class Downloader:
    __ROOT_PATH             = "temp/"
    __AUDIO_FORMAT_ON_DOWN  = "m4a"
    __AUDIO_FORMAT_ON_UP    = "mp3"
    __VIDEO_FORMAT          = "mp4"


    def __init__(self, url, audio_only=False):
        self.__url          = url
        self.__audio_only   = audio_only
        self.__file_name    = ""


    # pytube (fixed) methods
    def download(self) -> None:
        src = YouTube(self.__url, on_progress_callback=on_progress)

        if self.__audio_only:
            stream = src.streams.get_audio_only()
            name = f"temp.{self.__AUDIO_FORMAT_ON_UP}"

        else:
            stream = src.streams.get_highest_resolution()
            name = f"temp.{self.__VIDEO_FORMAT}"

        stream.download(filename=name, output_path=self.__ROOT_PATH)


    # local methods
    def check_format(self, f:list) -> bool:
        if f[1] == self.__AUDIO_FORMAT_ON_DOWN:
            return True
        
        if f[1] == self.__VIDEO_FORMAT:
            return True
        
        return False
    

    def fix_fname(self, fname:str) -> list:
        return fname.strip().replace(" ", "_").split(".")


    @property
    def get_files(self) -> list:
        return os.listdir(self.__ROOT_PATH)


    @property
    def get_name(self) -> str:
        if not os.path.isdir(self.__ROOT_PATH):
            return None
        
        try:
            for f in self.get_files:
                fixed = self.fix_fname(f)
                fname = ".".join(fixed)

                os.rename(os.path.join(self.__ROOT_PATH, f), os.path.join(self.__ROOT_PATH, fname))

                if self.check_format(fixed):
                    return fname
                
        except Exception as e:
            print(e)

    
    def clear(self) -> None:
        for f in self.get_files:
            fpath = os.path.join(self.__ROOT_PATH, f)
            os.remove(fpath)


    def convert_audio(self, file_name):
        pass
    
