import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            data = json.load(file)
            return(data)
    except FileNotFoundError:
        return []
def save_data(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos,file)
videos = load_data()
def list_videos():
     for index,video in enumerate(videos, start =1):
         print(f"{index}. {video['name']}, Durations: {video['time']}")
def no_videos():
    print("No videos available")
def invalid_input():
    print("Invalid Input")
while True:
    print("1. List Videos")
    print("2. Add Video")
    print("3. Total Videos")
    print("4. Delete Videos")
    print("5. Update Video")
    print("6. Exit")
    choice = input("Enter Your Choice: ")
    match choice:
        case "1":
            list_videos()
        case "2":
            name = input("Enter video name: ")
            duration = input("Enter video duration: ")
            video  = {"name": name, "time": duration}
            videos.append(video)
            save_data(videos)
        case "3":
            print(f"Total Videos: {len(videos)}")
        case "4":
            try:
                if not videos:
                    no_videos()
                else:
                    list_videos()
                    del_ = int(input("Enter the Number of video, which you want to delete: "))
                    idx = del_ - 1
                    if 0 <= idx < len(videos):
                        print(f"Deleted: {videos[idx]}")
                        videos.pop(idx)
                        save_data(videos)
                    else:
                        print("Video not found")
            except ValueError:
                invalid_input()
        case "5":
            try:
                if not videos:
                    no_videos()
                else:
                    list_videos()
                    z = int(input("Enter the Number of video, which you want to update:  "))
                    upd = z - 1
                    if 0 <= upd < len(videos):
                        n = input("Enter New Name: ")
                        d = input("Enter Updated Duration: ")
                        video  = {"name": n, "time": d}
                        videos[upd] = video
                        save_data(videos)
                    else:
                        print("Video not found")
            except ValueError:
                invalid_input()
        case "6":
            break
        case _:
            print("Invalid Choice")