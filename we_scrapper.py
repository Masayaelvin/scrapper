import requests
from bs4 import BeautifulSoup
import json
import time


#username = $1

def get_reels_data(username):
    base_url = f'https://www.instagram.com/{username}/reels/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # Send a GET request to the Instagram Reels page
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the page
    reels_data = []

    # Example: Extracting video links, likes, shares, comments
    reels = soup.find_all('div', {'class': 'tCibT'})
    for reel in reels:
        video_link = reel.find('a')['href']
        likes_count = reel.find('span', {'class': 'zV_Nj'}).text
        shares_count = reel.find('span', {'class': 'zV_Nj'})['aria-label']
        comments_count = reel.find('span', {'class': 'zV_Nj'}).find_next('span').text

        # Example: Extracting comments details
        comments = []
        comments_section = reel.find('div', {'class': 'EtaWk'})
        if comments_section:
            for comment in comments_section.find_all('li', {'class': 'gElp9'}):
                comment_content = comment.find('div', {'class': 'C4VMK'}).find('span').text
                timestamp = comment.find('time')['title']
                likes_on_comment = comment.find('button', {'class': 'FH9sR'}).text
                user_nickname = comment.find('a', {'class': 'sqdOP'}).text

                comments.append({
                    'content': comment_content,
                    'timestamp': timestamp,
                    'likes': likes_on_comment,
                    'user_nickname': user_nickname
                })

        reels_data.append({
            'video_link': video_link,
            'likes_count': likes_count,
            'shares_count': shares_count,
            'comments_count': comments_count,
            'comments': comments
        })

    return reels_data

def main():
    # Example usage
    username = 'slow_elvin'
    
    while True:
        reels_data = get_reels_data(username)
        # Send data to your backend here
        print(json.dumps(reels_data, indent=2))

        file = username + 'data' + '.json'

        with open(file, 'w') as f:
            data = json.dump(reels_data, f, indent=4)

        # Add a delay before making the next request to avoid being blocked
        time.sleep(10)

if __name__ == '__main__':
    main()
