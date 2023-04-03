from git import Repo
import os

# token = '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'
# g = Github(token)

file_list=os.listdir("/home/dhaman/Documents")
print (file_list)
repo_dir = "/home/dhaman/Documents/"
# for i in file_list:
print(repo_dir) 
# file_list1=os.listdir(repo_dir)
repo = Repo(repo_dir)
# file_list = ['folder2','folder3','folder4']
commit_message = 'updates'
# repo.index.add(file_list1)
repo.git.add(all = True)
repo.index.commit(commit_message)
# repo_name = input("give name of repo")
origin = repo.remote('origin')
# origin.push()
repo.git.push('origin', 'master')
    