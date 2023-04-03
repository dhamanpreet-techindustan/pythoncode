from github import Github

user = "dhamanpreet-techindustan"
password = "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"
g = Github(password)
repo = g.get_user().get_repo('pythoncode')
file_list = [
    '/home/dhaman/Documents/gitpython.py'
]
file_name = [
    'gitpython,py'
]
commit_message = 'python commit'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

tree = repo.create_git_tree(base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)