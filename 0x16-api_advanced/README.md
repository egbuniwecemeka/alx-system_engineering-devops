# 0x16. API advanced

## API endpoint

- Listings: These are endpoints protocols for controlling pagination and filtering. These include the below 5 common parameters.

- **after** - specifies fullname of an item a in list to use as anchor point slice
- **before** - same as above
- **limit** - total number of items to return in the lists slice.
- **count** - number of items seen in the listing. In html, user uses it to assign value to befor and after in responses.
- **show**

Listings do not use page numbers. Use **before**, **after** and **count** to navigate pages.

## modhashes (required by reddit to prevent CSRF)

- can be obtained via */api/me.json*
- send modhash via X-Modhash custom HTTP header.

## fullnames

- fullname = thing's type + unique ID == global unique ID
- Syntax: type_prefix of object's type + objects uniqueID in base 3 eg t3_15bfi0
- t1 - Comment
- t2 - Account
- t3 - Link
- t4 - Message
- t5 - Subreddit
- t6 - Award

## response body encoding (For legacy reasons)

- <, > and & are placed by &lt, &gt and &amp. Add raw_json=1 parament to request to disable this.

## account

- GET api/v1/me/ - returns identity of user
- GET /api/v1/me/karma - Return breakdown of subreddit karma
- GET/api/v1/me/prefs - return list of comma-separated items
- PATCH api/v1/me/prefs - endpoint expects JSON of a particular format.
- GET api/v1/me/trophies - return list of trophy of current user
- /prefs/friends
- /prefs/blocked
- /prefs/messaging
- /prefs/trusted
- /api/v1/me/friends
- /api/v1/me/blocked
- GET /api/needs_captcha - check if ReCAPTCHAs are needed for API methods
