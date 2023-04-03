from github import Github

repo_dir = '/home/dhaman/Documents/'
repo = repo_dir(repo_dir)
file_list =[
    '/home/dhaman/Documents/python.py'
]
commit_massage = 'add new pyhton file'
repo.index.add(file_list)
repo.index.commit(commit_massage)
origin = repo.remote('origin')
origin.push()