# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.utilities.file_wrapper import FileWrapper
from square.api.base_api import BaseApi


class CatalogApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(CatalogApi, self).__init__(config, auth_managers)

    def batch_delete_catalog_objects(self,
                                     body):
        """Does a POST request to /v2/catalog/batch-delete.

        Deletes a set of [CatalogItem]($m/CatalogItem)s based on the
        provided list of target IDs and returns a set of successfully deleted
        IDs in
        the response. Deletion is a cascading event such that all children of
        the
        targeted object are also deleted. For example, deleting a CatalogItem
        will
        also delete all of its
        [CatalogItemVariation]($m/CatalogItemVariation)
        children.
        `BatchDeleteCatalogObjects` succeeds even if only a portion of the
        targeted
        IDs can be deleted. The response will only include IDs that were
        actually deleted.

        Args:
            body (BatchDeleteCatalogObjectsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/batch-delete'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def batch_retrieve_catalog_objects(self,
                                       body):
        """Does a POST request to /v2/catalog/batch-retrieve.

        Returns a set of objects based on the provided ID.
        Each [CatalogItem]($m/CatalogItem) returned in the set includes all of
        its
        child information including: all of its
        [CatalogItemVariation]($m/CatalogItemVariation) objects, references
        to
        its [CatalogModifierList]($m/CatalogModifierList) objects, and the ids
        of
        any [CatalogTax]($m/CatalogTax) objects that apply to it.

        Args:
            body (BatchRetrieveCatalogObjectsRequest): An object containing
                the fields to POST for the request.  See the corresponding
                object definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/batch-retrieve'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def batch_upsert_catalog_objects(self,
                                     body):
        """Does a POST request to /v2/catalog/batch-upsert.

        Creates or updates up to 10,000 target objects based on the provided
        list of objects. The target objects are grouped into batches and each
        batch is
        inserted/updated in an all-or-nothing manner. If an object within a
        batch is
        malformed in some way, or violates a database constraint, the entire
        batch
        containing that item will be disregarded. However, other batches in
        the same
        request may still succeed. Each batch may contain up to 1,000 objects,
        and
        batches will be processed in order as long as the total object count
        for the
        request (items, variations, modifier lists, discounts, and taxes) is
        no more
        than 10,000.

        Args:
            body (BatchUpsertCatalogObjectsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/batch-upsert'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_catalog_image(self,
                             request=None,
                             image_file=None):
        """Does a POST request to /v2/catalog/images.

        Uploads an image file to be represented by a
        [CatalogImage]($m/CatalogImage) object that can be linked to an
        existing
        [CatalogObject]($m/CatalogObject) instance. The resulting
        `CatalogImage` is unattached to any `CatalogObject` if the
        `object_id`
        is not specified.
        This `CreateCatalogImage` endpoint accepts HTTP multipart/form-data
        requests with a JSON part and an image file part in
        JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            request (CreateCatalogImageRequest, optional): TODO: type
                description here.
            image_file (typing.BinaryIO, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/images'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        if isinstance(image_file, FileWrapper):
            image_file_wrapper = image_file.file_stream
            image_file_content_type = image_file.content_type
        else:
            image_file_wrapper = image_file
            image_file_content_type = 'image/jpeg'

        # Prepare files
        _files = {
            'request': (None, APIHelper.json_serialize(request), 'application/json; charset=utf-8'),
            'image_file': (image_file_wrapper.name, image_file_wrapper, image_file_content_type)
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, files=_files)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_catalog_image(self,
                             image_id,
                             request=None,
                             image_file=None):
        """Does a PUT request to /v2/catalog/images/{image_id}.

        Uploads a new image file to replace the existing one in the specified
        [CatalogImage]($m/CatalogImage) object. 
        This `UpdateCatalogImage` endpoint accepts HTTP multipart/form-data
        requests with a JSON part and an image file part in
        JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            image_id (string): The ID of the `CatalogImage` object to update
                the encapsulated image file.
            request (UpdateCatalogImageRequest, optional): TODO: type
                description here.
            image_file (typing.BinaryIO, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/images/{image_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'image_id': {'value': image_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        if isinstance(image_file, FileWrapper):
            image_file_wrapper = image_file.file_stream
            image_file_content_type = image_file.content_type
        else:
            image_file_wrapper = image_file
            image_file_content_type = 'image/jpeg'

        # Prepare files
        _files = {
            'request': (None, APIHelper.json_serialize(request), 'application/json; charset=utf-8'),
            'image_file': (image_file_wrapper.name, image_file_wrapper, image_file_content_type)
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, files=_files)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def catalog_info(self):
        """Does a GET request to /v2/catalog/info.

        Retrieves information about the Square Catalog API, such as batch
        size
        limits that can be used by the `BatchUpsertCatalogObjects` endpoint.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/info'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_catalog(self,
                     cursor=None,
                     types=None,
                     catalog_version=None):
        """Does a GET request to /v2/catalog/list.

        Returns a list of all [CatalogObject]($m/CatalogObject)s of the
        specified types in the catalog. 
        The `types` parameter is specified as a comma-separated list of the
        [CatalogObjectType]($m/CatalogObjectType) values, 
        for example, "`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`,
        `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`".
        __Important:__ ListCatalog does not return deleted catalog items. To
        retrieve
        deleted catalog items, use
        [SearchCatalogObjects]($e/Catalog/SearchCatalogObjects)
        and set the `include_deleted_objects` attribute value to `true`.

        Args:
            cursor (string, optional): The pagination cursor returned in the
                previous response. Leave unset for an initial request. The
                page size is currently set to be 100. See
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination) for more information.
            types (string, optional): An optional case-insensitive,
                comma-separated list of object types to retrieve.  The valid
                values are defined in the
                [CatalogObjectType]($m/CatalogObjectType) enum, for example,
                `ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,
                `MODIFIER`, `MODIFIER_LIST`, `IMAGE`, etc.  If this is
                unspecified, the operation returns objects of all the top
                level types at the version of the Square API used to make the
                request. Object types that are nested onto other object types
                are not included in the defaults.  At the current API version
                the default object types are: ITEM, CATEGORY, TAX, DISCOUNT,
                MODIFIER_LIST, DINING_OPTION, TAX_EXEMPTION, SERVICE_CHARGE,
                PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT,
                SUBSCRIPTION_PLAN, ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION,
                QUICK_AMOUNT_SETTINGS.
            catalog_version (long|int, optional): The specific version of the
                catalog objects to be included in the response.  This allows
                you to retrieve historical versions of objects. The specified
                version value is matched against the
                [CatalogObject]($m/CatalogObject)s' `version` attribute.  If
                not included, results will be from the current version of the
                catalog.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/list'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'types': types,
            'catalog_version': catalog_version
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def upsert_catalog_object(self,
                              body):
        """Does a POST request to /v2/catalog/object.

        Creates or updates the target [CatalogObject]($m/CatalogObject).

        Args:
            body (UpsertCatalogObjectRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/object'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_catalog_object(self,
                              object_id):
        """Does a DELETE request to /v2/catalog/object/{object_id}.

        Deletes a single [CatalogObject]($m/CatalogObject) based on the
        provided ID and returns the set of successfully deleted IDs in the
        response.
        Deletion is a cascading event such that all children of the targeted
        object
        are also deleted. For example, deleting a
        [CatalogItem]($m/CatalogItem)
        will also delete all of its
        [CatalogItemVariation]($m/CatalogItemVariation) children.

        Args:
            object_id (string): The ID of the catalog object to be deleted.
                When an object is deleted, other objects in the graph that
                depend on that object will be deleted as well (for example,
                deleting a catalog item will delete its catalog item
                variations).

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/object/{object_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'object_id': {'value': object_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_catalog_object(self,
                                object_id,
                                include_related_objects=False,
                                catalog_version=None):
        """Does a GET request to /v2/catalog/object/{object_id}.

        Returns a single [CatalogItem]($m/CatalogItem) as a
        [CatalogObject]($m/CatalogObject) based on the provided ID. The
        returned
        object includes all of the relevant [CatalogItem]($m/CatalogItem)
        information including:
        [CatalogItemVariation]($m/CatalogItemVariation)
        children, references to its
        [CatalogModifierList]($m/CatalogModifierList) objects, and the ids of
        any [CatalogTax]($m/CatalogTax) objects that apply to it.

        Args:
            object_id (string): The object ID of any type of catalog objects
                to be retrieved.
            include_related_objects (bool, optional): If `true`, the response
                will include additional objects that are related to the
                requested objects. Related objects are defined as any objects
                referenced by ID by the results in the `objects` field of the
                response. These objects are put in the `related_objects`
                field. Setting this to `true` is helpful when the objects are
                needed for immediate display to a user. This process only goes
                one level deep. Objects referenced by the related objects will
                not be included. For example,  if the `objects` field of the
                response contains a CatalogItem, its associated
                CatalogCategory objects, CatalogTax objects, CatalogImage
                objects and CatalogModifierLists will be returned in the
                `related_objects` field of the response. If the `objects`
                field of the response contains a CatalogItemVariation, its
                parent CatalogItem will be returned in the `related_objects`
                field of the response.  Default value: `false`
            catalog_version (long|int, optional): Requests objects as of a
                specific version of the catalog. This allows you to retrieve
                historical versions of objects. The value to retrieve a
                specific version of an object can be found in the version
                field of [CatalogObject]($m/CatalogObject)s. If not included,
                results will be from the current version of the catalog.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/object/{object_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'object_id': {'value': object_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'include_related_objects': include_related_objects,
            'catalog_version': catalog_version
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def search_catalog_objects(self,
                               body):
        """Does a POST request to /v2/catalog/search.

        Searches for [CatalogObject]($m/CatalogObject) of any type by matching
        supported search attribute values,
        excluding custom attribute values on items or item variations, against
        one or more of the specified query filters.
        This (`SearchCatalogObjects`) endpoint differs from the
        [SearchCatalogItems]($e/Catalog/SearchCatalogItems)
        endpoint in the following aspects:
        - `SearchCatalogItems` can only search for items or item variations,
        whereas `SearchCatalogObjects` can search for any type of catalog
        objects.
        - `SearchCatalogItems` supports the custom attribute query filters to
        return items or item variations that contain custom attribute values,
        where `SearchCatalogObjects` does not.
        - `SearchCatalogItems` does not support the `include_deleted_objects`
        filter to search for deleted items or item variations, whereas
        `SearchCatalogObjects` does.
        - The both endpoints have different call conventions, including the
        query filter formats.

        Args:
            body (SearchCatalogObjectsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/search'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def search_catalog_items(self,
                             body):
        """Does a POST request to /v2/catalog/search-catalog-items.

        Searches for catalog items or item variations by matching supported
        search attribute values, including
        custom attribute values, against one or more of the specified query
        filters.
        This (`SearchCatalogItems`) endpoint differs from the
        [SearchCatalogObjects]($e/Catalog/SearchCatalogObjects)
        endpoint in the following aspects:
        - `SearchCatalogItems` can only search for items or item variations,
        whereas `SearchCatalogObjects` can search for any type of catalog
        objects.
        - `SearchCatalogItems` supports the custom attribute query filters to
        return items or item variations that contain custom attribute values,
        where `SearchCatalogObjects` does not.
        - `SearchCatalogItems` does not support the `include_deleted_objects`
        filter to search for deleted items or item variations, whereas
        `SearchCatalogObjects` does.
        - The both endpoints use different call conventions, including the
        query filter formats.

        Args:
            body (SearchCatalogItemsRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/search-catalog-items'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_item_modifier_lists(self,
                                   body):
        """Does a POST request to /v2/catalog/update-item-modifier-lists.

        Updates the [CatalogModifierList]($m/CatalogModifierList) objects
        that apply to the targeted [CatalogItem]($m/CatalogItem) without
        having
        to perform an upsert on the entire item.

        Args:
            body (UpdateItemModifierListsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/update-item-modifier-lists'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_item_taxes(self,
                          body):
        """Does a POST request to /v2/catalog/update-item-taxes.

        Updates the [CatalogTax]($m/CatalogTax) objects that apply to the
        targeted [CatalogItem]($m/CatalogItem) without having to perform an
        upsert on the entire item.

        Args:
            body (UpdateItemTaxesRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/catalog/update-item-taxes'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
