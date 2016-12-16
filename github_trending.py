import requests
import json
from datetime import datetime, date, time, timedelta


def get_trending_repositories():
    date_week_back = datetime.now() - timedelta(days=7)
    payload = {
        'q': ('created:>={:%Y-%m-%d}'.format(date_week_back)), 'sort': 'stars'}
    list_trending_repositories = requests.get(
        'https://api.github.com/search/repositories', params=payload).json()
    return list_trending_repositories


def print_info_repositories(list_trending_repositories, top_size):
    for repository in list_trending_repositories['items'][0:top_size]:
        print('Name: {}, Star: {}, Open issues: {}, Link: {} '.format(
                    repository.get('name'),
                    repository.get('stargazers_count'),
                    repository.get('open_issues_count'),
                    repository.get('html_url')))


if __name__ == '__main__':
    amount_show_repositories = 20
    repositories = get_trending_repositories()
    print_info_repositories(repositories, amount_show_repositories)
