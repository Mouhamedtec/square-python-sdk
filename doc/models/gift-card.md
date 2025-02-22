
# Gift Card

Represents a Square gift card.

## Structure

`Gift Card`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-assigned ID of the gift card. |
| `type` | [`str (Gift Card Type)`](../../doc/models/gift-card-type.md) | Required | Indicates the gift card type. |
| `gan_source` | [`str (Gift Card GAN Source)`](../../doc/models/gift-card-gan-source.md) | Optional | Indicates the source that generated the gift card<br>account number (GAN). |
| `state` | [`str (Gift Card Status)`](../../doc/models/gift-card-status.md) | Optional | Indicates the gift card state. |
| `balance_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `gan` | `string` | Optional | The gift card account number (GAN). Buyers can use the GAN to make purchases or check<br>the gift card balance. |
| `created_at` | `string` | Optional | The timestamp when the gift card was created, in RFC 3339 format.<br>In the case of a digital gift card, it is the time when you create a card<br>(using the Square Point of Sale application, Seller Dashboard, or Gift Cards API).  <br>In the case of a plastic gift card, it is the time when Square associates the card with the<br>seller at the time of activation. |
| `customer_ids` | `List of string` | Optional | The IDs of the [customer profiles](../../doc/models/customer.md) to whom this gift card is linked. |

## Example (as JSON)

```json
{
  "id": null,
  "type": "PHYSICAL",
  "gan_source": null,
  "state": null,
  "balance_money": null,
  "gan": null,
  "created_at": null,
  "customer_ids": null
}
```

