import os


def git_data():
    return {
        b"gitusername": os.popen("git config user.name").read().strip().encode(),
        b"gitemail": os.popen("git config user.email").read().strip().encode(),
        #        "gitrepo": os.popen("git remote get-url origin").read().strip().rsplit(".",1)[0]
    }


d = git_data()
scaffer_out.update(d)

scaffer_out[b"libname"] = os.path.basename(os.getcwd()).encode()
