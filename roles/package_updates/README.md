# Package Updates

Simple role for managing package updates with version pinning capability.

## Purpose

The role performs four main functions:
1. **Package updates** - all packages or security updates only
2. **Specific version updates** - update specific packages to specified versions
3. **Version pinning** - preventing updates of specified packages
4. **Unpinning** - allowing updates of specified packages

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
   - RedHat 8+: `python3-dnf-plugin-versionlock`

2. Dry-run mode allows checking what would be done without actual changes (plugin installation is also skipped in dry-run).

3. The role does not restart services or reboot the system after updates.

## Author

Peter Galonza