
```markdown
## FastAPI App Setup and Deployment Instructions

### Prerequisites
- Ensure you have Python and FastAPI installed.
- Install `uvicorn` for running the FastAPI application:
  ```bash
  pip install uvicorn
  ```

- Install `api-spec-converter` globally if not already installed:
  ```bash
  npm install -g api-spec-converter
  ```

### Running the FastAPI App
To run the FastAPI application, execute the following command in your terminal:
```bash
uvicorn main:app --reload
```
This will start the FastAPI app locally on `http://127.0.0.1:8000`.

### Saving the OpenAPI Schema
To save the OpenAPI schema, run the following `curl` command:
```bash
curl http://127.0.0.1:8000/openapi.json -o openapi_schema.json
```

### Updating the OpenAPI Schema
After saving the OpenAPI schema, open `openapi_schema.json` and change the version to `3.0.0`.

### Converting OpenAPI 3.0 to Swagger 2.0
Use `api-spec-converter` to convert the OpenAPI schema to Swagger 2.0 format:
```bash
api-spec-converter --from=openapi_3 --to=swagger_2 openapi_schema.json > openapi_spec.json
```

### Deploying to Google API Gateway
To deploy or update the API configuration in Google API Gateway, you will need to create a new API config. Each new API config requires an `x-google-backend` field with the backend service address in your OpenAPI specification.

#### **Important: Manually Add `x-google-backend`**
After updating the OpenAPI schema, **manually add** the `x-google-backend` field to your OpenAPI spec for each operation that requires it. 

#### Example of x-google-backend in OpenAPI Spec:
```yaml
paths:
  /comments:
    get:
      x-google-backend:
        address: https://YOUR_BACKEND_URL_HERE
    post:
      x-google-backend:
        address: https://YOUR_BACKEND_URL_HERE
```

### Deployment Script
1. Make sure the deployment script is executable:
   ```bash
   chmod +x deploy_to_api_gateway.sh
   ```

2. Execute the deployment script:
   ```bash
   ./deploy_to_api_gateway.sh
   ```

### Important Notes
- Ensure you have the correct API_CONFIG name set in the `deploy_to_api_gateway.sh` script for version control.
- Update any necessary fields in your OpenAPI spec as per your API requirements before deployment.

### Troubleshooting
- If you encounter errors regarding API configs or the backend address, double-check your OpenAPI specification for the presence of the `x-google-backend` field and ensure the address is correctly set.
```

