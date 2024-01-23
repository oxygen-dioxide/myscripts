import pathlib
from github import Auth

def login() -> Auth.Token:
    folder = pathlib.Path(__file__).resolve().parent
    token_file = folder / "github_token.txt"
    if(not token_file.exists()):
        print(f"Please create a file '{token_file}' with your github token.")
        input()
        exit(1)
    with open(token_file, "r") as f:
        token = f.read().strip()
    auth = Auth.Token(token)
    return auth

def repo_name(inp:str) -> str:
    #grab github repo name from github url, like https://github.com/stakira/OpenUtau.git to stakira/OpenUtau
    inp = inp.strip()
    if(inp.endswith(".git")):
        inp = inp[:-4]
    if(inp.startswith("https://github.com/")):
        inp = inp[19:]
    elif(inp.startswith("github.com/")):
        inp = inp[11:]
    return inp