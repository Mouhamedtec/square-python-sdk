
# Terminal Refund Query Filter

## Structure

`Terminal Refund Query Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Optional | `TerminalRefund` objects associated with a specific device. If no device is specified, then all<br>`TerminalRefund` objects for the signed-in account are displayed. |
| `created_at` | [`Time Range`](../../doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC 3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevant endpoint-specific documentation to determine<br>how time ranges are handled. |
| `status` | `string` | Optional | Filtered results with the desired status of the `TerminalRefund`.<br>Options: `PENDING`, `IN_PROGRESS`, `CANCEL_REQUESTED`, `CANCELED`, or `COMPLETED`. |

## Example (as JSON)

```json
{
  "device_id": null,
  "created_at": null,
  "status": null
}
```

