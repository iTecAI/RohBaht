# RohBaht
A discord chatbot. That attempts to be human by storing massive wodges of data. Hooray!

Basically all you need to do is to open RohR#.#.py and change the values in the o class to custom ones.

Value reference:
- mode: The running mode of Roh. "interact" puts roh into the python shell, "discord" puts roh on discord, and "compile" creates a new corpus from every server you are a part of.
- locs: Channel ids for roh to run in. Get these by turning on developer mode in discord, right-clicking a channel, and clicking copy id.
- creds: Enter login credentials for roh to use when compiling and running on discord. These must be your account creds, not a token.
- corploc: Folder in /corpora/ to load or compile into. Keep this at 1 (if u use the full install)
- names: a list of names for roh to respond to
- bye: Roh will pick randomly from this list when it leaves a conversation
