from __future__ import annotations
from prettytable import PrettyTable
import datetime

from typing import List, Optional

from pydantic import BaseModel

class DeclineReason(BaseModel):
    code: str
    description: str

class Transaction(BaseModel):
    id: str
    cardholderId: str
    cardholderName: str
    cardholderEmail: str
    recipientName: str
    recipientEmail: str
    recipientId: str
    nameOnCard: str
    source: str
    vcnLast4: str
    vcnDisplayName: str
    virtualCardId: str
    type: str
    status: str
    declineReasons: Optional[List[DeclineReason]] = None
    approvalCode: str
    authBillingAmountCents: int
    authBillingCurrency: str
    authMerchantAmountCents: int
    authMerchantCurrency: str
    authExchangeRate: int
    clearingBillingAmountCents: int
    clearingBillingCurrency: str
    clearingMerchantAmountCents: int
    clearingMerchantCurrency: str
    clearingExchangeRate: int
    mcc: str
    mccGroup: str
    mccDescription: str
    merchantName: str
    merchantAddress: str
    merchantCity: str
    merchantState: str
    merchantZip: str
    authedAt: str
    updatedAt: str
    hasAttachments: bool
    referenceId: str
    creditCardId: str
    parentCreditCardId: str
    sentToExpensify: bool
    sentToQuickbooks: bool
    attachmentsCount: int
    referenceFields: List
    creditCardDisplayName: str
    parentCreditCardDisplayName: str
    creditCardHasReferenceFields: bool
    creditCardType: str

    def pretty_print(self):
        print()
        print("TRANSACTION INFO")
        print("Merchant           ---> {}".format(self.merchantName))
        print("Type               ---> {}".format(self.mccGroup))
        print(
            "Transaction Date   ---> {}".format(
                datetime.datetime.strptime(
                    self.authedAt, "%Y-%m-%dT%H:%M:%S.%f%z"
                ).strftime("%c %Z")
            )
        )
        print("Authorized amount  ---> {0:.2f}".format(
            float(self.authBillingAmountCents)/100))
        print("Cleared amount     ---> {0:.2f}".format(
            float(self.clearingBillingAmountCents)/100))
        print("Status             ---> {}".format(self.status))
        print("City               ---> {}".format(self.merchantCity))
        print("State              ---> {}".format(self.merchantState))
        print("Address            ---> {}".format(self.merchantAddress))

        print()
        print("CARD INFO")
        print("Last 4 Digits      ---> {}".format(self.vcnLast4))
        print("Parent Credit Card ---> {}".format(
            self.parentCreditCardDisplayName))
        print("Display Name       ---> {}".format(self.creditCardDisplayName))
        print()


class TransactionList(BaseModel):
    transactions: Optional[List[Transaction]] = None

    def pretty_print(self):
        table = PrettyTable(
            [
                "Index",
                "Transaction ID",
                "Transaction Date",
                "Authorization Amount",
                "Currency",
                "Name",
                "Description",
                "City",
                "State",
            ]
        )
        if self.transactions:
            for index, transaction in enumerate(self.transactions):
                id = transaction.id
                auth_date = datetime.datetime.strptime(
                    transaction.authedAt, "%Y-%m-%dT%H:%M:%S.%f%z"
                ).strftime("%c %Z")
                auth_amount = "{0:.2f}".format(
                        float(transaction.authBillingAmountCents) / 100)
                currency = transaction.authBillingCurrency
                merchant_name = transaction.merchantName
                merchante_description = transaction.mccDescription
                merchant_city = transaction.merchantCity
                merchant_state = transaction.merchantState
                table.add_row(
                    [
                        index,
                        id,
                        auth_date,
                        auth_amount,
                        currency,
                        merchant_name,
                        merchante_description,
                        merchant_city,
                        merchant_state,
                    ]
                )
            print(table)
        else:
            print("No transactions found for this card")
