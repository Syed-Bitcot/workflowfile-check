import os

print('-> Python script ran')  # This is just to verify if the script ran or not
print("Go"

a=False
# Simulate condition where GITHUB_ENV=true is appended to $GITHUB_ENV
with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
    env_file.write(f'GITHUB_ENV={a}\n')

# Uncomment this line to simulate the condition where GITHUB_ENV=false is appended to $GITHUB_ENV
# with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
#     env_file.write('GITHUB_ENV=false\n')
