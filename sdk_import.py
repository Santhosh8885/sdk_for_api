import sdk_for_api

post_details = sdk_for_api.post_details()
print("post details :",post_details)

post_data = sdk_for_api.get_post()
print("Post data: ",post_data)

post_based_on_userId = sdk_for_api.user_post(int(input("user id :")))
print("post_based_on_userId :",post_based_on_userId)

comment_data = sdk_for_api.get_comment()
print("comment_data :",comment_data)

comment_based_on_post = sdk_for_api.comment_post(int(input("post id :")))
print("comment_based_on_post :",comment_based_on_post)