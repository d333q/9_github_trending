import requests
import json
import pprint
from datetime import datetime, date, time, timedelta


def get_trending_repositories(top_size):
    info_repositories = []
    date_week_back = datetime.now() - timedelta(days=7)
    url = ('https://api.github.com/search/'
           'repositories?q=created:>={:%Y-%m-%d}&sort=stars'.format(date_week_back))
    list_trending_repositories = requests.get(url).json()
    for repository in list_trending_repositories['items'][0:top_size]:
        info_repositories.append({
                'name': repository.get('name'),
                'stargazers_count': repository.get('stargazers_count'),
                'open_issues_count': repository.get('open_issues_count'),
                'link': repository.get('html_url')})
    return info_repositories


def print_info_repositories(info_repositories):
    for repository in repositories:
        print('Name: {}, Star: {}, Open issues: {}, Link: {} '.format(
                    repository['name'],
                    repository['stargazers_count'],
                    repository['open_issues_count'],
                    repository['link']))


if __name__ == '__main__':
    repositories = get_trending_repositories(20)
    print_info_repositories(repositories)
