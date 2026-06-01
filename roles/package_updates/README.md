# Package Updates

Simple role for managing package updates with version pinning capability.

## Purpose

The role performs six main functions:
1. **Update cache** - refresh the package manager cache before updates
2. **Package updates** - all packages or security updates only
3. **Specific version updates** - update specific packages to specified versions
4. **Version pinning** - preventing updates of specified packages
5. **Unpinning** - allowing updates of specified packages
6. **Show pinned** - display the list of currently pinned packages

## Supported Distributions

- **Debian/Ubuntu** (apt)
- **RedHat/CentOS** (yum/dnf)

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `package_updates_mode` | `"security"` | Mode: `all` (all packages), `security` (security only), `specific` (specific packages), `none` (pinning only) |
| `package_pin_list` | `[]` | List of packages to pin |
| `package_unpin_list` | `[]` | List of packages to unpin |
| `package_specific_list` | `[]` | List of packages to update to specific versions (only when mode is `specific`). Format: list of dictionaries with `name` and `version` keys. |
| `update_cache` | `true` | Update package cache before updating |

## Usage Examples

### Example 1: Security updates with package pinning
```yaml
- hosts: servers
  roles:
    - package_updates
  vars:
    package_updates_mode: "security"
    package_pin_list:
      - nginx
      - postgresql
      - docker-ce
```

### Example 2: Full update of all packages
```yaml
- hosts: servers
  roles:
    - package_updates
  vars:
    package_updates_mode: "all"
```

### Example 3: Package pinning only (no updates)
```yaml
- hosts: servers
  roles:
    - package_updates
  vars:
    package_updates_mode: "none"
    package_pin_list:
      - kernel
      - openssl
```

### Example 4: Unpinning and updating
```yaml
- hosts: servers
  roles:
    - package_updates
  vars:
    package_updates_mode: "all"
    package_unpin_list:
      - nginx
      - php
```

### Example 5: Update specific packages to specified versions
```yaml
- hosts: servers
  roles:
    - package_updates
  vars:
    package_updates_mode: "specific"
    package_specific_list:
      - name: nginx
        version: 1.18.0
      - name: docker-ce
        version: 5:20.10.7
```

## Tags

- `package-updates` - update all packages
- `package-pin` - pin packages
- `package-unpin` - unpin packages
- `package-list-pinned` - show pinned packages

## Task Structure

The role's `main.yml` uses `import_tasks` to include modular task files, executed in the following order:

| Task file | Tags | Description |
|-----------|------|-------------|
| [`update_cache.yml`](tasks/update_cache.yml) | `package-updates` | Refreshes the package manager cache (apt or dnf) |
| [`install_plugins.yml`](tasks/install_plugins.yml) | `package-unpin`, `package-pin`, `package-list-pinned` | Installs `python3-dnf-plugin-versionlock` on RedHat 8+ |
| [`unpin.yml`](tasks/unpin.yml) | `package-unpin` | Unpins packages using `apt-mark unhold` or `dnf versionlock delete` |
| [`updates.yml`](tasks/updates.yml) | `package-updates` | Performs package updates (security, all, or specific versions) |
| [`pin.yml`](tasks/pin.yml) | `package-pin` | Pins packages using `apt-mark hold` or `dnf versionlock add` |
| [`show_pinned.yml`](tasks/show_pinned.yml) | `package-list-pinned` | Displays currently pinned packages |

## How It Works

### For Debian/Ubuntu:
- Pin: `apt-mark hold <package>`
- Unpin: `apt-mark unhold <package>`
- Show pinned: `apt-mark showhold`

### For RedHat/CentOS (8+):
- Pin: `dnf versionlock add <package>`
- Unpin: `dnf versionlock delete <package>`
- Show pinned: `dnf versionlock list`

## Notes

1. For pinning to work on RedHat/CentOS, the following plugins are required:
   - RedHat 8+: `python3-dnf-plugin-versionlock` (installed automatically by the role)

2. The role does not restart services or reboot the system after updates.

3. The `update_cache` variable controls whether the package cache is refreshed before updates. Cache is only updated when `package_updates_mode` is not `none`.

## Author

Peter Galonza