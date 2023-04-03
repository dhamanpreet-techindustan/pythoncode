from github import Github

user = "dhamanpreet-techindustan"
password = "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"
g = Github(user,password)
repo = g.get_user().get_repo('pythoncode')
file_list = [
    '/home/dhaman/Documents'
]
file_name = [
    'gitpython,py'
]
commit_message = 'python commit'
master_ref = repo.get_git_ref('master')
master_sha = master_ref.oject.sha
base_tree = repo.get_git_tree(master_sha)

tree = repo.create_git_tree(base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)