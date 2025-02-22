
# Search Loyalty Events Request

A request to search for loyalty events.

## Structure

`Search Loyalty Events Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | [`Loyalty Event Query`](../../doc/models/loyalty-event-query.md) | Optional | Represents a query used to search for loyalty events. |
| `limit` | `int` | Optional | The maximum number of results to include in the response.<br>The last page might contain fewer events.<br>The default is 30 events.<br>**Constraints**: `>= 1`, `<= 30` |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |

## Example (as JSON)

```json
{
  "limit": 30,
  "query": {
    "filter": {
      "order_filter": {
        "order_id": "PyATxhYLfsMqpVkcKJITPydgEYfZY"
      }
    }
  }
}
```

