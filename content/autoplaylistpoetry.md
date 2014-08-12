Title: AutoPlaylistPoetry: a declaration of love to Spotify and Python
Date: 2014-08-12 23:00
Tags: python, spotify, flask, redis
Slug: autoplaylistpoetry

A while ago I decided to try and build a little app that makes use of Spotify's [Metadata API](https://developer.spotify.com/technologies/metadata-api/). At the time, I also started experimenting with Python, so I chose that as the language to build this experiment in.

I started out by building a simple command line app that served the aforementioned purpose. But as I progressed, I wanted to experiment with different technologies in different settings and eventually ended up with more than one application, which I will detail below. Both are written in Python.

The result is a this little (web)app automatically generates [Spotify](https://www.spotify.com) playlists based on a search query entered by the user. _Auto Playlist Poetry_ is a proof-of-concept that's inspired by [**Playlist Poetry**](http://playlistpoetry.com/), which in turn was based on [this Tumbler blog](http://spotifypoetry.tumblr.com/). The idea is that the user can provide a message and the application will use the Spotify Metadata API to find songs whose titles together make up the provided message. 

This blog post will detail what I built, what choices I made, what algorithm underlies the results, what technologies were used, etc.

### The goods and the code

If you don't care about the rest of this article (and I don't blame you), but just want try the app and/or get the code, look no further.

