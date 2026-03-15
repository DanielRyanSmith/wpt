#!/usr/bin/env python3
import sys
import urllib.request
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

try:
    from bs4 import BeautifulSoup
    import markdownify
except ImportError:
    print("ERROR: Missing required packages. The agent should run: pip install beautifulsoup4 lxml markdownify")
    sys.exit(1)

def fetch_and_extract_text(url: str) -> str | None:
    """
    Fetches the HTML content from a URL and extracts the core textual content,
    stripping away navigation, footers, and boilerplate.
    Returns the content formatted as Markdown.
    """
    logger.info(f'Fetching content from: {url}')

    try:
        # Set User-Agent to bypass generic bot filters and identify our crawler
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0 (compatible; WPT-Gen/1.0)'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        logger.error(f'Failed to download HTML from {url}: {e}')
        return None

    # Use lxml if available, fallback to html.parser
    try:
        soup = BeautifulSoup(html, 'lxml')
    except Exception:
        soup = BeautifulSoup(html, 'html.parser')

    # Strip out boilerplate that isn't spec content
    for element in soup(['nav', 'script', 'style', 'footer', 'head', 'link', 'meta', 'noscript']):
        element.extract()

    # Find the main content area. Specs usually use <main>, <div class="main">, or just body
    main_content = soup.find('main') or soup.find('div', class_='main') or soup.find('body')

    if not main_content:
        logger.warning(f'Could not find main content block in {url}')
        return None

    # Pre-process <a> tags to preserve internal specification links (fragments)
    # but strip external URLs to conserve token limits.
    for a_tag in main_content.find_all('a'):
        href = a_tag.get('href')
        if not isinstance(href, str) or not href.startswith('#'):
            a_tag.unwrap()

    # Convert the HTML tree to markdown, omitting external link URLs to save token space
    content = markdownify.markdownify(
        str(main_content),
        heading_style='ATX',
        strip=['img', 'picture', 'video', 'audio', 'iframe'],
    )

    content = content.strip()
    if not content:
        logger.warning(f'Could not extract meaningful text from {url}')
        return None

    return content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_spec.py <url>")
        sys.exit(1)
        
    url = sys.argv[1]
    markdown_content = fetch_and_extract_text(url)
    
    if markdown_content:
        print("\n--- SPECIFICATION CONTENT ---\n")
        print(markdown_content)
        print("\n--- END SPECIFICATION CONTENT ---\n")
    else:
        sys.exit(1)
