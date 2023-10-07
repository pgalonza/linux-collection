def test_file_permissions(host):
    assert host.file('/etc/passwd').mode == 0o644
    assert host.file('/etc/group').mode == 0o644
    assert host.file('/etc/shadow').mode == 0o600