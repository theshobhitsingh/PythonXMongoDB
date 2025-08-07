# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient(
#     "Add the MongoDB Path")
# db = client['ytmanager']
# video_collection = db["videos"]


# def list_all_videos():
#     print('\n' + '<=>' * 30)
#     videos = list(video_collection.find())
#     if not videos:
#         print("No videos found.")
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. {video['name']}, Duration: {video['time']}")
#     print('<=>' * 30 + '\n')


# def add_video():
#     name = input("Enter Video Name: ")
#     time = input("Enter Video Length: ")
#     video_collection.insert_one({'name': name, 'time': time})
#     print("Video added successfully!")


# def update_video():
#     videos = list(video_collection.find())
#     list_all_videos()
#     try:
#         index = int(input("Which video number do you want to update? "))
#         if 1 <= index <= len(videos):
#             name = input("Enter the new Video Name: ")
#             time = input("Enter the new Video Time: ")
#             video_id = videos[index - 1]['_id']
#             video_collection.update_one(
#                 {'_id': video_id}, {'$set': {'name': name, 'time': time}})
#             print("Video updated successfully!")
#         else:
#             print("Invalid index selected!")
#     except ValueError:
#         print("Invalid input! Please enter a number.")


# def delete_video():
#     videos = list(video_collection.find())
#     list_all_videos()
#     try:
#         index = int(input("Which video number do you want to delete? "))
#         if 1 <= index <= len(videos):
#             video_id = videos[index - 1]['_id']
#             video_collection.delete_one({'_id': video_id})
#             print("Video deleted successfully!")
#         else:
#             print("Invalid index selected!")
#     except ValueError:
#         print("Invalid input! Please enter a number.")


# def main():
#     while True:
#         print("\nYouTube Manager || Choose an Option")
#         print("1. List All Favourite Videos")
#         print("2. Add a YouTube Video")
#         print("3. Update a YouTube Video")
#         print("4. Delete a YouTube Video")
#         print("5. Exit the Application")
#         choice = input("Enter your choice: ")

#         match choice:
#             case '1':
#                 list_all_videos()
#             case '2':
#                 add_video()
#             case '3':
#                 update_video()
#             case '4':
#                 delete_video()
#             case '5':
#                 print("Exiting YouTube Manager. Goodbye!")
#                 break
#             case _:
#                 print("Invalid Choice!")


# if __name__ == "__main__":
#     main()
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch Mongo URI from environment
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['ytmanager']
video_collection = db["videos"]

def list_all_videos():
    print('\n' + '<=>' * 30)
    videos = list(video_collection.find())
    if not videos:
        print("No videos found.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('<=>' * 30 + '\n')


def add_video():
    name = input("Enter Video Name: ")
    time = input("Enter Video Length: ")
    video_collection.insert_one({'name': name, 'time': time})
    print("Video added successfully!")


def update_video():
    videos = list(video_collection.find())
    list_all_videos()
    try:
        index = int(input("Which video number do you want to update? "))
        if 1 <= index <= len(videos):
            name = input("Enter the new Video Name: ")
            time = input("Enter the new Video Time: ")
            video_id = videos[index - 1]['_id']
            video_collection.update_one(
                {'_id': video_id}, {'$set': {'name': name, 'time': time}})
            print("Video updated successfully!")
        else:
            print("Invalid index selected!")
    except ValueError:
        print("Invalid input! Please enter a number.")


def delete_video():
    videos = list(video_collection.find())
    list_all_videos()
    try:
        index = int(input("Which video number do you want to delete? "))
        if 1 <= index <= len(videos):
            video_id = videos[index - 1]['_id']
            video_collection.delete_one({'_id': video_id})
            print("Video deleted successfully!")
        else:
            print("Invalid index selected!")
    except ValueError:
        print("Invalid input! Please enter a number.")


def main():
    while True:
        print("\nYouTube Manager || Choose an Option")
        print("1. List All Favourite Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video")
        print("4. Delete a YouTube Video")
        print("5. Exit the Application")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                print("Exiting YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main()
