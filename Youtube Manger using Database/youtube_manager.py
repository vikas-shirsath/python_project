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
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video():
    name = input("Enter Video Name : ")
    time = input("Enter the video Duration : ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()
    
def update_video():
    video_id = input("Enter Video Number to update video : ")
    new_name = input("Enter Video Name : ")
    new_time = input("Enter the video Duration : ")
    cursor.execute("UPDATE videos  SET name = ?, time = ?, WHERE id = ?",(new_name, new_time, video_id))
    conn.commit()
    
def delete_video():
    video_id = input("Enter Video Number to update video : ")
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main() :
    while(True):
        print("\nYoutube Manager app with DB || Choose an option ")
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
    
    conn.close()

if __name__ == "__main__" :
    main()