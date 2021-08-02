from instagramy import InstagramUser

name = input("Enter user name:")

user = InstagramUser(name)

followers = user.number_of_followers
print('Total followers:', followers)

following = user.number_of_followings
print('Total followings:', following)

posts = user.number_of_posts
print('Total posts:', posts)

bio = user.biography
print('Bio:\n', bio)

link_in_bio = user.website
print('Link in Bio:', link_in_bio)


OUTPUT :


Enter user name:malini_hariram
Total followers: 196
Total followings: 327
Total posts: 1
Bio:
 First cry on Jan 22😜🎂
Movie freak🤗
Born to shine bright😇
Music addictz 🎶
Link in Bio: None
