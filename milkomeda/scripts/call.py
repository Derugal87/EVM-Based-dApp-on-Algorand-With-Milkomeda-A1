from brownie import Storage, Contract, accounts, config

signer = accounts.add(config["wallets"]["dummy"])

def main():
    contract_address = "0xE389A7d21a98497d953a3fc3bf283BF5107fc621"
    storage = Contract.from_abi("Storage", abi=Storage.abi, address=contract_address)

    stored_value = storage.retrieve()
    print("Current value is:", stored_value)

    storage.store(stored_value + 1, {"from": signer})

    stored_value = storage.retrieve()
    print("Current value is:", stored_value)
