# Tiny11Builder - TCE

Scripts to build a trimmed-down Windows 11 image - now in...Python?
<p>

As implied by above, this is a fork of [Tiny11 by ntdevlabs](https://github.com/ntdevlabs/tiny11builder). But I don't think I'll be doing any pull requests. 

</p>

<p>

Just so there's no confusion here, I don't think this will ever replace the PS version of this script. And there's no reason to write this in Python given the advantages of using PS for the purpose. This is more of an exercise than anything else.

Also, One of the main motivations for wanting to re-write this (besides Python practice) is the amount time it takes to generate the new ISO.

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
- Error handling?

