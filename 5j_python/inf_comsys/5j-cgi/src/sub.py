import subprocess

run_server = subprocess.call(["python", "-m", "http.server", "--cgi", "8080"])