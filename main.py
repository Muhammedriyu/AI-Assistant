# AI-Assistant
About Jarvis - An Intelligent AI Consciousness 🧠 Jarvis is a voice commanding assistant service in Python 3.8 It can recognize human speech, talk to user and execute basic commands.  Requirements Operation system: Ubuntu 20.04 (Focal Fossa) Python Version: 3.8.x


Skip to content
ggeop
/
Python-ai-assistant

Type / to search

Code
Issues
22
Pull requests
11
Discussions
Actions
Projects
1
Wiki
Security
Insights
Owner avatar
Python-ai-assistant
Public
ggeop/Python-ai-assistant
 7 branches
 3 tags
Latest commit
@ggeop
ggeop Merge pull request #109 from ggeop/test_branch
…
2acc298
on Oct 12, 2021
Git stats
 647 commits
Files
Type
Name
Latest commit message
Commit time
.github
Create FUNDING.yml
4 years ago
bin
Remove merge feature branch to develop
2 years ago
config
Add Github release deployment
2 years ago
imgs
Add files via upload
2 years ago
src
Refactoring: Minor changes.
3 years ago
.gitattributes
Create git ignore.
4 years ago
.gitignore
Refactoring logs and naming.
3 years ago
.travis.yml
Remove merge feature branch to develop
2 years ago
LICENSE
Create LICENSE
4 years ago
README.md
Update README.md
2 years ago
requirements.txt
Reduce job execution time
2 years ago
run_jarvis.sh
AI updated readme.md
2 years ago
run_tests.sh
Create stages
2 years ago
setup.sh
Fix stages
2 years ago
README.md
CodeFactor Maintainability License: MIT Build Status

alt text

About Jarvis - An Intelligent AI Consciousness 🧠
Jarvis is a voice commanding assistant service in Python 3.8 It can recognize human speech, talk to user and execute basic commands.

Requirements
Operation system: Ubuntu 20.04 (Focal Fossa)
Python Version: 3.8.x
Assistant Skills
Opens a web page (e.g 'Jarvis open youtube')
Play music in Youtube (e.g 'Jarvis play mozart')
Increase/decrease the speakers master volume (also can set max/mute speakers volume) ** (e.g 'Jarvis volume up!')
Opens libreoffice suite applications (calc, writer, impress) (e.g 'Jarvis open calc')
Tells about something, by searching on the internet (e.g 'Jarvis tells me about oranges')
Tells the weather for a place (e.g 'Jarvis tell_the_skills me the weather in London')
Tells the current time and/or date (e.g 'Jarvis tell me time or date')
Set an alarm (e.g 'Jarvis create a new alarm')
Tells the internet speed (ping, uplink and downling) (e.g 'Jarvis tell_the_skills me the internet speed')
Tells the internet availability (e.g 'Jarvis is the internet connection ok?')
Tells the daily news (e.g 'Jarvis tell me today news')
Spells a word (e.g 'Jarvis spell me the word animal')
Creates a reminder (e.g 'Jarvis create a 10 minutes reminder')
Opens linux applications (e.g 'Jarvis open bash/firefox')
Tells everything it can do (e.g 'Jarvis tell me your skills or tell me what can you do')
Tells the current location (e.g 'Jarvis tell me your current location')
Tells how much memory consumes (e.g 'Jarvis tell me your memory consumption)
Tells users commands history (e.g 'Jarvis tell me my history')
Write/tell 'remember' and enable learning mode and add new responses on demand! (e.g 'Jarvis remember')
Clear bash console (e.g 'Jarvis clear console')
Has help command, which prints all the skills with their descriptions (e.g 'Jarvis help')
Do basic calculations (e.g 'Jarvis (5 + 6) * 8' or 'Jarvis one plus one')
Change settings on runtime (e.g 'Jarvis change settings')
Assistant Features
Asynchronous command execution & speech recognition and interpretation
Supports two different user input modes (text or speech), user can write or speek in the mic.
Answers in general questions (via call Wolfram API), e.g ('Jarvis tell me the highest building')
Change input mode on run time, triggered by a phrase e.g 'Jarvis change settings')
Easy voice-command customization
Configurable assistant name (e.g 'Jarvis', 'Sofia', 'John' etc.) (change on run time supported)
Log preview in console
Vocal or/and text response
Keeps commands history and learned skills in MongoDB.'
Getting Started
Create KEYs for third party APIs
Jarvis assistant uses third party APIs for speech recognition,web information search, weather forecasting etc. All the following APIs have free no-commercial API calls. Subscribe to the following APIs in order to take FREE access KEYs.

OpenWeatherMap: API for weather forecast.
WolframAlpha: API for answer questions.
IPSTACK: API for current location.
Setup Jarvis in Ubuntu/Debian system
Download the Jarvis repo locally:
git clone https://github.com/ggeop/Jarvis.git --branch master
For Contribution:

git clone https://github.com/ggeop/Jarvis.git --branch develop
Change working directory
cd Jarvis
Setup Jarvis and system dependencies:
bash setup.sh
Put the Keys in settings
NOTE: For better exprerience, before you start the application you can put the free KEYs in the settings.py

nano Jarvis/src/jarvis/jarvis/setting.py
Start voice commanding assistant
alt text

Start the assistant service:
bash run_jarvis.sh
How to add a new Skill to assistant
You can easily add a new skill in two steps.

Create a new configurationin SKILLS in skills/registry.py
{ 
  'enable': True,
  'func': Skills.new_skill,
  'tags': 'tag1, tag2',
  'description': 'skill description..'
}               
Create a new skill module in skills/collection
Desicion Model
alt text

Extract skill
The skill extraction implement in a matrix of TF-IDF features for each skill. In the following example he have a dimensional space with three skills. The user input analyzed in this space and by using a similarity metric (e.g cosine) we find the most similar skill. alt text

Contributing
Pull Requests (PRs) are welcome ☺️
The process for contribution is the following:
Clone the project
Checkout develop branch and create a feature branch e.g feature_branch
Open a PR to develop
Wait for review and approval !!
master branch update and release is automated via Travis CI/CD
Try to follow PEP-8 guidelines and add useful comments!
CI/CD Flow
alt text

About
Python AI assistant 🧠

Topics
python nlp ai mongodb sklearn pymongo voice-commands voice-recognition nltk voice-chat voice-control python35 nlp-machine-learning wolfram-language voice-assistant google-speech-recognition voice-activity-detection voice-recognition-experiment google-speech-to-text linux-assistant
Resources
 Readme
License
 MIT license
 Activity
Stars
 710 stars
Watchers
 42 watching
Forks
 207 forks
Report repository
Releases 3
Release_v.303
Latest
on Oct 12, 2021
+ 2 releases
Sponsor this project
Packages
No packages published
Contributors
8
@ggeop
@dependabot[bot]
@89Q12
@anujdube12
@szenekonzept
@snehkhajanchi
@vipul-sharma20
@codacy-badger
Languages
Python
95.2%
 
Shell
4.8%
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
⚛
