def convert(url):
    """Convert url to http:// if not present."""
    if not url.startswith('http'):
        url = 'http://' + url
    return url


def tagList():
    """List of tags to be extracted."""
    return [
        'description',
        'keywords',
        'language',
        'author',
        'publisher',
        'revisit-after',
        'expires',
        'last-modified',
        'url',
        'content-language',
        'content-type',
        'content-encoding',
        # FACEBOOK
        'og:title',
        'og:description',
        'og:image',
        'og:url',
        'og:site_name',
        'og:type',
        # TWITTER
        'twitter:card',
        'twitter:site',
        'twitter:title',
        'twitter:description',
        'twitter:image',
        'twitter:url',
        'twitter:creator',
        'twitter:site',
        'twitter:domain',
        # BASIC
        'generator',
        'application-name',

    ]
