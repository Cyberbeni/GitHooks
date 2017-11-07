# How to use

Move the files to an appropriate place, create files with same name in the .git/hooks/ folder of your repositories and run these scripts from them (also change the path for the sorting python script in the pre-commit hook) and give them permission to execute with `chmod +x filename`
You can also directly copy them into yout .git/hooks/ folder if you are sure you won't need to add something to all of your repositories later.

# Useful links

http://schacon.github.io/git/githooks.html
http://githooks.com/
https://medium.com/beyond-the-manifesto/prepending-your-git-commit-messages-with-user-story-ids-3bfea00eab5a
http://mgrebenets.github.io/tools/2015/06/04/jira-id-in-git-commit-messages
https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/sort_simple_yaml.py
https://gist.github.com/marteinn/be178f437e17ade4a14aa838a07d95fa
https://github.com/square/spacecommander

# Other cool stuff you can try with git hooks

- Squash the branch and add the original commit hash "pre-rebase"
- Run tests in "post-update" and automatically open pull request (create a config file that tells the script whether you want to make a pull request after successful test and what should be the included message)
