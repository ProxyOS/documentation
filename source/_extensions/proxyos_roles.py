from docutils import nodes
from docutils.parsers.rst.roles import set_classes

def role_important(role, rawtext, text, lineno, inliner, options={}, content=[]):
  options.update({'classes': ["proxyos-important"]})
  set_classes(options)
  return [nodes.inline(rawtext, text, **options)], []

def setup(app):
  app.add_role('important', role_important)
