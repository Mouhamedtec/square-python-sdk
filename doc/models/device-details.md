
# Device Details

Details about the device that took the payment.

## Structure

`Device Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Optional | The Square-issued ID of the device.<br>**Constraints**: *Maximum Length*: `255` |
| `device_installation_id` | `string` | Optional | The Square-issued installation ID for the device.<br>**Constraints**: *Maximum Length*: `255` |
| `device_name` | `string` | Optional | The name of the device set by the seller.<br>**Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "device_id": null,
  "device_installation_id": null,
  "device_name": null
}
```

