# Vinyl Tracker

Search web for vinyl stock and cost and update DB accordingly.

# Discogs API

Discogs appears to be the place for music marketplace. Ebay seems good, but to my untrained eye, Discogs' listings appear to be more consistent and in line with market trends, or rather are the market trend setters. With Ebay it feels like more work would be needed to validate price: you got your biddings and auctions, you got your hopeful up-sellers and your desperate down-sellers.

So for the first shot I am going with with Discogs. It has a [community driven API](https://python3-discogs-client.readthedocs.io/en/latest/authentication.html) with a python package ready to be installed. That's neat! All I need to do is register myself and get a PAT for auth.
