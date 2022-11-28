from urllib.parse import urlsplit, urlunsplit


def xpath_or_css(response, selector, add='text'):
    attr_name_to_scrape = add
    if selector.startswith('./'):
        selector = selector[1:]
    if selector.startswith('/'):
        if attr_name_to_scrape == 'text':
            selector += '/text()[normalize-space()]'
        else:
            selector += f'/@{attr_name_to_scrape}'

        # Add a '.' in front of the xpath selector, otherwise the iteration will only return the first iter
        return response.xpath(f'.{selector}').get()
    else:
        selector += f'::{attr_name_to_scrape}'
        return response.css(selector).get()


def get_base_url(url, urltype='std'):
    split_url = urlsplit(url)
    if urltype == 'std':
        return urlunsplit((split_url[0],split_url[1],split_url[2].replace('1', '{}'), '',''))
    return urlunsplit((split_url[0], split_url[1], '', '', ''))
