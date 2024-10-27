
def parse_date(date_str: str) -> datetime:
    date_formats = [
        '%m/%d/%Y', '%m-%d-%Y', '%m/%d/%y', '%m-%d-%y',
        '%d %B %Y', '%d %b %Y', '%B %d, %Y', '%b %d, %Y',
        '%Y-%m-%d'
    ]
    
    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            pass
    
    return None
