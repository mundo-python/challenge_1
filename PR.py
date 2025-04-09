S C:\Users\gisel\desktop\challenge_1> git add challenge1.py
warning: in the working copy of 'challenge1.py', LF will be replaced by CRLF the next time Git touches it
PS C:\Users\gisel\desktop\challenge_1> git status
On branch cambios_en_read_me
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   challenge1.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

PS C:\Users\gisel\desktop\challenge_1> git commit m- "cambios en readme y agregar archivo en nueva branch"
error: pathspec 'm-' did not match any file(s) known to git
error: pathspec 'cambios en readme y agregar archivo en nueva branch' did not match any file(s) known to git
PS C:\Users\gisel\desktop\challenge_1> git commit -m "cambios en readme y archivo nuevo"
[cambios_en_read_me 80695c0] cambios en readme y archivo nuevo
 1 file changed, 20 insertions(+)
 create mode 100644 challenge1.py
PS C:\Users\gisel\desktop\challenge_1> git push origin cambios_en_read_me
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 536 bytes | 268.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/mundo-python/challenge_1
   22acf23..80695c0  cambios_en_read_me -> cambios_en_read_me
PS C:\Users\gisel\desktop\challenge_1>