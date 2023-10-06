def test_sshd_config(host):
    assert host.file('/etc/ssh/sshd_config').exists

def test_sshd_banner(host):
    assert host.file('/etc/ssh/ssh-banner').exists