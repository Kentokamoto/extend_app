from __future__ import annotations

import datetime
from prettytable import PrettyTable

from typing import List, Optional

from pydantic import BaseModel


class Pagination(BaseModel):
    page: int
    pageItemCount: int
    totalItems: int
    numberOfPages: int


class Recipient(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    phone: str
    phoneIsoCountry: str
    avatarType: str
    createdAt: str
    updatedAt: str
    currency: str
    locale: str
    timezone: str
    verified: bool
    mfaPreference: str
    def name(self):
        return "{} {}".format(self.firstName, self.lastName)


class Organization(BaseModel):
    id: str
    role: str
    joinedAt: str
    lastLoggedInAt: str
    explicit: bool


class Cardholder(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    phone: str
    phoneIsoCountry: str
    avatarType: str
    createdAt: str
    updatedAt: str
    currency: str
    locale: str
    timezone: str
    verified: bool
    organization: Organization
    organizationId: str
    organizationRole: str
    mfaPreference: str

    def name(self):
        return "{} {}".format(self.firstName, self.lastName)


class Urls(BaseModel):
    large: str
    medium: str
    small: str


class CardImage(BaseModel):
    id: str
    contentType: str
    urls: Urls
    textColorRGBA: str
    hasTextShadow: bool
    shadowTextColorRGBA: str


class Address(BaseModel):
    address1: str
    address2: str
    city: str
    province: str
    postal: str
    country: str

    def __str__(self):
        output = '''{addr1}
{addr2}
{city}, {province}, {postal}
{country}'''.format(addr1=self.address1,
                    addr2=self.address2,
                    city=self.city,
                    province=self.province,
                    postal=self.province,
                    country=self.country)
        return output


class Features(BaseModel):
    customAddress: bool
    customMax: bool


class Issuer(BaseModel):
    id: str
    name: str


class VirtualCard(BaseModel):
    id: str
    status: str
    recipientId: str
    recipient: Recipient
    cardholderId: str
    cardholder: Cardholder
    cardImage: CardImage
    displayName: str
    expires: str
    currency: str
    limitCents: int
    balanceCents: int
    spentCents: int
    lifetimeSpentCents: int
    last4: str
    numberFormat: str
    validFrom: str
    validTo: str
    timezone: str
    creditCardId: str
    recurs: bool
    createdAt: str
    updatedAt: str
    address: Address
    direct: bool
    features: Features
    hasPlasticCard: bool
    activeUntil: str
    companyName: str
    creditCardDisplayName: str
    issuer: Issuer


class Cards(BaseModel):
    pagination: Optional[Pagination] = None
    virtualCards: Optional[List[VirtualCard]] = None

    def pretty_print(self):
        table = PrettyTable(
            [
                "Card Number",
                "Last 4",
                "Name on Card",
                "Billing Address",
                "Exp Date",
                "Description",
                "Limit ($)",
                "Spent ($)",
                "Balance ($)",
            ]
        )
        # Formatting
        table.align["Billing Address"] = 'l'

        if self.virtualCards:
            for index, card in enumerate(self.virtualCards):
                name = card.recipient.name()
                last4 = card.last4
                exp_date = datetime.datetime.strptime(
                    card.expires, "%Y-%m-%dT%H:%M:%S.%f%z"
                ).strftime("%m/%Y")
                limit = "{0:.2f}".format(float(card.limitCents) / 100)
                spent = "{0:.2f}".format(float(card.lifetimeSpentCents) / 100)
                balance = "{0:.2f}".format(float(card.balanceCents) / 100)
                address = str(card.address)
                description = card.displayName

                table.add_row([index,
                               last4,
                               name,
                               address,
                               exp_date,
                               description,
                               limit,
                               spent,
                               balance])
            print(table)
