
# Order Line Item Pricing Blocklists Blocked Discount

A discount to block from applying to a line item. The discount must be
identified by either `discount_uid` or `discount_catalog_object_id`, but not both.

## Structure

`Order Line Item Pricing Blocklists Blocked Discount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `string` | Optional | A unique ID of the `BlockedDiscount` within the order.<br>**Constraints**: *Maximum Length*: `60` |
| `discount_uid` | `string` | Optional | The `uid` of the discount that should be blocked. Use this field to block<br>ad hoc discounts. For catalog discounts, use the `discount_catalog_object_id` field.<br>**Constraints**: *Maximum Length*: `60` |
| `discount_catalog_object_id` | `string` | Optional | The `catalog_object_id` of the discount that should be blocked.<br>Use this field to block catalog discounts. For ad hoc discounts, use the<br>`discount_uid` field.<br>**Constraints**: *Maximum Length*: `192` |

## Example (as JSON)

```json
{
  "uid": null,
  "discount_uid": null,
  "discount_catalog_object_id": null
}
```

