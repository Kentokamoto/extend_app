from __future__ import annotations

from typing import List

from pydantic import BaseModel


class IssuerSanction(BaseModel):
    name: str
    status: str


class Organization(BaseModel):
    id: str
    role: str
    joinedAt: str
    lastLoggedInAt: str
    explicit: bool


class User(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    phone: str
    phoneIsoCountry: str
    avatarType: str
    avatarUrl: str
    createdAt: str
    updatedAt: str
    currency: str
    locale: str
    timezone: str
    verified: bool
    hasExpensifyLink: bool
    quickbooksTokenId: str
    employeeId: str
    issuerSanctions: List[IssuerSanction]
    organization: Organization
    organizationId: str
    organizationRole: str


class Account(BaseModel):
    user: User
    token: str
    refreshToken: str
