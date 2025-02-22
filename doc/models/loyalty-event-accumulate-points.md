
# Loyalty Event Accumulate Points

Provides metadata when the event `type` is `ACCUMULATE_POINTS`.

## Structure

`Loyalty Event Accumulate Points`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_program_id` | `string` | Optional | The ID of the [loyalty program](../../doc/models/loyalty-program.md).<br>**Constraints**: *Maximum Length*: `36` |
| `points` | `int` | Optional | The number of points accumulated by the event.<br>**Constraints**: `>= 1` |
| `order_id` | `string` | Optional | The ID of the [order](../../doc/models/order.md) for which the buyer accumulated the points.<br>This field is returned only if the Orders API is used to process orders. |

## Example (as JSON)

```json
{
  "loyalty_program_id": null,
  "points": null,
  "order_id": null
}
```

