# Apply to Plaid via API

Plaid Inc. allows applicants to apply to jobs via API. I've heard this gives applicants an advantage over those who apply through HTML forms or email, which makes sense given they are an API company. 

## Usage

All you need to do is fill out the string fields at the bottom of `apply.py` and run `python3 apply.py` to send the application. 

## How It Works

The `apply_to_plaid` function assembles the string fields into JSON and sends it to Plaid using the `post_api` function, which creates a `POST` requrest to the URL specified by `BASE_URL`. 

If you're applying to Plaid, learn more about APIs [here](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces).