from twython import Twython;

APP_KEY = 'k08TTiz73ZvuojkwFEQkpLEYg'
APP_SECRET = 'Cw8s6lDHwwIdADA6iyrgttNflnGqfqRItxUyFD5Ol371Iw328Q'

twitter = Twython(APP_KEY,APP_SECRET);
#ACCESS_TOKEN = twitter.obtain_access_token();

#twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
twitter.search(q='#TakeAKnee')



auth = twitter.get_authentication_tokens();

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print(auth['auth_url'])

# I manually open this url in the browers and
# set oaut_verifier to the value like seen below.

oauth_verifier = input('Enter your pin:')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

FINAL_OAUTH_TOKEN = final_step['oauth_token']
FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

print(twitter.verify_credentials())

twitter.get_home_timeline()