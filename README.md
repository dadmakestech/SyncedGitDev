# SyncedGitDev
Python script that can be used to pull all your repos automatically. put it as a daily scheduled activity on my windows machine to keep all my repos up to date without having to manually pull them.

# Usage:
python SyncedDev.py <targetdirectory> <repo1>,<repo2>,<repo3>,<repoN>

# Target Directory:
Directory where you want all repos to be Cloned to.

# Repo list:
List of repos to clone, if a repo already exists it will pull it down. If there are pending changes it should stash them prior to pulling latest.

# Pending work:
(1) options:
-s skip pulling if we are not in master branch
-d discard pending changes before pulling (as opposed to stashing)
(2) Provide a credential list. Right now it depends on you already having manually entered credentials for said REPO.
