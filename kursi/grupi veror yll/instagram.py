import instaloader
insta=instaloader.Instaloader()
username=input("Enter the username:")

profile=instaloader.Profile.from_username(insta.context,username)
print("Username:",profile.username)
print("Number of posts:",profile.mediacount)
print("Followers",profile.followers)