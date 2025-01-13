def test_sshd_config(host):
    assert host.file('/etc/ssh/sshd_config').exists
