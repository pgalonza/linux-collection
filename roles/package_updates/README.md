# Package Updates

Simple role for managing package updates with version pinning capability.

## Purpose

The role performs three main functions:
1. **Package updates** - all packages or security updates only
2. **Version pinning** - preventing updates of specified packages
3. **Unpinning** - allowing updates of specified packages

## Supported Distributions

- **Debian/Ubuntu** (apt)
- **RedHat/CentOS** (yum/dnf)

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `package_updates_enabled` | `true` | Enable/disable the role |
| `package_updates_mode` | `"security"` | Mode: `all` (all packages), `security` (security only), `none` (pinning only) |
| `package_pin_list` | `[]` | List of packages to pin |
| `package_unpin_list` | `[]` | List of packages to unpin |
| `update_cache` | `true` | Update package cache before updating |
| `package_updates_dry_run` | `false` | Simulation mode (no actual changes) |
| `package_updates_install_plugins` | `true` | Automatic installation of versionlock plugins for RedHat/CentOS |

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

## Tags

- `package-updates` - all tasks
- `package-update-all` - update all packages
- `package-update-security` - security updates
- `package-pin` - pin packages
- `package-unpin` - unpin packages
- `package-list-pinned` - show pinned packages

## How It Works

### For Debian/Ubuntu:
- Pin: `apt-mark hold <package>`
- Unpin: `apt-mark unhold <package>`
- Show pinned: `apt-mark showhold`

### For RedHat/CentOS:
- Pin: `yum versionlock add <package>` or `dnf versionlock add <package>`
- Unpin: `yum versionlock delete <package>` or `dnf versionlock delete <package>`
- Show pinned: `yum versionlock list` or `dnf versionlock list`

## Notes

1. For pinning to work on RedHat/CentOS, the following plugins are required:
   - RedHat 7: `yum-plugin-versionlock`
   - RedHat 8+: `python3-dnf-plugin-versionlock`
   The role automatically installs these plugins when `package_updates_install_plugins: true` (default).

2. Dry-run mode allows checking what would be done without actual changes (plugin installation is also skipped in dry-run).

3. The role does not restart services or reboot the system after updates.

## Author

Peter Galonza