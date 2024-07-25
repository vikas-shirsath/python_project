import sqlite3

conn = sqlite3.connect('youtube.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    pass

def add_video():
    name = input("Enter Video Name : ")
    time = input("Enter the video Duration : ")

def update_video():
    video_id = input("Enter Video Number to update video : ")
    name = input("Enter Video Name : ")
    time = input("Enter the video Duration : ")
    
def delete_video():
    video_id = input("Enter Video Number to update video : ")

def main() :
    while(True):
        print("\nYoutube Manager app with DB")
        print("1. List Videos")
        print("2. Add Videos ")
        print("3. Update Videos")
        print("4. Delete Video")
        print("5. Exit the app")
        choice = input("Enter a choice : ")
        
        match choice :
            case '1' :
                list_videos()
            case '2' :
                add_video()
            case '3' :
                update_video()
            case '4' :
                delete_video()
            case '5' :
                break
            case _ :
                print("Invalid Choice")

if __name__ == "__main__" :
    main()