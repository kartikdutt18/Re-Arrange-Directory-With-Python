# Re-Arrange-Directory-With-Python

Use this really cool (really simple) script to re-arrange your directory.Put stuff into folders based on their name or type. Beautifully organize your directory by creating a folder for every cool anime / movie you watch or document that you read.

## Why I did this?
If you download tons of anime or series, then your download folder is messy with sequels / episodes scattered all over the place. Recently, I downoaded about 70 or so videos of different animes and I didn't want to drag them into folders even though I can droup a bunch together.

## Solution
This script will explore all folder, sub-folders and sub-sub-sub----folders (I think you got the idea :wink:) and find all files matching the description.

### Hold up, What's a description?
Well, a description is something we use to identify files. Look at the example below :

These are the parameters and their explanations :
```
Base Path : Path in which will cover all folders and files (in it).
Substrings : Set of substrings which will be looked for in a file.
            It's case insensitive.
            Also, it will work if there are other characters between the substrings in file name.
            If you enter '*', you will be matching only the type.
Match All : Do you want to match all substrings or is it sufficient to match to any one.
Destination Path : A path which may be created if needed where are matched files will be transfered.
Type : Type of files maybe all, text, video, images or music. We will transfer pretty much any popular extention.
       Don't find the one you are looking for, Open a PR or an issue.
```
## Hope you have fun satisfying some of your OCD :slightly_smiling_face:
