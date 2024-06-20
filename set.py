import os

print('-> Python script ran')  # This is just to verify if the script ran or not

# Simulate condition where name=true is appended to $GITHUB_ENV
os.system('echo "name=true" >> $GITHUB_ENV')

# Uncomment this line to simulate the condition where name=true is not appended to $GITHUB_ENV
# os.system('echo "name=false" >> $GITHUB_ENV')
