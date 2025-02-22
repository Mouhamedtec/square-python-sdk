
# Job Assignment

An object describing a job that a team member is assigned to.

## Structure

`Job Assignment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `job_title` | `string` | Required | The title of the job.<br>**Constraints**: *Minimum Length*: `1` |
| `pay_type` | [`str (Job Assignment Pay Type)`](../../doc/models/job-assignment-pay-type.md) | Required | Enumerates the possible pay types that a job can be assigned. |
| `hourly_rate` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `annual_rate` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `weekly_hours` | `int` | Optional | The planned hours per week for the job. Set if the job `PayType` is `SALARY`. |

## Example (as JSON)

```json
{
  "job_title": "job_title4",
  "pay_type": "NONE",
  "hourly_rate": null,
  "annual_rate": null,
  "weekly_hours": null
}
```

