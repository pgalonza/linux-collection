def test_kernel_parameters(host):
    pam_su = host.file('/etc/default/grub')
    assert pam_su.contains('^GRUB_CMDLINE_LINUX=')