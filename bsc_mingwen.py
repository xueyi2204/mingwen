from web3 import Web3
import time


def send_transactions():
    # 替换为你的 BSC 节点 URL
    bsc_node_url = "https://bsc-dataseed.binance.org"

    # 替换为你的钱包私钥
    private_key =  ""

    # 替换为你的目标地址
    to_address = ""
    to_address = Web3.to_checksum_address(to_address)

    # to_address = to_address.upper()
    # print(to_address)

    # 替换为你想发送的 16 进制数据
    hex_data = ""

    # 连接到 BSC 节点
    w3 = Web3(Web3.HTTPProvider(bsc_node_url))
    print(w3.is_connected())
    account = w3.eth.account.from_key(private_key)
    balance_wei = w3.eth.get_balance(to_address)
    balance_bnb = w3.from_wei(balance_wei, 'ether')
    print(f"账户余额: {balance_bnb} BNB")

    # 构造交易
    transaction = {
        'to': to_address,
        'value': 0,  # 0 BNB
        'gas': 31000,  # Gas 需要根据实际情况调整
        'gasPrice': w3.to_wei('6', 'gwei'),  # Gas Price 需要根据实际情况调整
        'nonce': w3.eth.get_transaction_count(account.address),
        'data': hex_data,
        'chainId': 56,  # 指定链ID
    }

    # 签名交易
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)

    # 发送交易
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print(f"Transaction sent. Transaction hash: {transaction_hash.hex()}")

    receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print(f"交易成功: {receipt['status']}")
    print(f"Gas 消耗: {receipt['gasUsed']} wei")

    # 获取交易信息
    transaction_data = w3.eth.get_transaction(transaction_hash)
    block_number = transaction_data['blockNumber']
    print(f"交易 {transaction_hash} 所在区块号: {block_number}")
    time.sleep(5)



for i in range(500):
    print(f"正在第{i}次交易...")
    send_transactions()