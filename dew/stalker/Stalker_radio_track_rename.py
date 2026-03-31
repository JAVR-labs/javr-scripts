import os


def get_tracks(tracks_folder_path):
    return os.listdir(tracks_folder_path)


def get_next_name(tracks_folder_path):
    valid_tracks = get_valid_track(get_tracks(tracks_folder_path))
    last_track = valid_tracks[-1]
    next_track_num = ""

    for char in last_track:
        if char.isnumeric():
            next_track_num += char
    next_track_num = int(next_track_num) + 1
    return f"track_{next_track_num}.ogg"


def rename_file(old_file_path: str, new_name: str):
    new_file_path = f'{old_file_path.split("/")[0]}/{new_name}'
    os.rename(old_file_path, new_file_path)


def tracks_sorting(string: str):
    final_string = ""
    for char in string:
        if char.isnumeric():
            final_string += char
    return int(final_string)


def get_valid_track(tracks_to_check: list[str]) -> list[str]:
    valid_tracks = [track_to_check for track_to_check in tracks_to_check if
                    "track_" in track_to_check and ".ogg" in track_to_check]
    return sorted(valid_tracks, key=tracks_sorting)


if input("Add new path y/n: ").lower() == "y":
    with open("saved-paths.txt", "a+") as f_saved_paths:
        saved_paths = f_saved_paths.readlines()

        new_tracks_path = input("Enter the tracks path: ")
        if new_tracks_path not in saved_paths:
            f_saved_paths.write(new_tracks_path + "\n")
            print(f"{new_tracks_path} added to paths")
        else:
            print(f"{new_tracks_path} already in paths")


with open("saved-paths.txt", "r") as f_saved_paths:
    saved_paths = f_saved_paths.readlines()

    if len(saved_paths) > 0:
        for folder_path in saved_paths:
            folder_path = folder_path.strip()

            tracks = get_tracks(folder_path)

            altered_tracks = 0

            for track in tracks:
                if "track_" not in track and ".ogg" in track:
                    rename_file(f"{folder_path}/{track}", get_next_name(folder_path))
                    altered_tracks += 1

            print(f'{altered_tracks} track/s in "{folder_path}" have been renamed')
