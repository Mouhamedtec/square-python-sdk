# Gift Cards

```python
gift_cards_api = client.gift_cards
```

## Class Name

`GiftCardsApi`

## Methods

* [List Gift Cards](../../doc/api/gift-cards.md#list-gift-cards)
* [Create Gift Card](../../doc/api/gift-cards.md#create-gift-card)
* [Retrieve Gift Card From GAN](../../doc/api/gift-cards.md#retrieve-gift-card-from-gan)
* [Retrieve Gift Card From Nonce](../../doc/api/gift-cards.md#retrieve-gift-card-from-nonce)
* [Link Customer to Gift Card](../../doc/api/gift-cards.md#link-customer-to-gift-card)
* [Unlink Customer From Gift Card](../../doc/api/gift-cards.md#unlink-customer-from-gift-card)
* [Retrieve Gift Card](../../doc/api/gift-cards.md#retrieve-gift-card)


# List Gift Cards

Lists all gift cards. You can specify optional filters to retrieve
a subset of the gift cards.

```python
def list_gift_cards(self,
                   mtype=None,
                   state=None,
                   limit=None,
                   cursor=None,
                   customer_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Query, Optional | If a [type](../../doc/models/gift-card-type.md) is provided, the endpoint returns gift cards of the specified type.<br>Otherwise, the endpoint returns gift cards of all types. |
| `state` | `string` | Query, Optional | If a [state](../../doc/models/gift-card-status.md) is provided, the endpoint returns the gift cards in the specified state.<br>Otherwise, the endpoint returns the gift cards of all states. |
| `limit` | `int` | Query, Optional | If a limit is provided, the endpoint returns only the specified number of results per page.<br>The maximum value is 50. The default value is 30.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>If a cursor is not provided, the endpoint returns the first page of the results.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `customer_id` | `string` | Query, Optional | If a customer ID is provided, the endpoint returns only the gift cards linked to the specified customer. |

## Response Type

[`List Gift Cards Response`](../../doc/models/list-gift-cards-response.md)

## Example Usage

```python
result = gift_cards_api.list_gift_cards()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Gift Card

Creates a digital gift card or registers a physical (plastic) gift card. After the gift card
is created, you must call [CreateGiftCardActivity](../../doc/api/gift-card-activities.md#create-gift-card-activity)
to activate the card with an initial balance before it can be used for payment.

```python
def create_gift_card(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Gift Card Request`](../../doc/models/create-gift-card-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Gift Card Response`](../../doc/models/create-gift-card-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = 'NC9Tm69EjbjtConu'
body['location_id'] = '81FN9BNFZTKS4'
body['gift_card'] = {}
body['gift_card']['type'] = 'DIGITAL'

result = gift_cards_api.create_gift_card(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Gift Card From GAN

Retrieves a gift card using the gift card account number (GAN).

```python
def retrieve_gift_card_from_gan(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Retrieve Gift Card From GAN Request`](../../doc/models/retrieve-gift-card-from-gan-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Retrieve Gift Card From GAN Response`](../../doc/models/retrieve-gift-card-from-gan-response.md)

## Example Usage

```python
body = {}
body['gan'] = '7783320001001635'

result = gift_cards_api.retrieve_gift_card_from_gan(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Gift Card From Nonce

Retrieves a gift card using a secure payment token that represents the gift card.

```python
def retrieve_gift_card_from_nonce(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Retrieve Gift Card From Nonce Request`](../../doc/models/retrieve-gift-card-from-nonce-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Retrieve Gift Card From Nonce Response`](../../doc/models/retrieve-gift-card-from-nonce-response.md)

## Example Usage

```python
body = {}
body['nonce'] = 'cnon:7783322135245171'

result = gift_cards_api.retrieve_gift_card_from_nonce(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Link Customer to Gift Card

Links a customer to a gift card, which is also referred to as adding a card on file.

```python
def link_customer_to_gift_card(self,
                              gift_card_id,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gift_card_id` | `string` | Template, Required | The ID of the gift card to be linked. |
| `body` | [`Link Customer to Gift Card Request`](../../doc/models/link-customer-to-gift-card-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Link Customer to Gift Card Response`](../../doc/models/link-customer-to-gift-card-response.md)

## Example Usage

```python
gift_card_id = 'gift_card_id8'
body = {}
body['customer_id'] = 'GKY0FZ3V717AH8Q2D821PNT2ZW'

result = gift_cards_api.link_customer_to_gift_card(gift_card_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Unlink Customer From Gift Card

Unlinks a customer from a gift card, which is also referred to as removing a card on file.

```python
def unlink_customer_from_gift_card(self,
                                  gift_card_id,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gift_card_id` | `string` | Template, Required | The ID of the gift card to be unlinked. |
| `body` | [`Unlink Customer From Gift Card Request`](../../doc/models/unlink-customer-from-gift-card-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Unlink Customer From Gift Card Response`](../../doc/models/unlink-customer-from-gift-card-response.md)

## Example Usage

```python
gift_card_id = 'gift_card_id8'
body = {}
body['customer_id'] = 'GKY0FZ3V717AH8Q2D821PNT2ZW'

result = gift_cards_api.unlink_customer_from_gift_card(gift_card_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Gift Card

Retrieves a gift card using the gift card ID.

```python
def retrieve_gift_card(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The ID of the gift card to retrieve. |

## Response Type

[`Retrieve Gift Card Response`](../../doc/models/retrieve-gift-card-response.md)

## Example Usage

```python
id = 'id0'

result = gift_cards_api.retrieve_gift_card(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

