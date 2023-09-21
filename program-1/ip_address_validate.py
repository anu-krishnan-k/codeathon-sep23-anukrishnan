def is_valid_ip_address(ip_address):
    # Split the IP address into its four components
    components = ip_address.split('.')
    # Check that there are exactly four components
    if len(components) != 4:
        return False
    # Check that each component is an integer between 0 and 255
    for component in components:
        try:
            value = int(component)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False
    # If we got here, the IP address is valid
    return True

def test_is_valid_ip_address():
    assert is_valid_ip_address('192.168.0.1') == True
    assert is_valid_ip_address('255.255.0.0') == True
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('555.555.555.555') == False
    assert is_valid_ip_address('256.255.0.0') == False
