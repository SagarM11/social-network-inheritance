from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
   def __init__(self, text, timestamp=None):
      self.text = text
      self.timestamp = timestamp
   def set_user(self, user):
    pass


class TextPost(Post):  # Inherit properly
  def __init__(self, text, timestamp=None):
    super(TextPost,self).__init__(text,timestamp)
  def __str__(self):
    return((


class PicturePost(Post):  # Inherit properly
  def __init__(self, text, image_url, timestamp=None):
    super(PicturePost,self).__init__(text,timestamp)
    self.image = image_url
 
  def __str__(self):
    pass


class CheckInPost(...):  # Inherit properly
  def __init__(self, text, latitude, longitude, timestamp=None):
    super(CheckInPost,self).__init__(text,timestamp)
    self.latitude = latitude
    self.longitude = longitude
  def __str__(self):
    pass
