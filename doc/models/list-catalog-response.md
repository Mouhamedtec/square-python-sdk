
# List Catalog Response

## Structure

`List Catalog Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request. If unset, this is the final response.<br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `objects` | [`List of Catalog Object`](../../doc/models/catalog-object.md) | Optional | The CatalogObjects returned. |

## Example (as JSON)

```json
{
  "objects": [
    {
      "category_data": {
        "name": "Beverages"
      },
      "id": "5ZYQZZ2IECPVJ2IJ5KQPRDC3",
      "is_deleted": false,
      "present_at_all_locations": true,
      "type": "CATEGORY",
      "updated_at": "2017-02-21T14:50:26.495Z",
      "version": 1487688626495
    },
    {
      "id": "L5R47DGBZOOVKCAFIXC56AEN",
      "is_deleted": false,
      "present_at_all_locations": true,
      "tax_data": {
        "calculation_phase": "TAX_SUBTOTAL_PHASE",
        "enabled": true,
        "inclusion_type": "ADDITIVE",
        "name": "Sales Tax",
        "percentage": "5.0"
      },
      "type": "TAX",
      "updated_at": "2017-02-21T14:50:26.495Z",
      "version": 1487688626495
    }
  ]
}
```

