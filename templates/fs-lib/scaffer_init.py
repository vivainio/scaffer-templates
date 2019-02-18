import os

print("hello from scaffer init")
print(scaffer_in)

print(scaffer_out)

def git_data():
    return {
        "gitusername": os.popen("git config user.name").read().strip(),
        "gitemail": os.popen("git config user.email").read().strip(),
        "gitrepo": os.popen("git remote get-url origin").read().strip().rsplit(".",1)[0]
    }

d = git_data()
scaffer_out.update(d)


