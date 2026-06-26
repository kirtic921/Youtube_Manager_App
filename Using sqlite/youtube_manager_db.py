import sqlite3

con = sqlite3.connect('youtube-manager.db')

cursor = con.cursor()

cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )       
''')

def list_all_video():
    cursor.execute("SELECT * FROM videos")
    print('*'*70)
    for row in cursor.fetchall():
        print(row)
    print('*'*70)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    print("Addition successful.")

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))
    con.commit()
    print("Updation successful.")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()
    print("Deletion successful.")

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_all_video()
        elif choice == '2':
            list_all_video()
            name = input("Enter the video name: ")
            time = input("Enter the duration of the video: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the duration of the video: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid input." )
    con.close()            

if __name__== "__main__":
    main()