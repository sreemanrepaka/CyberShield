Cyberbullying project

Trained an ml model to detect cyberbullying in tweets

Made an api that responds to post requests and sends the data to the model, recieves the response ie cyberbullying or not and sends it back to the client

Made a chrome extension that takes in user input, sends a post request to aformentioned api and displays cyberbullying msg if data is cyberbullying.

Currently adding web scraping functionality to api so that stats of the current webpage can be displayed by chrome extension as bullying, not bullying etc.

Added a get request endpoint to the api such that upon receiving a get request by the extension, the api will scrape the tweets in the current site, do a post req to itself in order to pass those tweets to the model, get the result for every tweet and return results to client

Added another button to extension such that when the button is clicked, get request is sent to the api to the above endpoint and results are obtained.

Results are displayed as soon as the promise is resolved. No of total tweets, cyberbullying tweets and not cyberbullying tweets are counted and displayed accordingly.


