# TODO - make download async so you can report progress!

import sys
import os

# Input Arguments:
#   Repo Directory - string - location to clone and synchronize provided git repositories
#   Repos - url1,url2,... - list of repositories you wish to clone and keep up to date with master branch.

def clone(repo_url):
    result = os.system("git clone " + repo_url + " --recurse-submodules")
    return result == 0

def pull(repo_url):
    result = os.system("git pull " + repo_url)
    print("pull result=" + str(result))
    return result == 0

def extract_repo_name(repo_url):
    parts = repo_url.split("/")
    return parts[len(parts)-1]

def stash():
    return os.system("git stash --all") == 0

# Validate inputs were provided
if len(sys.argv) != 3:
    raise Exception("Please provide repo directory and list of repos.")

# Grab inputs from command line.
directory = sys.argv[1]
url_list = sys.argv[2].split(',')

# Create provided directory if it doesn't exist
if not os.path.exists(directory):
    os.mkdir(directory)


# TODO option: stash changes and pull? or leave?

# TODO option: don't pull if not in master? (currently "working")

os.chdir(directory)
# TODO this won't work if there are different creds for each would it?
for url in url_list:
    if os.path.exists(extract_repo_name(url)):
        print("repo already existed, let's update!")
        # Enter existing repo folder
        os.chdir(extract_repo_name(url))
        print("Changed WD to: " + os.getcwd())
        # Save off any pending changes
        stash()
        # Pull latest (do we need to provide branch?)
        pull(url)
        # Return to directory of repos
        os.chdir(directory)
    else:
        # Clone for the first time.
        clone(url)
