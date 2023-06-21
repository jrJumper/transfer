from web3 import Web3

# Подключение к блокчейну Ethereum
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Приватный ключ и адрес отправителя
private_key_sender = 'YOUR_PRIVATE_KEY_SENDER'
address_sender = 'SENDER_ADDRESS'

# Адрес получателя
address_recipient = 'RECIPIENT_ADDRESS'

# Адрес токена и его десятичные знаки
token_address = 'TOKEN_ADDRESS'
decimals = 18

# Количество токенов для перевода
amount_to_send = 100  # Указать желаемое количество токенов

# Получение nonce отправителя
nonce = web3.eth.getTransactionCount(address_sender)

# Получение контракта токена
token_contract = web3.eth.contract(address=token_address, abi=ABI)  # Замените ABI на фактическое значение ABI контракта

# Вычисление значения токена в минимальных единицах (wei)
amount_in_wei = amount_to_send * 10 ** decimals

# Создание транзакции перевода токенов
transaction = token_contract.functions.transfer(address_recipient, amount_in_wei).buildTransaction({
    'from': address_sender,
    'gas': 100000,  # Укажите желаемое значение газа
    'gasPrice': web3.toWei('50', 'gwei'),  # Укажите желаемую цену газа
    'nonce': nonce,
})

# Подписывание транзакции с использованием приватного ключа отправителя
signed_transaction = web3.eth.account.signTransaction(transaction, private_key_sender)

# Отправка транзакции в блокчейн
transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# Ожидание подтверждения транзакции
transaction_receipt = web3.eth.waitForTransactionReceipt(transaction_hash)

# Проверка статуса транзакции
if transaction_receipt.status == 1:
    print('Транзакция успешно выполнена!')
else:
    print('Транзакция не удалась. Проверьте ошибки.')
