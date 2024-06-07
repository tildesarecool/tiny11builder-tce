# Tiny11Builder - TCE

Scripts to build a trimmed-down Windows 11 image - now in...Python?

Below I have something of development log (in case you have a need to read boring stuff).
<p>

As implied by above, this is a fork of [Tiny11 by ntdevlabs](https://github.com/ntdevlabs/tiny11builder), a PowerShell script to remove certain components from a Windows 10/11 install source. But I don't think I'll be doing any pull requests. 

</p>

<p>

Just so there's no confusion here, I don't think this will ever replace the PS version of this script. And there's no reason to write this in Python given the advantages of using PS for the purpose. This is more of an exercise than anything else.

Also, One of the main motivations for wanting to re-write this (besides Python practice) is the amount time it takes to generate the new ISO (I'm hoping I can improve on the time required). I am also working on much more communications with the user. 

I might actually come back and re-write it using actually PS too. Or you know re-write my Python script based on a PS script...in PS.

</p>

<p>
Since I've been working on Python recently I wanted to see if I could recreate the functionality using Python. 
</p>
<p>
I haven't dissected the PS script yet but I should be able to support Windows 10 and 11 and any architecture (though since I don't care about ARM that will be at the bottom of the priority list).
</p>
<p>
One possible disadvantage of using this version is needing an install of Python (I wasn't planning to convert to exe).
</p>
<p>

I'm not sure yet if I'll utilize the same approach to creating a bootable ISO using oscdimg but I likely will not be able to get around using DISM. I will use the included unattend file at as a base for my own - I happen to have my own unattend files and want to skip a lot more things (like UELA agreement checkbox, keyboard language/layout and OS language).
</p>
<p>
Like the original, this is open-source, **so feel free to add or remove anything you want!** Feedback is also much appreciated.
</p>
<p>

It's too soon to say if I'll try to also reproduce  **tiny11 core builder**.  I will have to save that for last and deicied if it's worthwhile.
</p>

Instructions:

1. Download Windows 11 from the Microsoft website (<https://www.microsoft.com/software-download/windows11>)
2. Mount the downloaded ISO image using Windows Explorer.
3. (This step will be replaced/TBD)
4. Select the SKU that you want the image to be based: I'll replace the UI/presentation of this step
5. Sit back and relax :)
6. Re-building an ISO takes too long. I really hope I can improve this. 

What is removed (TBD):

- Clipchamp
- News
- Weather
- Xbox (although Xbox Identity provider is still here, so it should be possible to be reinstalled with no issues)
- GetHelp
- GetStarted
- Office Hub
- Solitaire
- PeopleApp
- PowerAutomate
- ToDo
- Alarms
- Mail and Calendar
- Feedback Hub
- Maps
- Sound Recorder
- Your Phone
- Media Player
- QuickAssist
- Internet Explorer
- Tablet PC Math
- Edge
- OneDrive

For tiny11 core (TBD):

Known issues:

TBD

Features to be implemented:

- option to import a custom hosts file?
- maybe a GUI? A TUI?
- Autounattend.xml selection/generation?
- Save settings as profile and select that for later? 
- Settings saved to JSON file?
- Error handling?
- I could offer to make Win 11 skip CPU etc checks. This might be too complicated. 

<p>

### Prior to June 6th 2024

I started breaking out the different sections into functions. The PS original is just one giant long block of code with very few breaks. I wanted to put it into sections to make it easier to read as well easier to debug later. I didn't get very far in, just barely started.

I'm doing this Python re-write in the worst way possible: just writing functions as I read the code. What I should do is re-organize the PS script to have spacing between different sections, summarize the functionality and then list out what I'm going to write step-by-step before I even written one line of Python. But instead I'm writing a Python version as I read a section of PS script. 

This why I wrote that get_processor_architecture() function already even though I have no idea where or if it will be needed later on. I also did it via environment variable like the PS script did even though that's likely not necessary.

I have already come with some improvements, though: instead of simply creating an arbibrary folder on the root of the user's C: drive I ask the user if they'd like to specify a working directory and mention the path that can be used by default if none is specified. This just seems more elegant and considerate of the user. I even do some input validation and offer suggestions if a path comes back invalid. I'm going to come back to that later but I already like it more than before.  

The next problem I had with the PS version was the script only except a drive letter (with no colon) for the Windows install source. I mean when I used this PS script I actually used a really old DOS command called SUBST so I could use a subdirectory as the source rather than actually mounting an ISO. I mean it just copies the contents some place else anyway I don't think I really that made the process better. But my script will let the user specify either a drive letter OR a folder some place on the PC.  This functionality doesn't work all the way quite yet but will by the time the script is done.

<hr>

### 7 June 2024

So far I've learned that the scratch directory is actually the location in the filesystem the the WIM file is mounted.

Since I defaulted this directory to %USERPROFILE%\documents\tiny11 that is where the WIM filesystem will be located.  I also realized the script converts an install.ESD file to a WIM file. Might explain some of the time it takes to run. 
 
I've made a few edits but mostly researched a possible solution to one of the script's operations taking a really long time. Which I'll do in the most needlessly complicated way possible (you're welcome). It invovles MemoryFS, tmpfile and symbolic links. I'll probably do some benchmarks to prove the feasibility before really adding it in. Or add it in anyway because hilarious. 


</p>