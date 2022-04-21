import re

from docutils import nodes
from docutils.parsers.rst.roles import set_classes

def role_important(role, rawtext, text, lineno, inliner, options={}, content=[]):
  options.update({'classes': ["proxyos-important"]})
  set_classes(options)
  return [nodes.inline(rawtext, text, **options)], []

def role_repository(role, rawtext, text, lineno, inliner, options={}, content=[]):
  options.update({'classes': ["proxyos-repository"]})
  set_classes(options)

  result = re.search(r'([^<]*) <([^>]*)>', text)
  if not result:
    raise Exception('Invalid repository format for: "%s"' % text)

  name = result.group(1)
  url = 'https://gitlab.com/proxyos/%s' % result.group(2)

  return [nodes.reference(rawtext, name, refuri=url, **options)], []

def role_repofile(role, rawtext, text, lineno, inliner, options={}, content=[]):
  options.update({'classes': ["proxyos-repofile"]})
  set_classes(options)

  result = re.search(r'([^<]*) <([^|]*)\|([^>]*)>', text)
  if not result:
    raise Exception('Invalid repository format for: "%s"' % text)

  pretty = result.group(1)
  repo = result.group(2)
  path = result.group(3)
  url = 'https://gitlab.com/proxyos/%s/-/tree/master/%s' % (repo, path)
  name = '%s[%s]' % (pretty, path)

  return [nodes.reference(rawtext, name, refuri=url, **options)], []

def setup(app):
  app.add_role('important', role_important)
  app.add_role('repository', role_repository)
  app.add_role('repofile', role_repofile)
