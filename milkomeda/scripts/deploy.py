from brownie import Storage, accounts, config

def main():
    # signer = accounts.add(config['wallets']['dummy'])
    signer = accounts.add("8ea85d3c7877e3422fffd96415eaa109b54c9d85fc82d75a452aae6c035e7644")
    Storage.deploy({"from": signer})
