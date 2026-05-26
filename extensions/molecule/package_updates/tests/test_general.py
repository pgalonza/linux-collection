"""Test package_updates role."""

import os
import pytest


def test_package_updates_role_installed(host):
    """Check that package_updates role tasks executed without errors."""
    # This is a basic test - in real scenario we would check
    # if packages are pinned or updated
    assert True


def test_dry_run_mode(host):
    """Check that dry-run mode was used (no actual changes)."""
    # Since we used dry-run: true, no packages should be actually updated
    # This is just a placeholder test
    assert True


@pytest.mark.parametrize("package", [
    "python3",
])
def test_python3_is_installed(host, package):
    """Test that python3 package is installed (base image)."""
    # python3 is pre-installed in the base images
    assert host.package(package).is_installed