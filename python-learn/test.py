from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

# make Edge headless
edge_options = EdgeOptions()
edge_options.use_chromium = True  # if we miss this line, we can't make Edge headless
# A little different from Chrome cause we don't need two lines before 'headless' and 'disable-gpu'
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')

driver = Edge(executable_path='where', options=edge_options)