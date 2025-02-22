
# Loyalty Event Adjust Points

Provides metadata when the event `type` is `ADJUST_POINTS`.

## Structure

`Loyalty Event Adjust Points`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_program_id` | `string` | Optional | The Square-assigned ID of the [loyalty program](../../doc/models/loyalty-program.md).<br>**Constraints**: *Maximum Length*: `36` |
| `points` | `int` | Required | The number of points added or removed. |
| `reason` | `string` | Optional | The reason for the adjustment of points. |

## Example (as JSON)

```json
{
  "loyalty_program_id": null,
  "points": 236,
  "reason": null
}
```

