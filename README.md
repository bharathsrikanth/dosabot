# dosabot
Where my dosa eaters at

Requires chromedriver (https://chromedriver.chromium.org/). Download the appropriate zip file, and then place the executable in the repo. .gitignore contains rules to ignore the Mac executable while committing.

Chromedriver may require permissions. Give appropriate permissions via chmod:

$ chmod 755 chromedriver

Besides, on some Macs, chromedriver won't run because it isn't from a trusted source. If this occurs, run the following command:

$ xattr -d com.apple.quarantine chromedriver
