from __future__ import annotations

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

