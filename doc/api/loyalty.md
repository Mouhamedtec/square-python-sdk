# Loyalty

```python
loyalty_api = client.loyalty
```

## Class Name

`LoyaltyApi`

## Methods

* [Create Loyalty Account](../../doc/api/loyalty.md#create-loyalty-account)
* [Search Loyalty Accounts](../../doc/api/loyalty.md#search-loyalty-accounts)
* [Retrieve Loyalty Account](../../doc/api/loyalty.md#retrieve-loyalty-account)
* [Accumulate Loyalty Points](../../doc/api/loyalty.md#accumulate-loyalty-points)
* [Adjust Loyalty Points](../../doc/api/loyalty.md#adjust-loyalty-points)
* [Search Loyalty Events](../../doc/api/loyalty.md#search-loyalty-events)
* [List Loyalty Programs](../../doc/api/loyalty.md#list-loyalty-programs)
* [Retrieve Loyalty Program](../../doc/api/loyalty.md#retrieve-loyalty-program)
* [Calculate Loyalty Points](../../doc/api/loyalty.md#calculate-loyalty-points)
* [Create Loyalty Reward](../../doc/api/loyalty.md#create-loyalty-reward)
* [Search Loyalty Rewards](../../doc/api/loyalty.md#search-loyalty-rewards)
* [Delete Loyalty Reward](../../doc/api/loyalty.md#delete-loyalty-reward)
* [Retrieve Loyalty Reward](../../doc/api/loyalty.md#retrieve-loyalty-reward)
* [Redeem Loyalty Reward](../../doc/api/loyalty.md#redeem-loyalty-reward)


# Create Loyalty Account

Creates a loyalty account. To create a loyalty account, you must provide the `program_id` and a `mapping` with the `phone_number` of the buyer.

```python
def create_loyalty_account(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Loyalty Account Request`](../../doc/models/create-loyalty-account-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Loyalty Account Response`](../../doc/models/create-loyalty-account-response.md)

## Example Usage

```python
body = {}
body['loyalty_account'] = {}
body['loyalty_account']['program_id'] = 'd619f755-2d17-41f3-990d-c04ecedd64dd'
body['loyalty_account']['mapping'] = {}
body['loyalty_account']['mapping']['phone_number'] = '+14155551234'
body['idempotency_key'] = 'ec78c477-b1c3-4899-a209-a4e71337c996'

result = loyalty_api.create_loyalty_account(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Loyalty Accounts

Searches for loyalty accounts in a loyalty program.

You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty `query` object or omit it entirely.

Search results are sorted by `created_at` in ascending order.

```python
def search_loyalty_accounts(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Loyalty Accounts Request`](../../doc/models/search-loyalty-accounts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Loyalty Accounts Response`](../../doc/models/search-loyalty-accounts-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['mappings'] = []

body['query']['mappings'].append({})
body['query']['mappings'][0]['phone_number'] = '+14155551234'

body['limit'] = 10

result = loyalty_api.search_loyalty_accounts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Loyalty Account

Retrieves a loyalty account.

```python
def retrieve_loyalty_account(self,
                            account_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The ID of the [loyalty account](../../doc/models/loyalty-account.md) to retrieve. |

## Response Type

[`Retrieve Loyalty Account Response`](../../doc/models/retrieve-loyalty-account-response.md)

## Example Usage

```python
account_id = 'account_id2'

result = loyalty_api.retrieve_loyalty_account(account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Accumulate Loyalty Points

Adds points to a loyalty account.

- If you are using the Orders API to manage orders, you only provide the `order_id`.
  The endpoint reads the order to compute points to add to the buyer's account.
- If you are not using the Orders API to manage orders,
  you first perform a client-side computation to compute the points.  
  For spend-based and visit-based programs, you can first call
  [CalculateLoyaltyPoints](../../doc/api/loyalty.md#calculate-loyalty-points) to compute the points  
  that you provide to this endpoint.

```python
def accumulate_loyalty_points(self,
                             account_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The [loyalty account](../../doc/models/loyalty-account.md) ID to which to add the points. |
| `body` | [`Accumulate Loyalty Points Request`](../../doc/models/accumulate-loyalty-points-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Accumulate Loyalty Points Response`](../../doc/models/accumulate-loyalty-points-response.md)

## Example Usage

```python
account_id = 'account_id2'
body = {}
body['accumulate_points'] = {}
body['accumulate_points']['order_id'] = 'RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY'
body['idempotency_key'] = '58b90739-c3e8-4b11-85f7-e636d48d72cb'
body['location_id'] = 'P034NEENMD09F'

result = loyalty_api.accumulate_loyalty_points(account_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Adjust Loyalty Points

Adds points to or subtracts points from a buyer's account.

Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
[AccumulateLoyaltyPoints](../../doc/api/loyalty.md#accumulate-loyalty-points)
to add points when a buyer pays for the purchase.

```python
def adjust_loyalty_points(self,
                         account_id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The ID of the [loyalty account](../../doc/models/loyalty-account.md) in which to adjust the points. |
| `body` | [`Adjust Loyalty Points Request`](../../doc/models/adjust-loyalty-points-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Adjust Loyalty Points Response`](../../doc/models/adjust-loyalty-points-response.md)

## Example Usage

```python
account_id = 'account_id2'
body = {}
body['idempotency_key'] = 'bc29a517-3dc9-450e-aa76-fae39ee849d1'
body['adjust_points'] = {}
body['adjust_points']['points'] = 10
body['adjust_points']['reason'] = 'Complimentary points'

result = loyalty_api.adjust_loyalty_points(account_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Loyalty Events

Searches for loyalty events.

A Square loyalty program maintains a ledger of events that occur during the lifetime of a
buyer's loyalty account. Each change in the point balance
(for example, points earned, points redeemed, and points expired) is
recorded in the ledger. Using this endpoint, you can search the ledger for events.

Search results are sorted by `created_at` in descending order.

```python
def search_loyalty_events(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Loyalty Events Request`](../../doc/models/search-loyalty-events-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Loyalty Events Response`](../../doc/models/search-loyalty-events-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['order_filter'] = {}
body['query']['filter']['order_filter']['order_id'] = 'PyATxhYLfsMqpVkcKJITPydgEYfZY'
body['limit'] = 30

result = loyalty_api.search_loyalty_events(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Loyalty Programs

**This endpoint is deprecated.**

Returns a list of loyalty programs in the seller's account.
Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

Replaced with [RetrieveLoyaltyProgram](../../doc/api/loyalty.md#retrieve-loyalty-program) when used with the keyword `main`.

```python
def list_loyalty_programs(self)
```

## Response Type

[`List Loyalty Programs Response`](../../doc/models/list-loyalty-programs-response.md)

## Example Usage

```python
result = loyalty_api.list_loyalty_programs()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Loyalty Program

Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.

Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

```python
def retrieve_loyalty_program(self,
                            program_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_id` | `string` | Template, Required | The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller. |

## Response Type

[`Retrieve Loyalty Program Response`](../../doc/models/retrieve-loyalty-program-response.md)

## Example Usage

```python
program_id = 'program_id0'

result = loyalty_api.retrieve_loyalty_program(program_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Calculate Loyalty Points

Calculates the points a purchase earns.

- If you are using the Orders API to manage orders, you provide the `order_id` in the request. The
  endpoint calculates the points by reading the order.
- If you are not using the Orders API to manage orders, you provide the purchase amount in
  the request for the endpoint to calculate the points.

An application might call this endpoint to show the points that a buyer can earn with the
specific purchase.

For spend-based and visit-based programs, the `tax_mode` setting of the accrual rule indicates how taxes should be treated for loyalty points accrual.

```python
def calculate_loyalty_points(self,
                            program_id,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_id` | `string` | Template, Required | The [loyalty program](../../doc/models/loyalty-program.md) ID, which defines the rules for accruing points. |
| `body` | [`Calculate Loyalty Points Request`](../../doc/models/calculate-loyalty-points-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Calculate Loyalty Points Response`](../../doc/models/calculate-loyalty-points-response.md)

## Example Usage

```python
program_id = 'program_id0'
body = {}
body['order_id'] = 'RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY'

result = loyalty_api.calculate_loyalty_points(program_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Loyalty Reward

Creates a loyalty reward. In the process, the endpoint does following:

- Uses the `reward_tier_id` in the request to determine the number of points
  to lock for this reward.
- If the request includes `order_id`, it adds the reward and related discount to the order.

After a reward is created, the points are locked and
not available for the buyer to redeem another reward.

```python
def create_loyalty_reward(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Loyalty Reward Request`](../../doc/models/create-loyalty-reward-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Loyalty Reward Response`](../../doc/models/create-loyalty-reward-response.md)

## Example Usage

```python
body = {}
body['reward'] = {}
body['reward']['loyalty_account_id'] = '5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd'
body['reward']['reward_tier_id'] = 'e1b39225-9da5-43d1-a5db-782cdd8ad94f'
body['reward']['order_id'] = 'RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY'
body['idempotency_key'] = '18c2e5ea-a620-4b1f-ad60-7b167285e451'

result = loyalty_api.create_loyalty_reward(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Loyalty Rewards

Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for all loyalty accounts.
If you include a `query` object, `loyalty_account_id` is required and `status` is  optional.

If you know a reward ID, use the
[RetrieveLoyaltyReward](../../doc/api/loyalty.md#retrieve-loyalty-reward) endpoint.

Search results are sorted by `updated_at` in descending order.

```python
def search_loyalty_rewards(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Loyalty Rewards Request`](../../doc/models/search-loyalty-rewards-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Loyalty Rewards Response`](../../doc/models/search-loyalty-rewards-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['loyalty_account_id'] = '5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd'
body['limit'] = 10

result = loyalty_api.search_loyalty_rewards(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Loyalty Reward

Deletes a loyalty reward by doing the following:

- Returns the loyalty points back to the loyalty account.
- If an order ID was specified when the reward was created
  (see [CreateLoyaltyReward](../../doc/api/loyalty.md#create-loyalty-reward)),
  it updates the order by removing the reward and related
  discounts.

You cannot delete a reward that has reached the terminal state (REDEEMED).

```python
def delete_loyalty_reward(self,
                         reward_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reward_id` | `string` | Template, Required | The ID of the [loyalty reward](../../doc/models/loyalty-reward.md) to delete. |

## Response Type

[`Delete Loyalty Reward Response`](../../doc/models/delete-loyalty-reward-response.md)

## Example Usage

```python
reward_id = 'reward_id4'

result = loyalty_api.delete_loyalty_reward(reward_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Loyalty Reward

Retrieves a loyalty reward.

```python
def retrieve_loyalty_reward(self,
                           reward_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reward_id` | `string` | Template, Required | The ID of the [loyalty reward](../../doc/models/loyalty-reward.md) to retrieve. |

## Response Type

[`Retrieve Loyalty Reward Response`](../../doc/models/retrieve-loyalty-reward-response.md)

## Example Usage

```python
reward_id = 'reward_id4'

result = loyalty_api.retrieve_loyalty_reward(reward_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Redeem Loyalty Reward

Redeems a loyalty reward.

The endpoint sets the reward to the `REDEEMED` terminal state.

If you are using your own order processing system (not using the
Orders API), you call this endpoint after the buyer paid for the
purchase.

After the reward reaches the terminal state, it cannot be deleted.
In other words, points used for the reward cannot be returned
to the account.

```python
def redeem_loyalty_reward(self,
                         reward_id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reward_id` | `string` | Template, Required | The ID of the [loyalty reward](../../doc/models/loyalty-reward.md) to redeem. |
| `body` | [`Redeem Loyalty Reward Request`](../../doc/models/redeem-loyalty-reward-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Redeem Loyalty Reward Response`](../../doc/models/redeem-loyalty-reward-response.md)

## Example Usage

```python
reward_id = 'reward_id4'
body = {}
body['idempotency_key'] = '98adc7f7-6963-473b-b29c-f3c9cdd7d994'
body['location_id'] = 'P034NEENMD09F'

result = loyalty_api.redeem_loyalty_reward(reward_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

