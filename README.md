# PottyMouthBot

PottyMouthBot is a [Discord](http://discord.com) bot for filtering out bad words from your server.          
The bot operates by searching all incoming messages for bad words found in `src/trie/words.txt`. It also searches for multiple [leetspeak](https://www.howtogeek.com/443390/what-is-leet-speak-and-how-do-you-use-it/) versions of those words as well.             
 If a bad word is detected by the bot, it will delete the offending message, and then warn the user using a random shame message. 
                 
                          
                        
 ### Installation
 To install the bot, you must be an administrator/owner of the Discord server.            
 Simply [click the following link]( https://discord.com/api/oauth2/authorize?client_id=756276859225768057&permissions=8192&scope=bot) and choose which server to install it to.
 FYI: The bot requires that the `Manage Messages` permission to delete messages. 
 
 ### Bugs/Requests
 If you have any requests or bugs to report, feel free to report an [issue here](https://github.com/nldoty/PottyMouthBot/issues).