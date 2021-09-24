from urllib.request import urlopen
import json

url_post = 'https://jsonplaceholder.typicode.com/posts'
url_comment = 'https://jsonplaceholder.typicode.com/comments'

response_post = urlopen(url_post)
post_data = json.loads(response_post.read())

response_comment = urlopen(url_comment)
comment_data = json.loads(response_comment.read())

def get_post():
    global post_data
    return post_data
def user_post(id):
    global post_data
    l = []
    for data in post_data:
        if data['userId']  == id:
            l.append(data)
    return l
def post_details():
    global post_data
    return list(post_data[0].keys())

def get_comment():
    global comment_data
    return comment_data
def comment_post(postid):
    global comment_data
    l = []
    for data in comment_data:
        if data['postId'] == postid:
            l.append(data)
    return l
print(user_post(3))