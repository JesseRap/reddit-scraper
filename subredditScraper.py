import praw, pprint, time, codecs, datetime

user = 'python comments experiment (by u/Spinozism)'

def scrapeComments2(subreddit, startID=None):
    # Scrapes all available comments from r/subreddit/comments (~ 1000)

    count = 0
    n=0
    lastPostID = ''
    if startID == None:
        suffix = ''
    else:
        suffix = 't1_'+startID
    url = 'https://www.reddit.com/r/'+subreddit+'/comments.json'
    docname = subreddit+'Comments.py'

    

    while True:
        r = praw.Reddit(user_agent=user)
        posts = r.get_content(url, params={'after': suffix}, limit=100)

        try:
            post = next(posts)
            suffix = 't1_' + post.id
            lastPostID = post.id
            #postList.append(post.body)
            #oldposts.append(post.id)
            with open(docname,'a', encoding='utf-8') as f:
                f.write(post.body)
                f.write('\n')
            count += 1
        except StopIteration:
            print("STOP")
            print(count)
            break

        for post in posts:
            #postList.append(post.body)
            lastPostID = post.id
            #print(post.id)
            #print(post.body)
            suffix = 't1_' + post.id
            with open(docname,'a', encoding='utf-8') as f:
                f.write(post.body)
                f.write('\n')
            count += 1
            print(count)
            if count % 50 == 0:
                time.sleep(2)
            if count % 100 == 0:
                print(lastPostID, post.created, post.body)

    return lastPostID

def scrapeComments(subreddit, startID=None):

    count = 0
    lastSubmissionID = ''
    if startID == None:
        suffix = ''
    else:
        suffix = 't1_'+startID
    url = 'https://www.reddit.com/r/'+subreddit+'/comments.json'
    docname = subreddit+'Comments.py'

    r = praw.Reddit(user_agent='philosophy comments experiment')

    subreddit = r.get_subreddit(subreddit)

    #comments = subreddit.get_comments(sort=u'new', time=u'all', limit=None,
                                      #params={'after':'t1_cytalui'})

    submissions = subreddit.get_new(limit=None, params={'after':'t3_4s85q4'})

    """
    se = r.search('after=2u0upv',subreddit,
                  syntax='cloudsearch')
    """
    
    for s in submissions:
        print(s.created_utc)
        print(datetime.datetime.fromtimestamp(int(s.created_utc)))
        print('submission ID', s.id)
        print('submission: ',s)
        #s.replace_more_comments()
        comments = s.comments
        #comments.replace_more_comments()
        commentsFlat = praw.helpers.flatten_tree(comments)
        for c in commentsFlat:
            print(c.created_utc)
            print(datetime.datetime.fromtimestamp(int(c.created_utc)))
            print(c)
            time.sleep(2)
    
    
    """
    submissions = praw.helpers.submissions_between(r, 'academicphilosophy',
                                                   lowest_timestamp=None,
                                                   highest_timestamp=None,
                                                   newest_first=True)
    
    for s in submissions:
        print(s)
        comments = s.comments
        flatComments = praw.helpers.flatten_tree(comments)
        for c in flatComments:
            print(c)
            print(datetime.datetime.fromtimestamp(int(c.created_utc)))
    """
    #n=0
    #for comment in comments:
        #n += 1
        #print(n, comment.id)
        #print(comment.id)
        #print(comment.body)
    #comments = subreddit.get_comments()
    #flatComments = praw.helpers.flatten_tree(comments)

    #for comment in flatComments:
    #    (print(comment))

    #print(next(subreddit))

    return


    
    """
    while True:
        r = praw.Reddit(user_agent='philosophy comments')
        posts = r.get_content(url, params={'after': suffix}, limit=100)

        try:
            post = next(posts)
            suffix = 't1_' + post.id
            lastPostID = post.id
            #postList.append(post.body)
            #oldposts.append(post.id)
            with open(docname,'a', encoding='utf-8') as f:
                f.write(post.body)
                f.write('\n')
            count += 1
        except StopIteration:
            print("STOP")
            print(count)
            break

        for post in posts:
            #postList.append(post.body)
            lastPostID = post.id
            #print(post.id)
            #print(post.body)
            suffix = 't1_' + post.id
            with open(docname,'a', encoding='utf-8') as f:
                f.write(post.body)
                f.write('\n')
            count += 1
            print(count)
            if count % 50 == 0:
                time.sleep(2)
            if count % 100 == 0:
                print(lastPostID, post.created, post.body)
    """
    #return lastSubmissionID

#print(scrapeComments('academicphilosophy'))

r  = praw.Reddit(user_agent=user)

def getAllSubmissionComments(session, submissionID):
    result = []
    submission = session.get_submission(submission_id=submissionID)
    result.append(str(submission.id))
    result.append(str(datetime.datetime.fromtimestamp(submission.created_utc)))
    result.append(submission.fullname)
    """"""
    extra = submission.replace_more_comments(limit=None)
    print(len(extra))
    while len(extra) != 0:
        extra = submission.replace_more_comments(limit=None)
        print('len(extra) = ',len(extra))
    """"""
    comments = praw.helpers.flatten_tree(submission.comments)
    n=0
    for c in comments:
        print(n)
        result.append(c)
        print(c)
        with open('commentScrapeTest.txt', 'a') as f:
            f.write(str(c.id)+' '+str(datetime.datetime.fromtimestamp(c.created_utc))+' '+str(c)+'\n')
        time.sleep(2)
        n+=1

    print(len(result))
    """
    with open('commentScrapeTest2.txt', 'w') as f:
        f.write(result)
    return result
    """

getAllSubmissionComments(r, '4sad2f')

"""
with open('commentScrapeTest.txt','w') as f:
    for comment in getAllSubmissionComments(r, '4sad2f'):
        f.write(comment)
"""    
"""
#sub1 = r.get_submission(url='https://www.reddit.com/r/technology/comments/4sajo0/pok%C3%A9mon_gos_success_adds_75_billion_to_nintendos/')
sub1 = r.get_submission(submission_id='4sajo0')
print("1")
#extra = sub1.replace_more_comments(limit=10)
print("2")
comments = praw.helpers.flatten_tree(sub1.comments)
print("3")
n=1
for c in comments:
    print(n)
    print(c)
    n+=1
"""

