import os
import json


def read_file(path):
    return open(os.path.join(os.path.dirname(__file__), path), 'r', encoding='utf-8')


SCANS = {
    'Ethereum': 'https://etherscan.io',
    'Optimism': 'https://optimistic.etherscan.io',
    'BSC': 'https://bscscan.com',
    'Gnosis': 'https://gnosisscan.io',
    'Polygon': 'https://polygonscan.com',
    'Fantom': 'https://ftmscan.com',
    'Arbitrum': 'https://arbiscan.io',
    'Avalanche': 'https://snowtrace.io',
    'zkSync': 'https://explorer.zksync.io',
    'Linea': 'https://lineascan.build',
    'Base': 'https://basescan.org',
    'zkEVM': 'https://zkevm.polygonscan.com',
    'Scroll': 'https://scrollscan.com',
    'Gravity': 'https://explorer.gravity.xyz',
}

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

SPACE_STATION_ABI = json.load(read_file('abi/space_station.json'))
LOYALTY_POINTS_ABI = json.load(read_file('abi/loyalty_points.json'))
ETHEREUM_INSTANT_PAYMENT_ABI = json.load(read_file('abi/ethereum_instant_payment.json'))
ARBITRUM_INSTANT_PAYMENT_ABI = json.load(read_file('abi/arbitrum_instant_payment.json'))
BASE_INSTANT_PAYMENT_ABI = json.load(read_file('abi/base_instant_payment.json'))

EIP1559_CHAINS = ['Ethereum', 'Optimism', 'Polygon', 'Arbitrum', 'Linea', 'Base', 'Scroll']


INSTANT_PAYMENT_CONTRACTS = {
    "ethereum": "0x07c78007DdcFFA630fD908a815165e5B0Af0C4F2",
    "arbitrum": "0x432CD30a1A45f20404f03863cB889e7876A957Af",
    "base": "0x96eb090B35dfBbe7208f357CD509a658c359209B"
}
