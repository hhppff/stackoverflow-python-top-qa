import os


def travel_dir():
    links = [name for name in os.listdir('stackoverflow') if name.endswith('.md')]
    links.sort(key=lambda _: int(_.split('.')[0]))
    titles = []

    for link in links:
        with open('stackoverflow/' + link, encoding='utf-8') as f:
            titles.append(f.readline()[1:].strip())

    return titles, links

def write_summary():
    with open('SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write('# Summary\n\n')
        f.write('* [Introduction](README.md)\n\n')
        f.write('* StackOverflow\n')
        titles, links = travel_dir()
        for title, link in zip(titles, links):
            f.write('  * [%s](stackoverflow/%s)\n' % (title, link) )


if __name__ == '__main__':
    write_summary()
    
    
