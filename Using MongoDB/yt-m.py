from pymongo import MongoClient

client = MongoClient("mongodb+srv://12_3:12_3@cluster0.solb9us.mongodb.net/")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_video():
    pass

def add_video(name, time):
    pass

def update_video(video_id, new_name, new_time):
    pass 

def delete_video(video_id):
    pass 

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
            video_id = input("Enter the number of video to update: ")
            new_name = input("Enter the title of the new video: ")
            new_time = input("Enter the time of the new video: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = input("Enter the number of video to delete: ")
            delete(video_id)
        elif choice == '5':
            break
        else:
            print("Inalid input")

if __name__ == "__main__":
    main()