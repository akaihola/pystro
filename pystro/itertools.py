def filtered_join(delimiter, *items, **kw):
    '''
    Join strings but drops empty and blank ones first.  You can also specify a
    custom filter with the `filt` keyword.  Drops None values before filtering.

    >>> filtered_join(', ', 'Only', '', 'three', ' \\t \\n ', 'items')
    'Only, three, items'
    >>> filtered_join(', ', 'A', 'B', 'C', filt=lambda s: s!='B')
    'A, C'
    '''
    return delimiter.join(
        filter(kw.get('filt'),
               [item.strip() for item in items if item is not None]))
