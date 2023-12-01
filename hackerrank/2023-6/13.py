import re


def main():
    n = int(input())
    html = [input() for _ in range(n)]

    ans = find(html)
    print(ans)


def find(html):
    domains = set()
    for line in html:
        urls = re.findall('https?://[^\s<>"]+|www\.[^\s<>"]+', line)
        for url in urls:
            url = url.split('?')[0]  # Remove parameters
            domain = re.search('https?://([^/]+)', url)
            if domain:
                domain = domain.group(1)
                domain = re.sub('^www\.|^ww2\.', '', domain)
                domains.add(domain)
    return ';'.join(sorted(domains))


if __name__ == '__main__': main()
