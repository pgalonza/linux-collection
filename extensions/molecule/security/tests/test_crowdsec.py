def test_crowdsec_config(host):
    assert host.file('/etc/crowdsec/config.yaml').exists
    # assert host.file('/etc/crowdsec/parsers/s02-enrich/whitelists-external.yaml').exists
