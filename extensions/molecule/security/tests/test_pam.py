def test_pam_su_wheel(host):
    pam_su = host.file('/etc/pam.d/su')
    assert pam_su.contains('^auth.*required.*pam_wheel.so.*use_uid$')