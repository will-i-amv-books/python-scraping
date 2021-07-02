############################### 5-crawlSimilarPageTypes.py
# Import statements


class Website:
    """Common base class for all articles/pages"""
    def __init__(self, type, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        self.pageType = pageType

# Crawler definition
class Crawler:
    pass


# Crawler instantiation
