from models import transactions

class TestTransaction():
    def test_single_transaction(self):
        example = '''
        {
  "transactions": [
    {
      "id": "txn_9iyd7pd3KQPAh5hwGxSbz3",
      "cardholderId": "u_4ghf9XE19xkAF0SFuvESez",
      "cardholderName": "Sarah Sanzari",
      "cardholderEmail": "sarah@paywithextend.com",
      "recipientName": "Kento Okamoto",
      "recipientEmail": "sarah+kento@paywithextend.com",
      "recipientId": "u_6Z4b7TxXAJ97m70luC2zAM",
      "nameOnCard": "Kento Okamoto",
      "source": "VIRTUAL",
      "vcnLast4": "9724",
      "vcnDisplayName": "Kento’s take home",
      "virtualCardId": "vc_0nWwUYip92B5iF1yZCODCl",
      "type": "DEBIT",
      "status": "PENDING",
      "approvalCode": "447624",
      "authBillingAmountCents": 1648,
      "authBillingCurrency": "USD",
      "authMerchantAmountCents": 1648,
      "authMerchantCurrency": "USD",
      "authExchangeRate": 1,
      "clearingBillingAmountCents": 0,
      "clearingBillingCurrency": "USD",
      "clearingMerchantAmountCents": 0,
      "clearingMerchantCurrency": "USD",
      "clearingExchangeRate": 1,
      "mcc": "5941",
      "mccGroup": "RETAIL",
      "mccDescription": "SPORTING GOODS STORES",
      "merchantName": "REI.COM  800-426-4840  800-426-4840  WA",
      "merchantAddress": "",
      "merchantCity": "",
      "merchantState": "",
      "merchantZip": "",
      "authedAt": "2023-02-18T00:59:00.000+0000",
      "updatedAt": "2023-02-18T01:00:14.511+0000",
      "hasAttachments": false,
      "referenceId": "447624",
      "creditCardId": "cc_66KdhnNCr0G6hJE45PV4GU",
      "parentCreditCardId": "cc_4RSlfSqmfDVAKIgYVkXRwx",
      "sentToExpensify": false,
      "sentToQuickbooks": false,
      "attachmentsCount": 0,
      "referenceFields": [],
      "creditCardDisplayName": "Take home assignment budget",
      "parentCreditCardDisplayName": "Comdata Ghost Card",
      "creditCardHasReferenceFields": true,
      "creditCardType": "DELEGATE"
    }
  ]
}'''
        transactions.TransactionList.parse_raw(example)
