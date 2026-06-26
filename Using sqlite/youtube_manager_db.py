import sqlite3

con = sqlite3.connect('youtube-manager.db')

cursor = conn.cursor()

cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )       
''')

def list_all_video():
    pass 

def add_video(name, time):
    pass 

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
            

if __name__==__main__:
    main()