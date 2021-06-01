Scripts to migrate from Coppermine to Piwigo. Use at your own risk, always make backups.

It is assumed your Coppermine gallery has categories with 1 level of albums inside, no nested albums.
Names are cleaned as far as was necessary for me, you have to check for yourself if all your filenames are clean (see `$conf['sync_chars_regex']` in the local config) otherwise you might miss photos/albums.
I would recommend that you [allow spaces](https://piwigo.org/forum/viewtopic.php?id=21790) in Piwigo.

- Get the "albums" folder from Coppermine
- Make an empty directory "galleries"
- Put archive.php in your main Coppermine folder and run it by visiting yourgallery.com/archive.php
- This outputs a file called `photopaths.csv`, download it to the same location as the `albums` and `galleries` folders
- Run `python makedirstruct.py`, this will move the files from the `albums` folder to subfolders in the `galleries` folder according to the structure saved in `photopaths.csv`
- Upload the contents of the `galleries` folder to the `galleries` folder in your Piwigo installation
- Import the photos using `admin->photos->add->FTP + Synchronization`
