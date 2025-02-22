
# Update Customer Custom Attribute Definition Response

Represents an [UpdateCustomerCustomAttributeDefinition](../../doc/api/customer-custom-attributes.md#update-customer-custom-attribute-definition) response.
Either `custom_attribute_definition` or `errors` is present in the response.

## Structure

`Update Customer Custom Attribute Definition Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_attribute_definition` | [`Custom Attribute Definition`](../../doc/models/custom-attribute-definition.md) | Optional | Represents a definition for custom attribute values. A custom attribute definition<br>specifies the key, visibility, schema, and other properties for a custom attribute. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "custom_attribute_definition": {
    "created_at": "2022-04-26T15:27:30Z",
    "description": "Update the description as desired.",
    "key": "favoritemovie",
    "name": "Favorite Movie",
    "schema": null,
    "source_application": {
      "application_id": "sq0idp-vYnkl5YF8SiWyJtfrKMhNA"
    },
    "updated_at": "2022-04-26T15:39:38Z",
    "version": 2,
    "visibility": "VISIBILITY_READ_ONLY"
  }
}
```

