
# V1 Payment Modifier

V1PaymentModifier

## Structure

`V1 Payment Modifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The modifier option's name. |
| `applied_money` | [`V1 Money`](../../doc/models/v1-money.md) | Optional | - |
| `modifier_option_id` | `string` | Optional | The ID of the applied modifier option, if available. Modifier options applied in older versions of Square Register might not have an ID. |

## Example (as JSON)

```json
{
  "name": null,
  "applied_money": null,
  "modifier_option_id": null
}
```

