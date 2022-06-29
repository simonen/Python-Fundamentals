class Comment:

    def __init__(self, username, content, likes=0):
        self.likes = likes
        self.username = username
        self.content = content


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)