
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.list_posts = []
        self.following = []

    def add_post(self, post):
        return(self.list_posts.append(post))

    def get_timeline(self):
        return(self.list_posts)

    def follow(self, other):
        return(self.following.append(other))
