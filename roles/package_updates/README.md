# Package Updates

Role for managing package updates and declarative version locks on RHEL-based systems.

## Supported Platforms

- RHEL / AlmaLinux / Rocky Linux 8
- RHEL / AlmaLinux / Rocky Linux 9

> Debian/Ubuntu support is being reworked separately. The role fails with an
> explicit error on non-RHEL systems.

## How It Works

The role separates two concerns:

1. **What to update** — `package_updates_mode`
2. **How to treat locked packages** — `package_updates_locked_policy`

Locked packages are defined exclusively by `package_updates_lock_list`.
The role manages these locks itself; `dnf versionlock` entries that are not
present in the lock or unlock lists are not modified.

### Update modes

| Mode | Description |
|------|-------------|
| `all` | Update all available packages |
| `security` | Update security advisories only |
| `specific` | Update packages from `package_updates_specific_list` |
| `none` | Do not update anything, only manage locks |

### Locked-package policies

| Policy | Description |
|--------|-------------|
| `exclude` | Locked packages are not updated |
| `include` | All selected packages are updated, including locked ones; all configured locks are released during the run and restored afterwards |
| `only` | Only locked packages are updated; all configured locks are released during the run and restored afterwards |

### Mode and policy matrix

| Mode | `exclude` | `include` | `only` |
|------|-----------|-----------|--------|
| `all` | All except locked | All, including locked | Only locked |
| `security` | Security except locked | All security, including locked | Security for locked only |
| `specific` | Listed packages except locked | Listed packages, including locked | Locked packages from the list |

For `specific`, a locked package is skipped when the policy is `exclude`.
To update a locked package explicitly, use `package_updates_locked_policy: include`.

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `package_updates_mode` | `"security"` | `all`, `security`, `specific`, or `none` |
| `package_updates_locked_policy` | `"exclude"` | `exclude`, `include`, or `only` |
| `package_updates_lock_list` | `[]` | Packages to lock before updating |
| `package_updates_unlock_list` | `[]` | Packages whose locks should be removed |
| `package_updates_specific_list` | `[]` | Packages for `specific` mode; strings or dictionaries with `name` and optional `version` |
| `package_updates_refresh_cache` | `true` | Refresh DNF metadata before package operations |
| `package_updates_only_installed` | `true` | In `specific` mode, update only already installed packages |

`package_updates_lock_list` and `package_updates_unlock_list` should not contain
the same package. Validation is intentionally minimal: only the two option
variables are checked, and `package_updates_lock_list` is verified against
installed packages. Malformed list types surface as task failures.

## Examples

### Update everything except locked packages

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: package_updates
      vars:
        package_updates_mode: "all"
        package_updates_locked_policy: "exclude"
        package_updates_lock_list:
          - kernel
          - docker-ce
```

### Update everything, including locked packages

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: package_updates
      vars:
        package_updates_mode: "all"
        package_updates_locked_policy: "include"
        package_updates_lock_list:
          - kernel
          - docker-ce
```

`kernel` and `docker-ce` are temporarily unlocked, updated, and locked again at
their new installed versions.

### Update only locked packages

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: package_updates
      vars:
        package_updates_mode: "all"
        package_updates_locked_policy: "only"
        package_updates_lock_list:
          - kernel
          - docker-ce
```

### Update specific packages

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: package_updates
      vars:
        package_updates_mode: "specific"
        package_updates_specific_list:
          - nginx
          - name: openssl
            version: "3.0.13-1.el9"
```

A string updates the package to the latest available version. A dictionary with
`version` installs that exact version.

### Only manage locks

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: package_updates
      vars:
        package_updates_mode: "none"
        package_updates_lock_list:
          - kernel
```

## Tags

| Tag | Description |
|-----|-------------|
| `package-updates` | Refresh cache, apply locks/unlocks, and perform updates |
| `package-lock` | Apply `package_updates_lock_list` only |
| `package-unlock` | Apply `package_updates_unlock_list` only |
| `package-locked` | Show configured and actual versionlock entries |

## Lock Management

The role uses:

- `community.general.dnf_versionlock` to add and remove version locks;
- `python3-dnf-plugin-versionlock` as the required DNF plugin.

The lock list is not validated against installed packages. Names in
`package_updates_lock_list` that are not installed are passed to
`dnf_versionlock`, which may lock available (not installed) versions of those
packages.

For `include` and `only` policies, every configured lock is temporarily
released for the duration of the update transaction and restored in an `always`
block, including when the update fails.

## Check Mode

Check mode works for validation and read-only tasks. For `include` and `only`
policies the simulation is approximate: version locks cannot be temporarily
removed non-destructively in check mode, so locked packages may not appear in
the simulated update transaction.

## Notes

1. The role does not restart services or reboot the system after updates.
2. A kernel update may require a reboot; this is not handled by the role.
3. On RHEL-based systems `dnf` is used. `yum` and `dnf5` are not supported.
4. On EL8, configure a Python interpreter supported by your Ansible version
   (3.8 or newer) together with matching DNF Python bindings. The default EL8
   Python 3.6 is not supported by Ansible 2.20.
5. The role is not idempotent in terms of changed-task reporting for `include`
   and `only` policies, because locks are intentionally removed and restored on
   every run.

## Author

Peter Galonza
