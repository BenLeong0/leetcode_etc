import requests
import json
import os
import ffmpeg

API_KEY = "pub_PUWse7ZVAhv4mOzDvKWPUyz5puy1qTxZ"


def get_vids_by_tag(tag, limit=1000, offset=0, API_KEY=API_KEY):
    get_vids_url = f"https://developers.medal.tv/v1/search?text=%23{tag}&limit={limit}&offset={offset}"
    headers = {"authorization": API_KEY}

    r = requests.get(get_vids_url, allow_redirects=True, headers=headers)
    resp = json.loads(r.content)["contentObjects"]

    return resp


def check_vid(video, min_likes=0, min_views=20):
    if video["contentLikes"] < min_likes:
        return False
    if video["contentViews"] < min_views:
        return False
    return True


def filter_vids(vids):
    return [video for video in vids if check_vid(video)]


def download_videos(video_list, tag):
    for (i, video) in enumerate(video_list):
        print(video["contentId"], video["contentTitle"], video["credits"])
        user_id = video["credits"].split("/")[-1][:-1]
        vid_id = video["contentId"].split("cid")[-1]

        url = f"https://cdn.medal.tv/{user_id}/share-{vid_id}.mp4"
        print(url)

        resp = requests.get(url, allow_redirects=True)
        if resp.status_code == 404:
            print("Could not retrieve")
        else:
            # file name has user and vid id
            open(f"medal_dl/vids/{tag}/tmp_{i}.mp4", "wb").write(resp.content)
            # Write to database


def download_videos_by_tag(tag):
    try:
        os.mkdir(f"medal_dl/vids/{tag}")
    except:
        pass

    video_list = get_vids_by_tag(tag)
    video_list = filter_vids(video_list)
    download_videos(video_list, tag)


if __name__ == "__main__":
    tags = ["ace", "lvl10", "clutch"]
    for tag in tags:
        download_videos_by_tag(tag)