[**CLICK HERE FOR AUTOPLAYLISTPOETRY**](http://autoplaylistpoetry.com/)

[**CLICK HERE FOR THE CODE**](https://github.com/DandyDev/autoplaylistpoetry)

### Disclaimer

A few caveats (ok, excuses really :) ) before reading the rest of this blog post, looking at my code and testing out the applications:

* The time I was able to put into this project - and thus the scope - were limited. That means that, while I tried my best to squash any bugs I encountered, the applications may (probably will) still contain bugs. I am of course sorry for that!
* No Test-coverage whatsoever. You read that right. I know, it's a shame. I would have loved to provide tests for everything, but so far the time spent on this project was limited, and I consider this a proof-of-concept. Do know, that I am well aware of best practices in Software Engineering and that I normally go out of my way to provide decent test-coverage for the code I write. Tests are at the top of my TODO list for this project.
* The way playlists get generated is somewhat involved I haven't smoothed out the algorithm completely yet. This means that it will sometimes get caught in some kind of loop, making the web app hang. Shouldn't occur too often though. Solutions and better ideas are welcome!
* External dependencies may make these applications fail sometimes. [The Spotify Metadata API](https://developer.spotify.com/technologies/metadata-api/) was somewhat fickle, and would sometimes return either a undocumented HTTP 502 or 504 error. I haven't seen any odd behaviour since moving to the new [Web API](https://developer.spotify.com/web-api/) though.
* Python is relatively new to me: In my current job I mainly develop in Scala & Java. I've done some Python programming as a hobby for some time now, and I really love the language! But I'm sure many of my solutions are "un-pythonic". I especially was unsure about how to organize my code, coming from an environment where everything is a class, and almost every class has it's own file. So I don't really know which code to put in what module/package/class/etc. Any ideas, contributions, PRs are welcome!

### The applications and installation/usage instructions

I ended up building two implementations of the idea: a command line app and a web app. Both (can) use Redis for caching the API results for later reuse. In the command line app, using Redis is optional, the web app requires it. Aside from `redis`, two other external Python libraries are used: `requests` is used by both implementations for querying the Spotify Metadata API and `Flask` is used as a web framework in the web app.

To install the requirements, you can (assuming you have `pip` installed) do the following in your terminal: 

	pip install -r requirements.txt

If you only want to try out the command line app locally (which is easier), you could choose to only install `requests` and optionally `redis`.

#### The command line app

The command line app has two different modes of operation: one-off or interactive. The latter can be invoked by passing `-i` or `--interactive` as an argument on the command line. Review the help by running:

	./cli.py --help
	
To run it for one message:

	./cli.py -m "if i can't let it go out of my mind"

The app tries to be a good unix-citizen and as such only gives back the endresult, without outputting any other messages during it's runtime. It also gives back 0 on success and non-0 on failure. Should you need more verbosity, you can pass `-v`. Without it, you only get the URIs for the playlist entries (or optionally the URLs)

The interactive mode let's you type in messages on a prompt, and returns the result. It's straigtforward enough. In iteractive mode, the app, by default, uses an in-memory caching mechanism for storing API results for later reuse. Both interactive and one-off mode can also use Redis by providing the `-r` switch, with optionally a hostname, port and password. It requires Redis to be running of course.

#### The web app

To run the web app:

	python wsgi.py

The web application has a very simple interface which needs no further explanation. The application was built using [Flask](http://flask.pocoo.org/) and for the interface I used [Twitter Bootstrap](http://twitter.github.io/bootstrap/) (I know! just don't tell any designers…) The app uses Redis for caching API results for later reuse.

The web app also provides a very simple REST API. The endpoint resides at `/api/playlist` and requires a `message` to be passed in the query string. It gives back the result in JSON or returns an error in case something went wrong. It also tells you if the result is a complete playlist covering all the words, or if it's a partial result.

### The algorithm

When I started out, my first idea was to generate all possible ways the input message could be divided in different groups of words. I would then sort those combinations, favoring the groupings that were larger so the resulting playlist would be shorter. The next step would be to find the first combination that yielded results from the API for each group. After giving it some more thought however, I realized that with a growing message-size, the amount of combinations/groupings would grow exponentially. It has a space-complexity of O(c^n)

I stuck to the idea of starting out with word-groupings as large as possible, so the resulting playlist would be as short as possible (optimal solution). The resulting approach is basically as follows:

1. Filter any non-alphanumeric/non-space/non-apostrophe characters from the message
2. Break down the message into words
3. Break the resulting list into two halves, with the first half being max size minus one
4. Start searching for a song with a title equal to the words in the first half, _ignoring case_
5. If it isn't found, make the first half of the list one word smaller and look again
6. Repeat 5 until a match is found
7. Start at 3 again with the remainder of the list (so it kind of uses recursion)

If at some point a sublist is encountered for which none of the "slices" yield a result, the algorithm backtracks:

1. Take the previous successful match
2. subtract one word
3. continue processing as above

So if have the sentence "This is a painfully boring example message", which is currently divided as follows, where <> means they have already matched and [] is currently being processed: 

	[<this is>, <a painfully boring>, [example message]]

The backtracking algorithm will go back to the last match, "unmatch" it, subtract a word from it and continue processing:

	[<this is>, [a painfully], [boring example message]]

The middle group is now the group that is currently processed, the last group is the remainder of the message.

This algorithm is implemented as an iterator, through the `MessageChunker` class. It returns a smaller chunk at each call of `next()`. A chunk can be "accepted" through calling `progress()`. The `MessageChunker` class is used by the `PlaylistGenerator` class, which takes care of querying the API, optionally caching results. The main method of this class is `generate_playlist()` which takes a message and tries to generate a playlist. The method can also give back a partial result, if it can't wholly match the message, and it will tell the calling code as much.

#### Caching

Because calling the Spotify API is "expensive", and because the assignment mentioned reusing results, I implemented a caching mechanism. `PlaylistCache` is the Abstract Base Class that defines the contract. Tracks should be stored as key/value pairs where the _key_ is the title (in lowercase) and the _value_ is a PlaylistItem object. 

Currently two implementations are provided: a naive in-memory cache based on a simple dictionary holding the keys and values (`MemPlaylistCache`) and a cache using the Redis key-value store (`RedisPlaylistCache`). The command line app will use the former by default and can optionally use the latter. The web app only uses the latter.

As an extra caching step, the cachelayer stores the expiration time of the HTTP request, as returned by the Spotify API. If a PlaylistItem is retrieved from the cache, that has expired, the PlaylistGenerator will ask the API if it has been updated yet. If not, the API returns a 304 and the cached result is used. If it _is_ updated, the cache will be invalidated.

#### Parallelization

As said, calling the Spotify API is expensive. One solution is to divide the work to be handles by multiple threads. The algorithm I used, doesn't lend itself very well for this approach, because the remaining wordgroups to be queried, depend on the results of the current query. In my opinion, it would be a waste to start querying without knowing if we'd need the results. Besides, we'd probably hit the rate limit pretty quickly.

There is however a scenario where using multiple threads becomes benificial: When a message consists of multiple sentences, determined by the occurence of .!?/ When either application encounters a message made up of multiple sentences, it will offload the work to multiple threads. Those threads - implemented in `PLGeneratorThread` - take a message from the queue and process it. Order is preserved through passing consecutive numbers to the queue and sorting them back at the end.
The running time of the playlist generation, all but guarantees that no race conditions occur. Should one thread fail however, only a partial result is available.

### Future improvements

Some future improvements could include:

* (unit)tests
* Dealing with skipping words to improve results
* Guarantee a maximum running time by setting time-outs for example. Strive for best-effort. Running time should improve however, when caching is used and the app is used many time, filling said cache.

