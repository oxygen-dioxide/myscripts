from github import Github
from github import Auth
import github_utils
from datetime import datetime
from typing import List, Tuple
from py_linq import Enumerable
from typing import List, Tuple

print("This script will plot the number of open pull requests over time.")

# using an access token
auth = github_utils.login()
# Public Web Github
g = Github(auth=auth)

repo_name = github_utils.repo_name(input("Repo name or url: "))
print("Repo:", repo_name)
repo = g.get_repo(repo_name)

print("getting open pulls")
open_pulls = list(repo.get_pulls(state='open', sort='created', base='master'))
print("getting closed pulls")
closed_pulls = list(repo.get_pulls(state='closed', sort='created', base='master'))
print("finished getting pulls")

#Openings and Closings of pull requests. (datetime, 1 for opening or -1 for closing)
pull_events:List[Tuple[datetime, int]] = []
for repo in open_pulls + closed_pulls:
    pull_events.append((repo.created_at, +1))
    if(repo.closed_at != None):
        pull_events.append((repo.closed_at, -1))
pull_events.sort()

pull_curve_x:List[datetime] = Enumerable(pull_events).select(lambda x:x[0]).to_list()
pull_curve_y:List[int] = []
pullnum = 0
for pull_event in pull_events:
    pullnum += pull_event[-1]
    pull_curve_y.append(pullnum)

from matplotlib import pyplot as plt
from datetime import datetime
plt.plot(pull_curve_x, pull_curve_y)
plt.show()