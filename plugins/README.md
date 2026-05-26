# Collections Plugins Directory

This directory is reserved for [Ansible collection plugins](https://docs.ansible.com/ansible/latest/plugins/plugins.html). Plugins extend Ansible’s core functionality by adding new module utilities, lookup plugins, filters, callbacks, and more.

## Structure

- `plugins/` – root directory for all plugin types
  - `modules/` – custom modules (executable Python or PowerShell scripts)
  - `module_utils/` – shared library code for modules
  - `lookup/` – lookup plugins (e.g., `lookup('my_plugin')`)
  - `filter/` – Jinja2 filter plugins
  - `callback/` – callback plugins (control output and events)
  - `connection/` – connection plugins (e.g., `docker`, `httpapi`)
  - `inventory/` – dynamic inventory plugins
  - `vars/` – variable plugins
  - `strategy/` – strategy plugins (control playbook execution flow)
  - `shell/` – shell plugins (for target shells)
  - `test/` – test plugins (Jinja2 tests)

## Current Status

This collection (`pgalonza.linux`) does not yet include any custom plugins. The directory is kept as a placeholder for future extensions.

## Adding Plugins

If you wish to contribute a plugin:

1. Create the appropriate subdirectory (e.g., `plugins/lookup/`).
2. Write your plugin following Ansible’s plugin development guidelines.
3. Update the `galaxy.yml` file to declare the plugin in the `plugins` section (optional but recommended).
4. Test the plugin locally before submitting a pull request.

## Documentation

- [Ansible Plugin Development](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html)
- [Collections Structure](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_structure.html)
