
# Get Bank Account Response

Response object returned by `GetBankAccount`.

## Structure

`Get Bank Account Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `bank_account` | [`Bank Account`](../../doc/models/bank-account.md) | Optional | Represents a bank account. For more information about<br>linking a bank account to a Square account, see<br>[Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api). |

## Example (as JSON)

```json
{
  "bank_account": {
    "account_number_suffix": "971",
    "account_type": "CHECKING",
    "bank_name": "Bank Name",
    "country": "US",
    "creditable": false,
    "currency": "USD",
    "debitable": false,
    "holder_name": "Jane Doe",
    "id": "w3yRgCGYQnwmdl0R3GB",
    "location_id": "S8GWD5example",
    "primary_bank_identification_number": "112200303",
    "status": "VERIFICATION_IN_PROGRESS",
    "version": 5
  }
}
```

