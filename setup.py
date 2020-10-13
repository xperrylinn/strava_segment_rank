from distutils.core import setup

setup(
    name='strava segment rank',
    version='1.0',
    description='Strava segment leaderboard scraper',
    author='Xavier Linn',
    author_email='xavierperrylinn@gmail.com',
    url='https://github.com/xperrylinn/strava_segment_rank',
    packages=[
        'pandas',
        'stravaio',
        'selenium'
    ],
)
