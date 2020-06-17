from bs4 import BeautifulSoup
html_doc = """
<body>
    <div class="my_par">
        <h5>你媽啦</h5>
        <p class="my_par">
            <h5>操你媽</h5>
            <a id="link1" href="/my_link1">Link 1</a>
            <a id="link2" href="/my_link2">Link 2</a>
            <a id="link3" href="/my_link3">Link 3</a>
            <a id="link3" href="/my_link4">Link 4</a>
        </p>
    </div>
</body>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
link2_tag = soup.find(id="link3").find_parent('p').find_previous('h5')

print(link2_tag)