import praw

reddit = praw.Reddit('bot1') #bot1 in praw.ini file. (SC91)
subreddit = reddit.subreddit('AskReddit')

for submission in subreddit.stream.submissions():
    if len(submission.title.split()) > 50:

    questions = ['what is', 'who is', 'what are']
    normalized_title = submission.title.lower()

    for question_phrase in questions:
        if question_phrase in normalized_title:
