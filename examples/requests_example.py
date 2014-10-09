import requests
import urlparse

GITHUB_API_URL = 'https://api.github.com/'
ROBOTTELO_COLLABORATORS_URL = urlparse.urljoin(
    GITHUB_API_URL, '/repos/SatelliteQE/robottelo/collaborators')

response = requests.get(ROBOTTELO_COLLABORATORS_URL)
results = response.json()

print 'Robottelo collaborators:'
for collaborator in results:
    print '* {0} - {1}'.format(
        collaborator['login'], collaborator['html_url'])
