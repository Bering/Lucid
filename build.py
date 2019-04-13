import os
os.system("pyinstaller __main__.py -n LUCID -i public\\favicon.ico --hidden-import=bottle")

# TODO:
# * Copy the views and public folders
# * -i iconfile

# Nice to have:
# * Rename the folder in the dist folder
# * Zip the folder in the dist folder
# * Delete the build folder
# * Delete the __main__ folder from the dist folder (keep the zip)
# * Zip the source (exclude .git, pycache and dist folders)
# * Upload both zips to ringlogic.com
