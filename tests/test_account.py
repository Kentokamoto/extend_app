from models import account


class TestAccount:
    example_model = '''{
    "user": {
        "id": "u_6Z4b7TxXAJ97m70luC2zAM",
        "firstName": "Kento",
        "lastName": "Okamoto",
        "email": "sarah+kento@paywithextend.com",
        "phone": "+12125555555",
        "phoneIsoCountry": "US",
        "avatarType": "DEFAULT",
        "createdAt": "2023-02-13T22:28:11.180+0000",
        "updatedAt": "2023-02-18T00:20:50.649+0000",
        "currency": "USD",
        "locale": "en-US",
        "timezone": "America/New_York",
        "verified": true,
        "mfaPreference": "EMAIL"
    },
    "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qWXlOME15T1RjeE16azJPRUk1TVVKR1FqWTVOME5GUVVSQ1FVWkVPRVJETURBMU5rRXdOdyJ9.eyJpc3MiOiJodHRwczovL2V4dGVuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNlYWI5N2JlNjI0ODllYWU2NTY2ZGQ4IiwiYXVkIjpbImV4dGVuZCIsImh0dHBzOi8vZXh0ZW5kLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzY2Nzk2NTAsImV4cCI6MTY3NjY4MDU1MCwiYXpwIjoiTFN1R0swSmluMkRkVW9qbHRDWDloZHlRTU9OUlM3d2YiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFkZHJlc3MgcGhvbmUgcmVhZDpjcmVkaXRjYXJkcyBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.QJP_F345hVCbcP0YvdRjkjtf5XAqLQ1qj5DEiA6x7Lczp6du7sK5O33e8EEU1ilpSNaLkrtEkZ2-UldnhZ6uOgl_5d__aqTw4oN0I--eCDGf8-yUfA8cGSy50udZPKR03GS-dwp-DtSdXjAb0mvMuwqTv_-bj2XOc3RrbIZFaxW8FJBQwEdadA8vBj_9qWBInATcQsi9kMmvU2WZn5uZLRxOKYbBXtiql5MAwPmKGUC8BIlAcgFGCIpyBzbrePhT8f7U4iQx1a4v5VpesFsaVBLkjQ8C80bjvM-pdbjPMPfem6h1fdbhO4q9tpyb16FCC88RRaGpR1v6BuvTpNLbbg",
    "refreshToken": "v1.Ma8DMrG__9mjZ-vKNzSrACDOFjCKUc25QMRMkHHs4u-cVh1YieJL2WorYdTVm08Gsn-N0C6UQVwFpvw9WiTKkf8"
    }'''

    def test_model_schema(self):
        acct = account.Account.parse_raw(self.example_model)

    def test_get_user_model_schema(self):
        response = '''
        {"id":"u_6Z4b7TxXAJ97m70luC2zAM",
        "firstName":"Kento",
        "lastName":"Okamoto",
        "email":"sarah+kento@paywithextend.com",
        "phone":"+12125555555",
        "phoneIsoCountry":"US",
        "avatarType":"DEFAULT",
        "createdAt":"2023-02-13T22:28:11.180+0000",
        "updatedAt":"2023-02-18T01:49:06.585+0000",
        "currency":"USD",
        "locale":"en-US",
        "timezone":"America/New_York",
        "verified":true,
        "mfaPreference":"EMAIL"}
        '''
        acct = account.User.parse_raw(response)
