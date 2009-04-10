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

def filtered_split(delimiter, s, **kw):
    '''
    Split string with delimiter but drop empty and blank parts.

    >>> filtered_split(',', '')
    []
    >>> filtered_split(',', 'A  , , B,C,')
    ['A', 'B', 'C']
    >>> filtered_split(',', 'A,B,C', filt=lambda s: s!='B')
    ['A', 'C']
    '''
    return filter(kw.get('filt'), [item.strip()
                                   for item in s.split(delimiter)])
