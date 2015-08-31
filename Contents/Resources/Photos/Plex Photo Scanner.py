import os, os.path, time
import Filter, Media, PhotoFiles, VideoFiles
import UnicodeHelper

# Scans through files, and add to the media list.
def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):
  
  # Filter out bad stuff.
  Filter.Scan(path, files, mediaList, subdirs, PhotoFiles.photo_exts + VideoFiles.video_exts, root)
  
  # Add all the photos to the list.
  for path in files:
    file = os.path.basename(path)
    title,ext = os.path.splitext(file)
    ext = ext[1:].lower()
    
    name = UnicodeHelper.filenameToString(title)
    
    if ext in PhotoFiles.photo_exts:
      photo = Media.Photo(name)
    
      # Creation date, year.
      created_at = time.localtime(os.path.getmtime(path))
      photo.released_at = time.strftime('%Y-%m-%d', created_at)
      photo.year = int(time.strftime('%Y', created_at))
    
      # Add the photo.
      photo.parts.append(path)
      mediaList.append(photo)
    else:
      
      # Add the video.
      video = Media.Video(name)
      video.parts.append(path)
      mediaList.append(video)
      