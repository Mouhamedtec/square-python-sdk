# Terminal

```python
terminal_api = client.terminal
```

## Class Name

`TerminalApi`

## Methods

* [Create Terminal Action](../../doc/api/terminal.md#create-terminal-action)
* [Search Terminal Actions](../../doc/api/terminal.md#search-terminal-actions)
* [Get Terminal Action](../../doc/api/terminal.md#get-terminal-action)
* [Cancel Terminal Action](../../doc/api/terminal.md#cancel-terminal-action)
* [Create Terminal Checkout](../../doc/api/terminal.md#create-terminal-checkout)
* [Search Terminal Checkouts](../../doc/api/terminal.md#search-terminal-checkouts)
* [Get Terminal Checkout](../../doc/api/terminal.md#get-terminal-checkout)
* [Cancel Terminal Checkout](../../doc/api/terminal.md#cancel-terminal-checkout)
* [Create Terminal Refund](../../doc/api/terminal.md#create-terminal-refund)
* [Search Terminal Refunds](../../doc/api/terminal.md#search-terminal-refunds)
* [Get Terminal Refund](../../doc/api/terminal.md#get-terminal-refund)
* [Cancel Terminal Refund](../../doc/api/terminal.md#cancel-terminal-refund)


# Create Terminal Action

Creates a Terminal action request and sends it to the specified device to take a payment
for the requested amount.

```python
def create_terminal_action(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Terminal Action Request`](../../doc/models/create-terminal-action-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Terminal Action Response`](../../doc/models/create-terminal-action-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = 'thahn-70e75c10-47f7-4ab6-88cc-aaa4076d065e'
body['action'] = {}
body['action']['device_id'] = '{{DEVICE_ID}}'
body['action']['deadline_duration'] = 'PT5M'
body['action']['type'] = 'SAVE_CARD'
body['action']['save_card_options'] = {}
body['action']['save_card_options']['customer_id'] = '{{CUSTOMER_ID}}'
body['action']['save_card_options']['reference_id'] = 'user-id-1'

result = terminal_api.create_terminal_action(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Terminal Actions

Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal action requests are available for 30 days.

```python
def search_terminal_actions(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Terminal Actions Request`](../../doc/models/search-terminal-actions-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Terminal Actions Response`](../../doc/models/search-terminal-actions-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['created_at'] = {}
body['query']['filter']['created_at']['start_at'] = '2022-04-01T00:00:00.000Z'
body['query']['sort'] = {}
body['query']['sort']['sort_order'] = 'DESC'
body['limit'] = 2

result = terminal_api.search_terminal_actions(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Terminal Action

Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.

```python
def get_terminal_action(self,
                       action_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_id` | `string` | Template, Required | Unique ID for the desired `TerminalAction` |

## Response Type

[`Get Terminal Action Response`](../../doc/models/get-terminal-action-response.md)

## Example Usage

```python
action_id = 'action_id6'

result = terminal_api.get_terminal_action(action_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Terminal Action

Cancels a Terminal action request if the status of the request permits it.

```python
def cancel_terminal_action(self,
                          action_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_id` | `string` | Template, Required | Unique ID for the desired `TerminalAction` |

## Response Type

[`Cancel Terminal Action Response`](../../doc/models/cancel-terminal-action-response.md)

## Example Usage

```python
action_id = 'action_id6'

result = terminal_api.cancel_terminal_action(action_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Terminal Checkout

Creates a Terminal checkout request and sends it to the specified device to take a payment
for the requested amount.

```python
def create_terminal_checkout(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Terminal Checkout Request`](../../doc/models/create-terminal-checkout-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Terminal Checkout Response`](../../doc/models/create-terminal-checkout-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = '28a0c3bc-7839-11ea-bc55-0242ac130003'
body['checkout'] = {}
body['checkout']['amount_money'] = {}
body['checkout']['amount_money']['amount'] = 2610
body['checkout']['amount_money']['currency'] = 'USD'
body['checkout']['reference_id'] = 'id11572'
body['checkout']['note'] = 'A brief note'
body['checkout']['device_options'] = {}
body['checkout']['device_options']['device_id'] = 'dbb5d83a-7838-11ea-bc55-0242ac130003'

result = terminal_api.create_terminal_checkout(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Terminal Checkouts

Returns a filtered list of Terminal checkout requests created by the application making the request. Only Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout requests are available for 30 days.

```python
def search_terminal_checkouts(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Terminal Checkouts Request`](../../doc/models/search-terminal-checkouts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Terminal Checkouts Response`](../../doc/models/search-terminal-checkouts-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['status'] = 'COMPLETED'
body['limit'] = 2

result = terminal_api.search_terminal_checkouts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Terminal Checkout

Retrieves a Terminal checkout request by `checkout_id`. Terminal checkout requests are available for 30 days.

```python
def get_terminal_checkout(self,
                         checkout_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_id` | `string` | Template, Required | The unique ID for the desired `TerminalCheckout`. |

## Response Type

[`Get Terminal Checkout Response`](../../doc/models/get-terminal-checkout-response.md)

## Example Usage

```python
checkout_id = 'checkout_id8'

result = terminal_api.get_terminal_checkout(checkout_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Terminal Checkout

Cancels a Terminal checkout request if the status of the request permits it.

```python
def cancel_terminal_checkout(self,
                            checkout_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_id` | `string` | Template, Required | The unique ID for the desired `TerminalCheckout`. |

## Response Type

[`Cancel Terminal Checkout Response`](../../doc/models/cancel-terminal-checkout-response.md)

## Example Usage

```python
checkout_id = 'checkout_id8'

result = terminal_api.cancel_terminal_checkout(checkout_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Terminal Refund

Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments should use the Refunds API. For more information, see [Refunds API](../../doc/api/refunds.md).

```python
def create_terminal_refund(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Terminal Refund Request`](../../doc/models/create-terminal-refund-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Terminal Refund Response`](../../doc/models/create-terminal-refund-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = '402a640b-b26f-401f-b406-46f839590c04'
body['refund'] = {}
body['refund']['payment_id'] = '5O5OvgkcNUhl7JBuINflcjKqUzXZY'
body['refund']['amount_money'] = {}
body['refund']['amount_money']['amount'] = 111
body['refund']['amount_money']['currency'] = 'CAD'
body['refund']['reason'] = 'Returning items'
body['refund']['device_id'] = 'f72dfb8e-4d65-4e56-aade-ec3fb8d33291'

result = terminal_api.create_terminal_refund(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Terminal Refunds

Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request. Terminal refund requests are available for 30 days.

```python
def search_terminal_refunds(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Terminal Refunds Request`](../../doc/models/search-terminal-refunds-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Terminal Refunds Response`](../../doc/models/search-terminal-refunds-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['status'] = 'COMPLETED'
body['limit'] = 1

result = terminal_api.search_terminal_refunds(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Terminal Refund

Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.

```python
def get_terminal_refund(self,
                       terminal_refund_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_refund_id` | `string` | Template, Required | The unique ID for the desired `TerminalRefund`. |

## Response Type

[`Get Terminal Refund Response`](../../doc/models/get-terminal-refund-response.md)

## Example Usage

```python
terminal_refund_id = 'terminal_refund_id0'

result = terminal_api.get_terminal_refund(terminal_refund_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Terminal Refund

Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

```python
def cancel_terminal_refund(self,
                          terminal_refund_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal_refund_id` | `string` | Template, Required | The unique ID for the desired `TerminalRefund`. |

## Response Type

[`Cancel Terminal Refund Response`](../../doc/models/cancel-terminal-refund-response.md)

## Example Usage

```python
terminal_refund_id = 'terminal_refund_id0'

result = terminal_api.cancel_terminal_refund(terminal_refund_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

