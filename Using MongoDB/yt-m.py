from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://12_3:<password>@cluster0.solb9us.mongodb.net/")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name" : name, "time" : time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("Youtube Manager App | Using MongoDB")
        print("1. List all videos")
        print("2. Add a video in the list")
        print("3. Update a video in the list ")
        print("4. Delete a video from the list ")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_all_video()
        elif choice == '2':
            name = input("Enter the video title: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the ID of video to update: ")
            new_name = input("Enter the title of the new video: ")
            new_time = input("Enter the time of the new video: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = input("Enter the ID  of video to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Inalid input")

if __name__ == "__main__":
    main()