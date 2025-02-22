# Checkout

```python
checkout_api = client.checkout
```

## Class Name

`CheckoutApi`

## Methods

* [Create Checkout](../../doc/api/checkout.md#create-checkout)
* [List Payment Links](../../doc/api/checkout.md#list-payment-links)
* [Create Payment Link](../../doc/api/checkout.md#create-payment-link)
* [Delete Payment Link](../../doc/api/checkout.md#delete-payment-link)
* [Retrieve Payment Link](../../doc/api/checkout.md#retrieve-payment-link)
* [Update Payment Link](../../doc/api/checkout.md#update-payment-link)


# Create Checkout

Links a `checkoutId` to a `checkout_page_url` that customers are
directed to in order to provide their payment information using a
payment processing workflow hosted on connect.squareup.com.

NOTE: The Checkout API has been updated with new features.
For more information, see [Checkout API highlights](https://developer.squareup.com/docs/checkout-api#checkout-api-highlights).
We recommend that you use the new [CreatePaymentLink](../../doc/api/checkout.md#create-payment-link) 
endpoint in place of this previously released endpoint.

```python
def create_checkout(self,
                   location_id,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the business location to associate the checkout with. |
| `body` | [`Create Checkout Request`](../../doc/models/create-checkout-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Checkout Response`](../../doc/models/create-checkout-response.md)

## Example Usage

```python
location_id = 'location_id4'
body = {}
body['idempotency_key'] = '86ae1696-b1e3-4328-af6d-f1e04d947ad6'
body['order'] = {}
body['order']['order'] = {}
body['order']['order']['location_id'] = 'location_id'
body['order']['order']['reference_id'] = 'reference_id'
body['order']['order']['customer_id'] = 'customer_id'
body['order']['order']['line_items'] = []

body['order']['order']['line_items'].append({})
body['order']['order']['line_items'][0]['name'] = 'Printed T Shirt'
body['order']['order']['line_items'][0]['quantity'] = '2'
body['order']['order']['line_items'][0]['applied_taxes'] = []

body['order']['order']['line_items'][0]['applied_taxes'].append({})
body['order']['order']['line_items'][0]['applied_taxes'][0]['tax_uid'] = '38ze1696-z1e3-5628-af6d-f1e04d947fg3'

body['order']['order']['line_items'][0]['applied_discounts'] = []

body['order']['order']['line_items'][0]['applied_discounts'].append({})
body['order']['order']['line_items'][0]['applied_discounts'][0]['discount_uid'] = '56ae1696-z1e3-9328-af6d-f1e04d947gd4'

body['order']['order']['line_items'][0]['base_price_money'] = {}
body['order']['order']['line_items'][0]['base_price_money']['amount'] = 1500
body['order']['order']['line_items'][0]['base_price_money']['currency'] = 'USD'

body['order']['order']['line_items'].append({})
body['order']['order']['line_items'][1]['name'] = 'Slim Jeans'
body['order']['order']['line_items'][1]['quantity'] = '1'
body['order']['order']['line_items'][1]['base_price_money'] = {}
body['order']['order']['line_items'][1]['base_price_money']['amount'] = 2500
body['order']['order']['line_items'][1]['base_price_money']['currency'] = 'USD'

body['order']['order']['line_items'].append({})
body['order']['order']['line_items'][2]['name'] = 'Woven Sweater'
body['order']['order']['line_items'][2]['quantity'] = '3'
body['order']['order']['line_items'][2]['base_price_money'] = {}
body['order']['order']['line_items'][2]['base_price_money']['amount'] = 3500
body['order']['order']['line_items'][2]['base_price_money']['currency'] = 'USD'

body['order']['order']['taxes'] = []

body['order']['order']['taxes'].append({})
body['order']['order']['taxes'][0]['uid'] = '38ze1696-z1e3-5628-af6d-f1e04d947fg3'
body['order']['order']['taxes'][0]['type'] = 'INCLUSIVE'
body['order']['order']['taxes'][0]['percentage'] = '7.75'
body['order']['order']['taxes'][0]['scope'] = 'LINE_ITEM'

body['order']['order']['discounts'] = []

body['order']['order']['discounts'].append({})
body['order']['order']['discounts'][0]['uid'] = '56ae1696-z1e3-9328-af6d-f1e04d947gd4'
body['order']['order']['discounts'][0]['type'] = 'FIXED_AMOUNT'
body['order']['order']['discounts'][0]['amount_money'] = {}
body['order']['order']['discounts'][0]['amount_money']['amount'] = 100
body['order']['order']['discounts'][0]['amount_money']['currency'] = 'USD'
body['order']['order']['discounts'][0]['scope'] = 'LINE_ITEM'

body['order']['idempotency_key'] = '12ae1696-z1e3-4328-af6d-f1e04d947gd4'
body['ask_for_shipping_address'] = True
body['merchant_support_email'] = 'merchant+support@website.com'
body['pre_populate_buyer_email'] = 'example@email.com'
body['pre_populate_shipping_address'] = {}
body['pre_populate_shipping_address']['address_line_1'] = '1455 Market St.'
body['pre_populate_shipping_address']['address_line_2'] = 'Suite 600'
body['pre_populate_shipping_address']['locality'] = 'San Francisco'
body['pre_populate_shipping_address']['administrative_district_level_1'] = 'CA'
body['pre_populate_shipping_address']['postal_code'] = '94103'
body['pre_populate_shipping_address']['country'] = 'US'
body['redirect_url'] = 'https://merchant.website.com/order-confirm'
body['additional_recipients'] = []

body['additional_recipients'].append({})
body['additional_recipients'][0]['location_id'] = '057P5VYJ4A5X1'
body['additional_recipients'][0]['description'] = 'Application fees'


result = checkout_api.create_checkout(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Payment Links

Lists all payment links.

```python
def list_payment_links(self,
                      cursor=None,
                      limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>If a cursor is not provided, the endpoint returns the first page of the results.<br>For more  information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |
| `limit` | `int` | Query, Optional | A limit on the number of results to return per page. The limit is advisory and<br>the implementation might return more or less results. If the supplied limit is negative, zero, or<br>greater than the maximum limit of 1000, it is ignored.<br><br>Default value: `100` |

## Response Type

[`List Payment Links Response`](../../doc/models/list-payment-links-response.md)

## Example Usage

```python
result = checkout_api.list_payment_links()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Payment Link

Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to pay for goods and services.

```python
def create_payment_link(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Payment Link Request`](../../doc/models/create-payment-link-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Payment Link Response`](../../doc/models/create-payment-link-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = 'cd9e25dc-d9f2-4430-aedb-61605070e95f'
body['quick_pay'] = {}
body['quick_pay']['name'] = 'Auto Detailing'
body['quick_pay']['price_money'] = {}
body['quick_pay']['price_money']['amount'] = 10000
body['quick_pay']['price_money']['currency'] = 'USD'
body['quick_pay']['location_id'] = 'A9Y43N9ABXZBP'

result = checkout_api.create_payment_link(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Payment Link

Deletes a payment link.

```python
def delete_payment_link(self,
                       id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The ID of the payment link to delete. |

## Response Type

[`Delete Payment Link Response`](../../doc/models/delete-payment-link-response.md)

## Example Usage

```python
id = 'id0'

result = checkout_api.delete_payment_link(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Payment Link

Retrieves a payment link.

```python
def retrieve_payment_link(self,
                         id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The ID of link to retrieve. |

## Response Type

[`Retrieve Payment Link Response`](../../doc/models/retrieve-payment-link-response.md)

## Example Usage

```python
id = 'id0'

result = checkout_api.retrieve_payment_link(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Payment Link

Updates a payment link. You can update the `payment_link` fields such as
`description`, `checkout_options`, and  `pre_populated_data`.
You cannot update other fields such as the `order_id`, `version`, `URL`, or `timestamp` field.

```python
def update_payment_link(self,
                       id,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The ID of the payment link to update. |
| `body` | [`Update Payment Link Request`](../../doc/models/update-payment-link-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Update Payment Link Response`](../../doc/models/update-payment-link-response.md)

## Example Usage

```python
id = 'id0'
body = {}
body['payment_link'] = {}
body['payment_link']['version'] = 1
body['payment_link']['checkout_options'] = {}
body['payment_link']['checkout_options']['ask_for_shipping_address'] = True

result = checkout_api.update_payment_link(id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

