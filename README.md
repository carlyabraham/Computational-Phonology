# Computational-Phonology
scripts relating to compphon - both assignments for the NYU graduate course (LING-GA 1230) and otherwise

## italian_broad_transcription.py
Assignment for LING-GA 1230. Performs a broad transcription of Italian text to IPA. The alternations that are handled are documented in the comments of the script. I used regexs to catch the different environments and rules, and re.sub() to replace the IPA symbols (in unicode). Honestly, there are still some issues (like word-initial s being realized as [z]), and I may get back to fixing it, may not ¯\_(ツ)_/¯. 

#### To run:
* Save file locally
* Have the Italian that you want transcribed saved in the same directory as a .txt file. 
* Run 
```
python stressot-makeinput.py
```
* You will be prompted to give the file name of the Italian .txt file. Just type the file name (WITHOUT ".txt" at the end) and press "Enter."
* The transcribed text will be in that directory as <filename>_ipa.txt
