from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


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


class TransactionList(BaseModel):
    transactions: Optional[List[Transaction]] = None

