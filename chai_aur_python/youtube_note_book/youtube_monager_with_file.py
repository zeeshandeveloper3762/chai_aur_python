# import json

# def load_data():
#     try:
#         with open('youtube.txt', 'r') as file:
#             test = json.load(file)
#             return test
#     except FileNotFoundError:
#         return []
    
# def save_data_helper(videos):
#     with open('youtube.txt', 'w') as file:
#         json.dump(videos, file)

# def list_all_videos(videos):
#     print("\n")
#     print("*" * 70)
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. {video['name']}, Duration: {video['time']} ")
#     print("\n")
#     print("*" * 70)

# def add_video(videos):
#     name = input("Enter video name: ")
#     time = input("Enter video duration: ")
#     videos.append({"name": name, "time": time})

# def update_video(videos):
#     list_all_videos(videos)


# def delete_video():
#     pass





# def main():
#     videos = load_data()
#     while True:
#         print("1. List all youtube videos ")
#         print("2. Add a youtube video ")
#         print("3. Update a youtube video details ")
#         print("4. Delete a youtube video ")
#         print("5. Exit the app ")
#         choice = input("Enter your choice: ")
#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_video(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             case _:
#                 print("Invalid coice")


# if __name__ == "__main__":
#     main()


import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    # giving all videos to update video
    list_all_videos(videos)

    # video number to update video
    index = int(input("Enter the video number to update: "))

    # Validation ager user 1 se kam ya file (videos) ke legth se zyada ka namber dale to use message show karen "Invalid index selected"
    if index >= 1 <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))
    
    if index >= 1 <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main() 